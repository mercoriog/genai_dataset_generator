@echo off
REM Get setup script abspath.
for /f "delims=" %%A in ("%~f0") do set "script_path=%%~dpA"

REM Get dirname from script abspath.
set "script_dir=%~dp0"

REM Set my virtual environment name.
set "virtualenv_name=genaienv"

REM Set correct directory where to store 'genaienv'.
set "venv_path=%script_dir%\%virtualenv_name%"

echo [START] Activate 'genaienv' virtual environment.

REM Activate virtual environment.
call "%venv_path%\Scripts\activate"

echo [START] Start 'genai_dataset_generator.py'...
python %script_dir%\src\main.py

echo [START] Deactivate 'genaienv' virtual environment.

REM Deactivate virtual environment.
deactivate
