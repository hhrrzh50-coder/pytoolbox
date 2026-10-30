# Pi Calculator Desktop App

A standalone desktop application for calculating pi (π). It uses the Chudnovsky algorithm from the parent `pytoolbox` package and provides a simple graphical interface.

## Run from source

Requires Python 3.10 or newer.

From the repository root:

```bash
python -m pip install -r projects/pi_calculator/requirements-build.txt
python projects/pi_calculator/main.py
```

## Build a Windows executable

On a Windows machine with Python installed, double-click `build_windows.bat`. The script installs PyInstaller and creates:

```
projects/pi_calculator/dist/PiCalculator.exe
```

The resulting executable bundles Python and the app dependencies. The target computer does not need Python installed.

## Use

1. Open PiCalculator.exe.
2. Enter the number of decimal places (0–100000).
3. Click **Calculate π**.
4. Click **Copy result** to copy the calculated digits.

The app calculates in a background thread so the window remains responsive. Very large calculations may take time and use significant memory.
