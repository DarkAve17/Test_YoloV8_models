@echo off
ECHO ===================================
ECHO  Project Setup & Execution Script 
ECHO ===================================

:: This script assumes you have Python installed and in your PATH,
:: and a requirements.txt file exists in this directory.

:: 1. Check for the virtual environment and create it if it's missing.
IF NOT EXIST "venv" (
    ECHO [+] Creating virtual environment...
    python -m venv venv
) ELSE (
    ECHO [*] Virtual environment already exists.
)

:: 2. Activate the venv and install dependencies.
ECHO [+] Activating environment and installing dependencies...
CALL .\venv\Scripts\activate.bat
pip install -r requirements.txt

:: 3. Run the main Python script.
ECHO [+] Running the Python script (test.py)...
ECHO -----------------------------------
python test.py
ECHO -----------------------------------

ECHO.
ECHO Script has finished. Press any key to exit.
pause > nul