# pytoolbox

**A fun Python toolbox for calculating pi (π) and exploring handy utilities.**

[![Build Pi Calculator](https://github.com/hhrrzh50-coder/pytoolbox/actions/workflows/build-pi-calculator.yml/badge.svg)](https://github.com/hhrrzh50-coder/pytoolbox/actions/workflows/build-pi-calculator.yml)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](LICENSE)

Calculate π to a chosen number of decimal places with the Chudnovsky series, or use the included helpers for text, files, time, math, randomness, and validation.

## Windows Pi Calculator download

The standalone Windows portable app is kept directly in this repository:

**[Download PiCalculator-Windows-Portable.exe](projects/pi_calculator/downloads/PiCalculator-Windows-Portable.exe)**

Open the EXE on Windows; Python does not need to be installed. The file is rebuilt by the **Build Pi Calculator** GitHub Actions workflow whenever the desktop app or its calculation code changes. You can also browse the [desktop app project folder](projects/pi_calculator/).

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

The graphical app source, build script, and generated portable executable are in [projects/pi_calculator](projects/pi_calculator/). See its README for build and usage instructions.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## License

This project is released under **The Unlicense**. See [LICENSE](LICENSE) for the complete text.
