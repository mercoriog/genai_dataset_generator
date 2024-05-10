#!/bin/bash

# Check if python is installed:
if ! command -v python3 &> /dev/null
then
	echo "[SETUP] Python3 not installed. Start installation..."
	
	# Install python using apt.
	sudo apt update
	sudo apt install python3==3.9

	echo "[SETUP] Python3 installation done."
else
	echo "[SETUP] Python3 found."
fi

# Get setup.sh abspath.
script_path=$(readlink -f "$0")

# Get dirname from script abspath.
script_dir=$(dirname "$script_path")

# Start src/setup.py python script.
python3 $script_dir/src/setup.py

echo "Done."

sleep 5s
