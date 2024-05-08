#!/bin/bash

# Check if python is installed:
if ! command -v python3 &> /dev/null
then
	echo "Python3 not installed. Start installation..."
	
	# Install python using apt.
	sudo apt install python3==3.9.18

	echo "Python3 installation done."
else
	echo "Python3 found."
fi

# Check python version.
python_version=$(python --version 2>&1)
echo "Current python3 version: $python_version"

# Correct python version.
correct_python_version="3.9.18"

# Check if python version is 3.9.18
if [[ "$python_version" != *"$correct_python_version"* ]]; then
	# Upgrade python to 3.9.18
	sudo apt install --only-upgrade python3=="$correct_python_version"
else
	echo "Correct python3 version installed. [Python3 $correct_python_version]"
fi

# Check if pip3 is installed.
if ! command -v pip3 &> /dev/null
then
	echo "pip3 not installed. Start installation..."

	# Install pip3.
	sudo apt install python3-pip

	echo "pip3 installation done."
else
	echo "pip3 found."
fi

python3 -m venv genaienv

source genaienv/Scripts/activate

pip install -r requirements.txt

echo "Done."

sleep 5s
