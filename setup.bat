@echo off
echo ========================================
echo Satellite Image Change Detection Setup
echo ========================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)
echo.

echo Creating virtual environment...
if exist .venv (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully!
)
echo.

echo Activating virtual environment...
call .venv\Scripts\activate.bat
echo.

echo Installing required packages...
echo This may take a few minutes...
echo.

pip install --upgrade pip
pip install numpy matplotlib pillow pandas scipy scikit-image opencv-python
pip install streamlit plotly
pip install rasterio

if %errorlevel% neq 0 (
    echo.
    echo WARNING: Some packages may have failed to install.
    echo If rasterio failed, you can install it via conda:
    echo   conda install -c conda-forge rasterio
    echo.
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the application:
echo   1. Activate virtual environment: .venv\Scripts\activate
echo   2. Run: streamlit run app.py
echo.
echo Or simply run: run_app.bat
echo.
pause
