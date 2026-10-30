# pytoolbox

**A fun Python toolbox for calculating pi (π) and exploring handy utilities.**

Calculate π to a chosen number of decimal places with the Chudnovsky series, or use the included helpers for text, files, time, math, randomness, and validation.

## Features

- **Pi calculator** — calculate π to a chosen number of decimal places.
- **Random helpers** — secure password generation and random choice.
- **Text helpers** — de-duplication, URL slug generation, and truncation.
- **File helpers** — UTF-8 text and JSON read/write functions.
- **Time helpers** — Unix timestamp conversion and date distance.
- **Math helpers** — clamp, mean, and median.
- **Validation helpers** — lightweight email and HTTP(S) URL checks.

## Installation

Python 3.10 or newer is required.

```bash
python -m pip install .
```

## Calculate pi

```python
from pytoolbox import calculate_pi

print(calculate_pi(50))
# 3.14159265358979323846264338327950288419716939937511
```

The result is returned as a string to preserve precision.

## Quick start

```python
from pytoolbox import random_password, slugify, clamp, is_email

print(random_password(18, symbols=True))
print(slugify("Hello, Python World!"))
print(clamp(120, 0, 100))
print(is_email("hello@example.com"))
```

## Standalone desktop project

A separate graphical pi calculator is available in [projects/pi_calculator](projects/pi_calculator/). It lets you enter the number of decimal places, calculate π, and copy the result. See its README for instructions to build a Windows `.exe` that runs without a Python installation.

The GitHub Actions workflow **Build Pi Calculator** can also build the Windows executable and upload it as a downloadable workflow artifact.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## License

This project is released under **The Unlicense**. See [LICENSE](LICENSE) for the complete text.
