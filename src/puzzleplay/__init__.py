"""puzzleplay -- a terminal player for logicgrid puzzles.

A Textual app, chosen over a web UI because it has to be playable over SSH:
it runs in the session you are already in, with no port forwarding.

    logicgrid-play puzzles
"""

from .board import NO, YES, Board, Conflict
from .library import Library, LibraryError

__version__ = "0.1.0"
__all__ = ["Board", "Conflict", "Library", "LibraryError", "NO", "YES", "__version__"]
