"""Small, safe file-system helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_text(path: str | Path, *, encoding: str = "utf-8") -> str:
    """Read a text file using the requested encoding."""
    return Path(path).read_text(encoding=encoding)


def write_text(
    path: str | Path,
    content: str,
    *,
    encoding: str = "utf-8",
    create_parents: bool = True,
) -> Path:
    """Write text to a file and return its resolved path."""
    target = Path(path)
    if create_parents:
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding=encoding)
    return target


def read_json(path: str | Path, *, encoding: str = "utf-8") -> Any:
    """Load JSON data from a file."""
    with Path(path).open("r", encoding=encoding) as stream:
        return json.load(stream)


def write_json(
    path: str | Path,
    data: Any,
    *,
    indent: int = 2,
    encoding: str = "utf-8",
) -> Path:
    """Write JSON data with readable indentation."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding=encoding) as stream:
        json.dump(data, stream, ensure_ascii=False, indent=indent)
        stream.write("\n")
    return target
