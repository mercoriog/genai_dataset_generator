#!/bin/bash

python -m venv genaienv

source genaienv/Scripts/activate

pip install -r requirements.txt

echo "Done."

sleep 5s
