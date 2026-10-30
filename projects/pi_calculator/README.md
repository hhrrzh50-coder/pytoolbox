# Pi Calculator Desktop App

A standalone Windows desktop application for calculating pi (π). It uses the Chudnovsky algorithm from the parent `pytoolbox` package and provides a simple graphical interface.

## Download for Windows

Download the portable executable directly from this repository:

[PiCalculator-Windows-Portable.exe](downloads/PiCalculator-Windows-Portable.exe)

No Python installation is required on the target Windows computer. Download the EXE, then double-click it to launch the calculator.

## Run from source

Requires Python 3.10 or newer.

From the repository root:

```bash
python -m pip install -r projects/pi_calculator/requirements-build.txt
python projects/pi_calculator/main.py
```

## Build a Windows executable

On a Windows machine with Python installed, double-click `build_windows.bat`. The script installs PyInstaller and creates `dist/PiCalculator.exe` in this project directory.

The GitHub Actions workflow also rebuilds the portable executable and places the updated file in `downloads/` in the repository.

## Use

1. Open `PiCalculator-Windows-Portable.exe`.
2. Enter the number of decimal places (0–100000).
3. Click **Calculate π**.
4. Click **Copy result** to copy the calculated digits.

The app calculates in a background thread so the window remains responsive. Very large calculations may take time and use significant memory.
