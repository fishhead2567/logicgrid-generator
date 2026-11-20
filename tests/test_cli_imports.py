"""Every module in the package imports, and the CLI builds its parser.

Trivial, and it would have caught a real break. A syntax error was edited into
``cli.py`` and the whole 670-test suite stayed green, because nothing imported
the CLI: it is the one module with no unit tests of its own, being mostly
argument wiring and printing. So the module nobody tests was also the module
nobody noticed was broken, and the breakage surfaced only when a human ran the
command by hand.

This is not a test of behaviour. It is a test that the code parses, which is
the floor below which the other 670 tell you nothing.
"""

from __future__ import annotations

import importlib
import pkgutil

import pytest

import logicgrid


def _module_names() -> list[str]:
    return [
        f"logicgrid.{m.name}"
        for m in pkgutil.iter_modules(logicgrid.__path__)
        if not m.name.startswith("_")
    ]


def test_there_are_modules_to_check():
    # Without this, a packaging change that hides the modules would make every
    # case below vacuous and the file would still pass.
    names = _module_names()
    assert len(names) >= 8, f"only found {names}"


@pytest.mark.parametrize("name", _module_names())
def test_module_imports(name: str):
    importlib.import_module(name)


def test_cli_parser_builds():
    """The parser is where a typo in a subcommand's wiring shows up."""
    from logicgrid.cli import build_parser

    parser = build_parser()
    commands = set(parser._subparsers._group_actions[0].choices)  # type: ignore[attr-defined]
    assert {"gen", "show", "solve", "stats", "themes", "narrate"} <= commands


def test_every_subcommand_has_a_handler():
    from logicgrid.cli import build_parser

    parser = build_parser()
    choices = parser._subparsers._group_actions[0].choices  # type: ignore[attr-defined]
    missing = [name for name, sub in choices.items() if not sub.get_default("func")]
    assert not missing, f"subcommands with no func: {missing}"
