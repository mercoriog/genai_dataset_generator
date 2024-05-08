#!/bin/bash

# Check if python is installed:
if ! command -v python3 &> /dev/null
then
	echo "[SETUP] Python3 not installed. Start installation..."
	
	# Install python using apt.
	sudo apt install python3==3.9

	echo "[SETUP] Python3 installation done."
else
	echo "[SETUP] Python3 found."
fi

# Retrive current python version.
python_version=$(python3 --version 2>&1)
echo "[SETUP] Current python3 version: $python_version"

# Check if pip3 is installed.
if ! command -v pip3 &> /dev/null
then
	echo "[SETUP] pip3 not installed. Start installation..."

	# Install pip3.
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
    pip install --user virtualenv
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

echo "[SETUP] Build 'genaienv' virtual environment."
# Build virtual environment.
python3 -m venv $venv_path

echo "[SETUP] Activate 'genaienv' virtual environment."
# Activate virtual environment.
source "$venv_path/bin/activate"

# Correct python version.
desired_version="3.9.18"

# Check if python version is '3.9.18':
if [[ "$python_version" != *"$desired_version"* ]]; then
	echo "[SETUP] Python $desired_version required. Start installation..."
	
	# Install curl.
	sudo apt install curl

    # Install pyenv.
    curl https://pyenv.run | bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"

    # Install python desired version.
    pyenv install $desired_version
    pyenv global $desired_version

	echo "[SETUP] Python $desired_version installation done."

else
	echo "[SETUP] Correct python3 version installed. [Python3 $desired_version]"
fi

echo "[SETUP] Start downloading dependencies..."
# Install dependencies.
pip install -r requirements.txt
echo "[SETUP] Dependencies installed"

echo "[SETUP] Deactivate 'genaienv' virtual environment."
# Deactivate virtual environment.
deactivate

echo "[SETUP] Done."
sleep 10s
