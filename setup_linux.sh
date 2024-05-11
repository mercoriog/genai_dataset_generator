#!/bin/bash

# Check if python is installed:
if ! command -v python3 &> /dev/null
then
	echo "[SETUP] Python3 not installed. Start installation..."
	
	# Install python using apt.
	sudo apt update
	sudo apt install python3

	echo "[SETUP] Python3 installation done."
else
	echo "[SETUP] Python3 found."
fi

# Check if pip3 is installed.
if ! command -v pip3 &> /dev/null
then
	echo "[SETUP] pip3 not installed. Start installation..."

	# Install pip3.
	sudo apt update
	sudo apt install python3-pip

	echo "[SETUP] pip3 installation done."
else
	echo "[SETUP] pip3 found."
fi

# Check if venv installed:
if dpkg -s python3-venv &> /dev/null; then
    echo "[SETUP] venv found."
else
    echo "[SETUP] venv non installed. Start installation..."
    # Install venv. 
    sudo apt update
    sudo apt install python3-venv
    echo "[SETUP] venv installation done."
fi

# Get setup script abspath.
script_path=$(readlink -f "$0")

# Get dirname from script abspath.
script_dir=$(dirname "$script_path")

# Set my virtual environment name.
virtualenv_name="genaienv"

# Set correct directory where to store 'genaienv'.
venv_path="$script_dir/$virtualenv_name"
echo "[SETUP] 'genaienv' virtual environment path $venv_path"

echo "[SETUP] Build 'genaienv' virtual environment."
# Build virtual environment.
python3 -m venv $venv_path

echo "[SETUP] Activate 'genaienv' virtual environment."
# Activate virtual environment.
source "$venv_path/bin/activate"

# Check if virtual environment is activated successfully:
if [[ $VIRTUAL_ENV != "" ]]; then
    echo "[SETUP] Virtual environment activated."
else
    echo "[SETUP] Virtual environment NOT activated."
    exit 1
fi

# Install dependencies inside the virtual environment.
echo "[SETUP] Start downloading dependencies..."
pip install -r requirements.txt
echo "[SETUP] Dependencies installed"

echo "[SETUP] Deactivate 'genaienv' virtual environment."
# Deactivate virtual environment.
deactivate

echo "[SETUP] Done."
sleep 10s
