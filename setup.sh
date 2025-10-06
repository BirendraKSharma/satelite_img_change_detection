#!/bin/bash

echo "========================================"
echo "Satellite Image Change Detection Setup"
echo "========================================"
echo ""

echo "Checking Python installation..."
python --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python is not installed or not in PATH"
    exit 1
fi
echo ""

echo "Creating virtual environment..."
if [ -d ".venv" ]; then
    echo "Virtual environment already exists, skipping..."
else
    python -m venv .venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created successfully!"
fi
echo ""

echo "Activating virtual environment..."
source .venv/Scripts/activate
echo ""

echo "Installing required packages..."
echo "This may take a few minutes..."
echo ""

pip install --upgrade pip
pip install numpy matplotlib pillow pandas scipy scikit-image opencv-python
pip install streamlit plotly
pip install rasterio

if [ $? -ne 0 ]; then
    echo ""
    echo "WARNING: Some packages may have failed to install."
    echo "If rasterio failed, you can install it via conda:"
    echo "  conda install -c conda-forge rasterio"
    echo ""
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To run the application:"
echo "  1. Activate virtual environment: source .venv/Scripts/activate"
echo "  2. Run: streamlit run app.py"
echo ""
echo "Or simply run: ./run_app.sh"
echo ""
