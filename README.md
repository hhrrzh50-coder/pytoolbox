# pytoolbox

A small collection of practical, dependency-free Python utilities for everyday projects.

## Features

- **Random helpers** — cryptographically secure password generation and random choice.
- **Text helpers** — stable de-duplication, URL slug generation, and truncation.
- **File helpers** — UTF-8 text and JSON read/write functions.
- **Time helpers** — Unix timestamp conversion and date distance.
- **Math helpers** — clamp, mean, and median.
- **Validation helpers** — lightweight email and HTTP(S) URL checks.

## Installation

Python 3.10 or newer is required.

```bash
python -m pip install .
```

## Quick start

```python
from pytoolbox import random_password, slugify, clamp, is_email

print(random_password(18, symbols=True))
print(slugify("Hello, Python World!"))
print(clamp(120, 0, 100))
print(is_email("hello@example.com"))
```

File helpers can be imported from their module:

```python
from pytoolbox.file_tools import read_json, write_json

write_json("data/settings.json", {"theme": "dark"})
settings = read_json("data/settings.json")
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## License

This project is released under **The Unlicense**. See [LICENSE](LICENSE) for the complete text.
