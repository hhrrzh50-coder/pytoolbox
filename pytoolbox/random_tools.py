"""Random value helpers."""

from __future__ import annotations

import secrets
import string
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def random_password(
    length: int = 16,
    *,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    symbols: bool = False,
) -> str:
    """Generate a cryptographically secure password.

    Raises ValueError when length is non-positive or no character groups are enabled.
    """
    if length < 1:
        raise ValueError("length must be at least 1")

    groups = []
    if uppercase:
        groups.append(string.ascii_uppercase)
    if lowercase:
        groups.append(string.ascii_lowercase)
    if digits:
        groups.append(string.digits)
    if symbols:
        groups.append("!@#$%^&*()-_=+[]{};:,.?")
    if not groups:
        raise ValueError("at least one character group must be enabled")
    if length < len(groups):
        raise ValueError("length must be at least the number of enabled character groups")

    chars = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    chars.extend(secrets.choice(alphabet) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def random_choice(items: Sequence[T]) -> T:
    """Choose one item from a non-empty sequence."""
    if not items:
        raise ValueError("items must not be empty")
    return secrets.choice(items)
