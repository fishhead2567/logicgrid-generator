"""A thin Claude API wrapper for the narrative round-trip.

Deliberately small: one model config, one call, plus concurrent and batch
helpers.  Nothing here knows about puzzles -- :mod:`logicgrid.narrate` and
:mod:`logicgrid.extract` own the prompts.

The ``anthropic`` package is an optional dependency (``pip install
logicgrid[llm]``).  Importing this module without it is fine; only
:meth:`Client.complete` needs it, and :class:`DryRunClient` lets the whole
pipeline be exercised with no key and no spend.
"""

from __future__ import annotations

import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Sequence

#: Narration wants a strong model; extraction is the gate, so accuracy matters
#: there too.  Both default to the current Opus.  Override per role if you want
#: to trade accuracy for cost -- e.g. ``ModelConfig(model="claude-haiku-5-5")``
#: for the extractor, which is the bulk of the calls (3 per puzzle).
DEFAULT_MODEL = "claude-opus-5-5"

#: Server-side refusal fallback.  A logic puzzle is not going to trip a safety
#: classifier, but a declined request would otherwise just stop, so the chain is
#: cheap insurance on a long batch run.
FALLBACK_BETA = "server-side-fallback-2026-07-01"
DEFAULT_FALLBACK = "claude-opus-4-8"


class LLMError(RuntimeError):
    """Any failure talking to the model, including refusals."""


@dataclass(frozen=True, slots=True)
class ModelConfig:
    model: str = DEFAULT_MODEL
    max_tokens: int = 16000
    effort: str = "high"  # low | medium | high | xhigh | max
    #: ``None`` disables the server-side refusal fallback.
    fallback: str | None = DEFAULT_FALLBACK
    temperature_note: str = ""  # kept for provenance only; sampling params are rejected

    def describe(self) -> str:
        return f"{self.model} (effort={self.effort})"


@dataclass(slots=True)
class Request:
    """One prompt, with an optional JSON schema to constrain the reply."""

    system: str
    user: str
    schema: Mapping[str, Any] | None = None
    key: str = ""


@dataclass(slots=True)
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read: int = 0
    calls: int = 0

    def add(self, other: "Usage") -> None:
        self.input_tokens += other.input_tokens
        self.output_tokens += other.output_tokens
        self.cache_read += other.cache_read
        self.calls += other.calls

    def cost(self, model: str = DEFAULT_MODEL) -> float:
        """Rough USD estimate using first-party rates for the common models."""
        rates = {
            "claude-opus-5-5": (4.00, 20.00),
            "claude-opus-5": (5.00, 25.00),
            "claude-sonnet-5-5": (2.00, 10.00),
            "claude-haiku-5-5": (0.10, 0.50),
        }
        rin, rout = rates.get(model, (4.00, 20.00))
        return (self.input_tokens * rin + self.output_tokens * rout) / 1e6

    def summary(self, model: str = DEFAULT_MODEL) -> str:
        return (
            f"{self.calls} calls, {self.input_tokens:,} in / "
            f"{self.output_tokens:,} out tokens, ~${self.cost(model):.3f}"
        )


