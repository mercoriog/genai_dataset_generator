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

# Check venv installed
if dpkg -s python3-venv &> /dev/null; then
    echo "venv found."
else
    echo "venv non installed. Start installation..."
    spip install --user virtualenv
    echo "venv installation done."
fi

python3 -m venv genaienv

source genaienv/Scripts/activate

# Correct python version.
desired_version="3.9.18"

# Check if python version is 3.9.18
if [[ "$python_version" != *"$desired_version"* ]]; then
	# Upgrade python to 3.9.18
	# Installa una specifica versione di Python con pyenv
    curl https://pyenv.run | bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"

    pyenv install $desired_version
    pyenv global $desired_version

else
	echo "Correct python3 version installed. [Python3 $desired_version]"
fi


pip install -r requirements.txt

echo "Done."

sleep 5s
