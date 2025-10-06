@echo off
echo ========================================
echo Starting Satellite Change Detection App
echo ========================================
echo.

REM Check if virtual environment exists
if not exist .venv (
    echo Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if streamlit is installed
python -c "import streamlit" 2>nul
if %errorlevel% neq 0 (
    echo Streamlit is not installed!
    echo Installing now...
    pip install streamlit
)

echo.
echo Launching Streamlit Dashboard...
echo The app will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause
