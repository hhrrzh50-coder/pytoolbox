"""Date and time helpers."""

from __future__ import annotations

from datetime import date, datetime, timezone


def timestamp_to_datetime(timestamp: int | float, *, utc: bool = True) -> datetime:
    """Convert a Unix timestamp to a timezone-aware datetime."""
    tz = timezone.utc if utc else None
    result = datetime.fromtimestamp(timestamp, tz=tz)
    if not utc:
        return result.astimezone()
    return result


def days_between(start: date | datetime, end: date | datetime) -> int:
    """Return the absolute whole-day distance between two dates."""
    return abs((end.date() - start.date()).days if isinstance(start, datetime) and isinstance(end, datetime)
               else (end - start).days)


def now_utc() -> datetime:
    """Return the current UTC time as an aware datetime."""
    return datetime.now(timezone.utc)