class Client:
    """Minimal Claude client. Set ``ANTHROPIC_API_KEY`` or pass ``api_key``."""

    def __init__(self, api_key: str | None = None, config: ModelConfig | None = None) -> None:
        try:
            import anthropic  # noqa: PLC0415
        except ImportError as exc:  # pragma: no cover - env dependent
            raise LLMError(
                "the 'anthropic' package is required for live calls: "
                "pip install 'logicgrid[llm]'"
            ) from exc
        self._anthropic = anthropic
        key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        # A bare client also picks up ANTHROPIC_AUTH_TOKEN or an `ant auth
        # login` profile, so an unset API key is not necessarily an error.
        self._client = anthropic.Anthropic(api_key=key) if key else anthropic.Anthropic()
        self.config = config or ModelConfig()
        self.usage = Usage()

    # -- single call -----------------------------------------------------
    def complete(self, request: Request, config: ModelConfig | None = None) -> str:
        cfg = config or self.config
        output_config: dict[str, Any] = {"effort": cfg.effort}
        if request.schema is not None:
            output_config["format"] = {"type": "json_schema", "schema": request.schema}

        kwargs: dict[str, Any] = {
            "model": cfg.model,
            "max_tokens": cfg.max_tokens,
            "system": request.system,
            "messages": [{"role": "user", "content": request.user}],
            "output_config": output_config,
        }
        try:
            if cfg.fallback:
                response = self._client.beta.messages.create(
                    betas=[FALLBACK_BETA],
                    fallbacks=[{"model": cfg.fallback}],
                    **kwargs,
                )
            else:
                response = self._client.messages.create(**kwargs)
        except self._anthropic.APIStatusError as exc:
            raise LLMError(f"{cfg.model}: {exc}") from exc

        if getattr(response, "stop_reason", None) == "refusal":
            detail = getattr(response, "stop_details", None)
            raise LLMError(f"request refused ({getattr(detail, 'category', '?')})")
        if getattr(response, "stop_reason", None) == "max_tokens":
            raise LLMError(
                f"reply hit max_tokens ({cfg.max_tokens}); raise it and retry"
            )

        u = response.usage
        self.usage.add(
            Usage(
                input_tokens=getattr(u, "input_tokens", 0) or 0,
                output_tokens=getattr(u, "output_tokens", 0) or 0,
                cache_read=getattr(u, "cache_read_input_tokens", 0) or 0,
                calls=1,
            )
        )
        for block in response.content:
            if block.type == "text" and block.text.strip():
                return block.text
        raise LLMError("model returned no text content")

    # -- many calls ------------------------------------------------------
    def complete_many(
        self,
        requests: Sequence[Request],
        config: ModelConfig | None = None,
        max_workers: int = 4,
        on_done: Callable[[int, str | Exception], None] | None = None,
    ) -> list[str | Exception]:
        """Run prompts concurrently. Exceptions are returned, not raised."""
        results: list[str | Exception] = [LLMError("not run")] * len(requests)

        def run(i: int) -> None:
            try:
                results[i] = self.complete(requests[i], config)
            except Exception as exc:  # noqa: BLE001 - surfaced per-item
                results[i] = exc
            if on_done is not None:
                on_done(i, results[i])

        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            list(pool.map(run, range(len(requests))))
        return results

    # -- batch api -------------------------------------------------------
    def complete_batch(
        self,
        requests: Sequence[Request],
        config: ModelConfig | None = None,
        poll_seconds: float = 20.0,
        timeout_seconds: float = 24 * 3600,
        on_status: Callable[[str, int], None] | None = None,
    ) -> list[str | Exception]:
        """Run prompts through the Batches API at half price.

        Worth it for a full 50-puzzle run (200 calls) when you are not waiting
        on the result.  Results come back in arbitrary order, so they are keyed
        by ``custom_id`` and reordered here.
        """
        cfg = config or self.config
        if cfg.fallback:
            # The fallbacks parameter is rejected on the Batches API.
            cfg = ModelConfig(cfg.model, cfg.max_tokens, cfg.effort, None)

        payload = []
        for i, req in enumerate(requests):
            output_config: dict[str, Any] = {"effort": cfg.effort}
            if req.schema is not None:
                output_config["format"] = {"type": "json_schema", "schema": req.schema}
            payload.append(
                {
                    "custom_id": f"r{i}",
                    "params": {
                        "model": cfg.model,
                        "max_tokens": cfg.max_tokens,
                        "system": req.system,
                        "messages": [{"role": "user", "content": req.user}],
                        "output_config": output_config,
                    },
                }
            )

        batch = self._client.messages.batches.create(requests=payload)
        deadline = time.monotonic() + timeout_seconds
        while True:
            batch = self._client.messages.batches.retrieve(batch.id)
            if on_status is not None:
                counts = getattr(batch, "request_counts", None)
                done = (getattr(counts, "succeeded", 0) or 0) if counts else 0
                on_status(batch.processing_status, done)
            if batch.processing_status == "ended":
                break
            if time.monotonic() > deadline:
                raise LLMError(f"batch {batch.id} did not finish within the timeout")
            time.sleep(poll_seconds)

        results: list[str | Exception] = [LLMError("missing from batch")] * len(requests)
        for entry in self._client.messages.batches.results(batch.id):
            try:
                idx = int(str(entry.custom_id)[1:])
            except (ValueError, IndexError):  # pragma: no cover - defensive
                continue
            if entry.result.type != "succeeded":
                results[idx] = LLMError(f"batch item {entry.custom_id}: {entry.result.type}")
                continue
            message = entry.result.message
            text = next(
                (b.text for b in message.content if b.type == "text" and b.text.strip()),
                None,
            )
            if text is None:
                results[idx] = LLMError("batch item returned no text")
            else:
                results[idx] = text
            u = message.usage
            self.usage.add(
                Usage(
                    input_tokens=getattr(u, "input_tokens", 0) or 0,
                    output_tokens=getattr(u, "output_tokens", 0) or 0,
                    calls=1,
                )
            )
        return results


class DryRunClient:
    """Records prompts and returns canned replies. No network, no spend.

    Used by ``--dry-run`` to prove the prompts assemble and the plumbing works
    before any key is configured.  ``replies`` is consumed in order; when it
    runs out, an empty string is returned.
    """

    def __init__(self, replies: Sequence[str] = ()) -> None:
        self.prompts: list[Request] = []
        self.replies = list(replies)
        self.usage = Usage()
        self.config = ModelConfig()

    def complete(self, request: Request, config: ModelConfig | None = None) -> str:
        self.prompts.append(request)
        self.usage.add(Usage(calls=1))
        return self.replies.pop(0) if self.replies else ""

    def complete_many(
        self,
        requests: Sequence[Request],
        config: ModelConfig | None = None,
        max_workers: int = 4,
        on_done: Callable[[int, str | Exception], None] | None = None,
    ) -> list[str | Exception]:
        # Mirrors the live client's contract: a failing call is *returned* as an
        # exception, never raised, so one bad reader cannot abort a whole run.
        out: list[str | Exception] = []
        for i, req in enumerate(requests):
            try:
                out.append(self.complete(req, config))
            except Exception as exc:  # noqa: BLE001 - surfaced per-item
                out.append(exc)
            if on_done is not None:
                on_done(i, out[-1])
        return out

    complete_batch = complete_many
