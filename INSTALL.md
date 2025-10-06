# Installation Guide - Satellite Image Change Detection System

## Quick Setup (Recommended)

### Option 1: Using Conda (Easiest for GDAL/Rasterio)

```bash
# Create a new conda environment
conda create -n satellite-analysis python=3.10 -y
conda activate satellite-analysis

# Install GDAL and rasterio via conda (avoids compilation issues)
conda install -c conda-forge rasterio gdal -y

# Install remaining packages via pip
pip install numpy matplotlib scikit-image opencv-python streamlit plotly pandas Pillow scipy geopandas folium streamlit-folium
```

### Option 2: Using pip (Windows)

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install packages one by one to handle dependencies
pip install numpy
pip install matplotlib
pip install pandas
pip install Pillow
pip install scipy
pip install scikit-image
pip install opencv-python
pip install plotly
pip install streamlit
pip install geopandas
pip install folium
pip install streamlit-folium

# Install rasterio (may require Visual C++ Build Tools)
pip install rasterio
```

### Option 3: Simplified Requirements (if rasterio fails)

If you have trouble installing rasterio, you can use this simplified version:

```bash
pip install numpy matplotlib scikit-image opencv-python streamlit plotly pandas Pillow scipy
```

Then modify the code to use PIL/OpenCV for basic TIFF reading instead of rasterio.

## Verify Installation

Run the quick start check:

```bash
python quick_start.py
```

## Troubleshooting

### Issue: Rasterio installation fails

**Solution 1**: Use conda (recommended)
```bash
conda install -c conda-forge rasterio
```

**Solution 2**: Install pre-built wheel
- Download from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#rasterio
- Install: `pip install rasterio‑1.3.9‑cp310‑cp310‑win_amd64.whl`

**Solution 3**: Install GDAL first
```bash
conda install -c conda-forge gdal
pip install rasterio
```

### Issue: Import errors

Make sure your virtual environment is activated:
```bash
# Check Python path
python -c "import sys; print(sys.executable)"

# Should point to your venv directory
```

### Issue: Memory errors with large images

- Close other applications
- Process images in chunks
- Use lower resolution versions for initial testing

## Running the Application

### Interactive Dashboard
```bash
streamlit run app.py
```

### Python Script
```bash
python example_usage.py
```

### Quick Test
```bash
python quick_start.py
```

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: 500MB for dependencies
- **OS**: Windows 10/11, Linux, macOS

## Dependencies Explained

- **rasterio**: Reading GeoTIFF satellite images
- **numpy**: Numerical computations
- **matplotlib**: Creating visualizations
- **scikit-image**: Image processing algorithms
- **opencv-python**: Computer vision operations
- **streamlit**: Interactive web dashboard
- **plotly**: Interactive plots
- **pandas**: Data analysis and statistics
- **scipy**: Scientific computing

## Next Steps

After successful installation:

1. ✓ Verify your satellite images are in the project folder
2. ✓ Run `python quick_start.py` to check everything
3. ✓ Launch the dashboard: `streamlit run app.py`
4. ✓ Explore the example: `python example_usage.py`

## Support

If you encounter issues:

1. Check the Python version: `python --version`
2. Verify virtual environment is activated
3. Try the conda installation method
4. Review error messages carefully
5. Install packages individually to isolate problems

## Alternative: Docker (Advanced)

If you prefer containerization:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

Build and run:
```bash
docker build -t satellite-analysis .
docker run -p 8501:8501 satellite-analysis
```
