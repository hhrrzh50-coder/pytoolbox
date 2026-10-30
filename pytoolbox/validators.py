"""Lightweight format validators (not full standards parsers)."""

from __future__ import annotations

import re
from urllib.parse import urlparse

_EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def is_email(value: str) -> bool:
    """Return whether value resembles an email address."""
    return bool(_EMAIL_RE.fullmatch(value))


def is_url(value: str) -> bool:
    """Return whether value has an HTTP(S) scheme and a hostname."""
    try:
        parsed = urlparse(value)
        return parsed.scheme in {"http", "https"} and bool(parsed.hostname)
    except ValueError:
        return False


def is_non_empty_string(value: object) -> bool:
    """Return whether value is a string containing non-whitespace characters."""
    return isinstance(value, str) and bool(value.strip())
