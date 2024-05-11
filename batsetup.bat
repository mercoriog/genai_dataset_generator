@echo off
REM Check if python is installed:
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [SETUP] Python3 not installed. Start installation...
    REM Install python using apt.
    curl -o python_installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
    echo [SETUP] Python3 installation done.

    REM Esegui l'installer con le opzioni per l'installazione silenziosa
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

    REM Controlla se l'installazione è avvenuta con successo
    python --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo Python 3 è stato installato con successo.
        REM Puoi inserire qui le azioni da eseguire dopo l'installazione di Python 3.
    ) else (
        echo Si è verificato un errore durante l'installazione di Python 3.
        REM Puoi inserire qui le azioni da eseguire in caso di errore durante l'installazione.
    )

) else (
    echo [SETUP] Python3 found.
)

REM Retrive current python version.
for /f "tokens=*" %%v in ('python3 --version 2^>^&1') do set "python_version=%%v"
echo [SETUP] Current python3 version: %python_version%

REM Check if pip3 is installed.
pip3 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [SETUP] pip3 not installed. Start installation...
    REM Install pip3.
    sudo apt update
    sudo apt install python3-pip
    echo [SETUP] pip3 installation done.
) else (
    echo [SETUP] pip3 found.
)

REM Check if venv installed:
dpkg -s python3-venv >nul 2>&1
if %errorlevel% equ 0 (
    echo [SETUP] venv found.
) else (
    echo [SETUP] venv non installed. Start installation...
    REM Install venv.
    sudo apt update
    sudo apt install python3-venv
    echo [SETUP] venv installation done.
)

REM Get setup script abspath.
for %%A in ("%~f0") do set "script_dir=%%~dpA"

REM Set my virtual environment name.
set "virtualenv_name=genaienv"

REM Set correct directory where to store 'genaienv'.
set "venv_path=%script_dir%\%virtualenv_name%"
echo [SETUP] 'genaienv' virtual environment path %venv_path%

echo [SETUP] Build 'genaienv' virtual environment.
REM Build virtual environment.
python3 -m venv %venv_path%

echo [SETUP] Activate 'genaienv' virtual environment.
REM Activate virtual environment.
call "%venv_path%\Scripts\activate"

REM Check if virtual environment is activated successfully:
if defined VIRTUAL_ENV (
    echo [SETUP] Virtual environment activated.
) else (
    echo [SETUP] Virtual environment NOT activated.
    exit /b 1
)

REM Correct python version.
set "desired_version=3.9.18"

REM Check if python version is '3.9.18':
echo %python_version% | findstr /i /c:"%desired_version%" >nul
if %errorlevel% neq 0 (
    echo [SETUP] Python %desired_version% required. Start installation...
    REM Install curl.
    sudo apt update
    sudo apt install curl

    REM Install pyenv.
    curl https://pyenv.run | bash
    set "PATH=%USERPROFILE%\.pyenv\bin;%PATH%"
    pyenv init --path | cmd /q /v:on
    REM Install python desired version.
    pyenv install %desired_version%
    pyenv global %desired_version%
    echo [SETUP] Python %desired_version% installation done.
) else (
    echo [SETUP] Correct python3 version installed. [Python3 %desired_version%]
)

echo [SETUP] Start downloading dependencies...
REM Install dependencies.
pip install -r requirements.txt
echo [SETUP] Dependencies installed

echo [SETUP] Deactivate 'genaienv' virtual environment.
REM Deactivate virtual environment.
deactivate

echo [SETUP] Done.
timeout /t 10 >nul
