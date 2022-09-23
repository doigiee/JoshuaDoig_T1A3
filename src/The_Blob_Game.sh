#!/bin/bash

echo "Welcome to The Blob Game!"

echo "Checking for virtual environment"
FILE=.venv
if [ -d "$FILE" ]; then
    echo "The Virtual environment exists"
else
    echo "Creating virtual environment"
    python3 -m venv .venv
    source .venv/bin/activate
fi

echo "Checking for other dependecies install status"

pip install -r requirements.txt

echo "All python packages are now installed, running main application"

python3 main.py