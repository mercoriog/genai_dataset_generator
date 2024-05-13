@echo off
REM Install gdown library
pip install gdown

REM Get setup.sh abspath.
for /f "delims=" %%A in ("%~f0") do set "script_path=%%~dpA"

REM Start src\setup.py python script.
python %script_path%src\setup.py

echo Done.

timeout /t 5 >nul