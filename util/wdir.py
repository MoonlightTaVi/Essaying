import os
from pathlib import Path


base = __file__


def abs(path: str) -> str:
    """Convert relative path to absolute."""
    if os.path.isabs(path):
        return path
    return os.path.join(wdir(), path)


def wdir() -> str:
    """Get current working directory absolute path."""
    return Path(base).absolute().parent


def exists(path: str) -> bool:
    return os.path.exists(abs(path))