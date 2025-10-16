@echo off
title Python 3.10 Installer (No Admin)
color 0a

echo ============================================
echo   Python 3.10 Auto Installer (No Admin)
echo   Installs pip + dependencies + runs main.py
echo ============================================
echo.

set PYTHON_URL=https://www.python.org/ftp/python/3.10.13/python-3.10.13-amd64.exe
set PYTHON_PATH=%USERPROFILE%\AppData\Local\Programs\Python310
set INSTALLER=%TEMP%\python310_installer.exe

echo [1/6] Downloading Python 3.10 installer...
powershell -Command "Invoke-WebRequest '%PYTHON_URL%' -OutFile '%INSTALLER%'"

echo [2/6] Installing Python 3.10 (user mode, no admin)...
start /wait "" "%INSTALLER%" /quiet InstallAllUsers=0 PrependPath=0 Include_pip=1 TargetDir="%PYTHON_PATH%"

set "PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%"

echo [3/6] Ensuring pip is installed...
python -m ensurepip --default-pip

echo [4/6] Installing dependencies: pyautogui, keyboard, colorama...
python -m pip install --user pyautogui keyboard colorama

echo [5/6] Adding Python 3.10 to your user PATH...
powershell -Command "[Environment]::SetEnvironmentVariable('Path', '%PYTHON_PATH%;%PYTHON_PATH%\Scripts;' + [Environment]::GetEnvironmentVariable('Path','User'), 'User')"

echo [6/6] Running main.py (if found)...
if exist main.py (
    python main.py
) else (
    echo main.py not found in this folder, skipping run.
)

echo.
echo ✅ All done! Python 3.10 is installed without admin.
pause
