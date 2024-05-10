# Check if python version is '3.9.18':
if [[ "$python_version" != *"$desired_version"* ]]; then
	

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
