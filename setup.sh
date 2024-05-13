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

# Install gdown library
pip3 install gdown

# Get setup.sh abspath.
script_path=$(readlink -f "$0")

# Get dirname from script abspath.
script_dir=$(dirname "$script_path")

# Start src/setup.py python script.
python3 $script_dir/src/setup.py

echo "Done."

sleep 5s
