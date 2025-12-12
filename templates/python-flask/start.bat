@echo off
REM start flask dev server on Windows (cmd)
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host 0.0.0.0 --port 5555
