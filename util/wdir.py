import os


def abs(path: str) -> str:
    """Convert relative path to absolute."""
    if os.path.isabs(path):
        return path
    return os.path.abspath(path)


def wdir() -> str:
    """Get current working directory absolute path."""
    return abs(os.curdir)


def exists(path: str) -> bool:
    return os.path.exists(abs(path))