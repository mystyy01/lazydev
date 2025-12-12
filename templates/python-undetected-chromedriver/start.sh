#!/usr/bin/env bash
set -euo pipefail

echo "Starting lazydev undetected-chromedriver template..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
	echo "Creating virtual environment in ./venv"
	python -m venv venv
fi

# Activate the virtual environment
# shellcheck source=/dev/null
source venv/bin/activate

echo "Installing Python dependencies from requirements.txt (if any)"
pip install --upgrade pip
if [ -f requirements.txt ]; then
	pip install -r requirements.txt
fi

echo "Running main.py"
python main.py

echo "Done."
