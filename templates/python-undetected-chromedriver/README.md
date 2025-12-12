How to set up the lazydev python-undetected-chromedriver template

1. Create a virtual environment
```
python -m venv venv
```
1a. Source your virtual environment
```
source venv/bin/activate
```
2. Install requirements
```
pip install -r requirements.txt
```
3. Make the start script executable (if present)
```
chmod +x start.sh
```
4. Run it
```
./start.sh
```
On Windows (PowerShell / CMD) run `start.bat`

5. Notes
- This template uses `undetected-chromedriver` to run Chromium-based browsers without detection in automation. Ensure you have a compatible browser installed on your system (for example, Google Chrome).

6. Have fun and build a great app!

lazydev © 2025
