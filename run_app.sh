#!/bin/bash

echo "========================================"
echo "Starting Satellite Change Detection App"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found!"
    echo "Please run setup.sh first"
    exit 1
fi

# Activate virtual environment
source .venv/Scripts/activate

# Check if streamlit is installed
python -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Streamlit is not installed!"
    echo "Installing now..."
    pip install streamlit
fi

echo ""
echo "Launching Streamlit Dashboard..."
echo "The app will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
