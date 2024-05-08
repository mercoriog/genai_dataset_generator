#!/bin/bash

# Get setup script abspath.
script_path=$(readlink -f "$0")

# Get dirname from script abspath.
script_dir=$(dirname "$script_path")

# Set my virtual environment name.
virtualenv_name="genaienv"

# Set correct directory where to store 'genaienv'.
venv_path="$script_dir/$virtualenv_name"

echo "[START] Activate 'genaienv' virtual environment."
# Activate virtual environment.
source "$venv_path/bin/activate"

echo "[START] Start 'genai_dataset_generator.py'..."
python3 $script_dir/src/main.py

echo "[START] Deactivate 'genaienv' virtual environment."
# Deactivate virtual environment.
deactivate

