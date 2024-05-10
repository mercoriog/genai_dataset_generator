# Check if python version is '3.9.18':
if [[ "$python_version" != *"$desired_version"* ]]; then
	echo "[SETUP] Python $desired_version required. Start installation..."
	
	# Install curl.
	sudo apt update
	sudo apt install curl

	echo "[SETUP] pyenv required. Start installation..."
    # Install pyenv.
    curl https://pyenv.run | bash
    export PYENV_ROOT="$HOME/.pyenv"
    [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    eval "$(pyenv virtualenv-init -)"

    # Install python desired version.
    pyenv install $desired_version
    pyenv global $desired_version

	echo "[SETUP] Python $desired_version installation done."

else
	echo "[SETUP] Correct python3 version installed. [Python3 $desired_version]"
fi

# Activate virtual environment.
source "$venv_path/bin/activate"

# Check if virtual environment is activated successfully:
if [[ $VIRTUAL_ENV != "" ]]; then
    echo "[SETUP] Virtual environment activated."
else
    echo "[SETUP] Virtual environment NOT activated."
    exit 1
fi

echo "[SETUP] Start downloading dependencies..."
# Install dependencies.
pip install -r requirements.txt
echo "[SETUP] Dependencies installed"
