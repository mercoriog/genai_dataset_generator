#!/bin/bash

# Check if python is installed:
if ! command -v python3 &> /dev/null
then
	echo "Python3 not installed. Start installation..."
	
	# Install python using apt.
	sudo apt install python3==3.9

	echo "Python3 installation done."
else
	echo "Python3 found."
fi

# Check python version.
python_version=$(python3 --version 2>&1)
echo "Current python3 version: $python_version"

python3 -m venv genaienv

source genaienv/Scripts/activate

# Correct python version.
desired_version="3.9.18"

# Check if python version is 3.9.18
if [[ "$python_version" != *"$desired_version"* ]]; then
	# Upgrade python to 3.9.18
	sudo apt update
	sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
	
	# Download and compile
	cd /tmp
	wget https://www.python.org/ftp/python/$desired_version/Python-$desired_version.tgz
	tar -xf Python-$desired_version.tgz
	cd Python-$desired_version
	./configure --enable-optimizations
	make -j$(nproc)
	sudo make altinstall

	# Clean .tgz archive
    cd ..
    rm -rf Python-$desired_version Python-$desired_version.tgz
else
	echo "Correct python3 version installed. [Python3 $desired_version]"
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

pip install -r requirements.txt

echo "Done."

sleep 5s
