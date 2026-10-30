"""Text processing helpers."""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def deduplicate(items: Iterable[T]) -> list[T]:
    """Remove duplicates while preserving the original order."""
    return list(dict.fromkeys(items))


def slugify(value: str, *, separator: str = "-") -> str:
    """Convert text into a simple ASCII-friendly URL slug."""
    if not separator:
        raise ValueError("separator must not be empty")
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    words = re.sub(r"[^a-zA-Z0-9]+", separator, ascii_text.lower()).strip(separator)
    return words


def truncate(value: str, max_length: int, *, suffix: str = "...") -> str:
    """Truncate text to max_length, including the suffix."""
    if max_length < 0:
        raise ValueError("max_length must not be negative")
    if len(value) <= max_length:
        return value
    if max_length <= len(suffix):
        return suffix[:max_length]
    return value[: max_length - len(suffix)] + suffix
