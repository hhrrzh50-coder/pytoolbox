"""A fun Python toolbox that can calculate pi to high precision."""

from .math_tools import clamp, mean, median
from .pi import calculate_pi
from .random_tools import random_password, random_choice
from .text_tools import deduplicate, slugify, truncate
from .time_tools import timestamp_to_datetime, days_between
from .validators import is_email, is_url

__all__ = [
    "clamp", "mean", "median", "calculate_pi",
    "random_password", "random_choice",
    "deduplicate", "slugify", "truncate",
    "timestamp_to_datetime", "days_between",
    "is_email", "is_url",
]

__version__ = "0.2.0"
