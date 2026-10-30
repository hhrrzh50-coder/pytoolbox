"""Basic numeric helpers."""

from __future__ import annotations

from collections.abc import Iterable
from statistics import mean as _mean, median as _median
from typing import TypeVar

Number = TypeVar("Number", int, float)


def clamp(value: Number, minimum: Number, maximum: Number) -> Number:
    """Constrain value to the inclusive [minimum, maximum] range."""
    if minimum > maximum:
        raise ValueError("minimum must not exceed maximum")
    return max(minimum, min(value, maximum))


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean; raises ValueError for empty input."""
    data = list(values)
    if not data:
        raise ValueError("mean requires at least one value")
    return float(_mean(data))


def median(values: Iterable[float]) -> float:
    """Return the median; raises ValueError for empty input."""
    data = list(values)
    if not data:
        raise ValueError("median requires at least one value")
    return float(_median(data))
