@echo off
echo Starting lazydev undetected-chromedriver template...

REM Create virtual environment if it doesn't exist
if not exist venv (
	echo Creating virtual environment in .\venv
	python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

echo Installing Python dependencies from requirements.txt (if any)
python -m pip install --upgrade pip
if exist requirements.txt (
	pip install -r requirements.txt
)

echo Running main.py
python main.py

echo Done.
pause
