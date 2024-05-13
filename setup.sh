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

python3 -m venv genaienv

source genaienv/bin/activate

pip3 install -r requirements.txt

echo "Done."

sleep 5s
