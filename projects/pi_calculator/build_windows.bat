@echo off
setlocal
cd /d %~dp0
py -m pip install -r requirements-build.txt
if errorlevel 1 exit /b 1
py -m PyInstaller --noconfirm --clean --onefile --windowed --name PiCalculator --paths ../.. main.py
if errorlevel 1 exit /b 1
echo.
echo Build complete: projects\pi_calculator\dist\PiCalculator.exe
pause
