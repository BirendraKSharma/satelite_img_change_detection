# 🛰️ Satellite Image Change Detection System

A comprehensive Business Intelligence solution for analyzing temporal changes in satellite imagery from NASA. This system provides advanced change detection algorithms and an interactive GUI dashboard for environmental monitoring.

## 📋 Overview

This system analyzes GIS satellite image data to detect and visualize changes in natural and anthropological environments between two time periods. It's designed for environmental monitoring, urban planning, deforestation tracking, and disaster assessment.

## ✨ Features

### Change Detection Methods
1. **Threshold-based Detection** - Simple pixel difference with configurable threshold
2. **Otsu Auto-thresholding** - Automatic optimal threshold calculation
3. **Change Vector Detection (CVD)** - Multi-spectral magnitude analysis
4. **Vegetation Analysis** - NDVI-based vegetation health monitoring

### Visualization & Analysis
- Side-by-side temporal comparison
- Change intensity heatmaps
- Binary change maps
- NDVI vegetation indices
- Statistical analysis and reporting
- Interactive BI dashboard

### Business Intelligence Features
- Real-time KPIs and metrics
- Change region statistics
- Vegetation loss/gain tracking
- Export capabilities (CSV)
- Interactive parameter tuning

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Windows/Linux/Mac OS

### Installation

1. **Clone or navigate to the project directory**
```bash
cd d:\programming\project\Satelite_Image_detection
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows with bash
# or
venv\Scripts\activate.bat      # On Windows with cmd
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

### Running the Application

#### Option 1: Interactive Dashboard (Recommended)
```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

#### Option 2: Python Script
```python
from change_detector import ChangeDetector

# Initialize detector
detector = ChangeDetector(
    'snapshot-2025-10-01T00_00_00Z.tif',
    'snapshot-2025-10-06T00_00_00Z.tif'
)

# Load images
detector.load_images()

# Detect changes
change_map = detector.detect_changes_threshold(threshold=0.15)

# Get statistics
stats = detector.analyze_change_statistics(change_map)
print(stats)

# Vegetation analysis
veg_results = detector.detect_vegetation_change()
```

## 📊 Usage Guide

### Dashboard Navigation

1. **Configuration Panel (Sidebar)**
   - Select earlier and later images
   - Choose detection method
   - Adjust sensitivity thresholds
   - Run analysis

2. **Key Performance Indicators**
   - Total area analyzed
   - Changed area percentage
   - Number of change regions
   - Average region size

3. **Visualizations**
   - Temporal image comparison
   - Change overlay (red highlights)
   - Binary change map
   - Intensity heatmap
   - NDVI indices (vegetation mode)

4. **Export**
   - Download change maps as CSV
   - Export statistics and reports

### Detection Methods Explained

#### 1. Threshold-based Detection
- **Use Case**: General change detection
- **Parameter**: Threshold (0.0 - 1.0)
- **Best For**: Quick analysis, clear changes
- **Recommendation**: Start with 0.15, adjust as needed

#### 2. Otsu Auto-threshold
- **Use Case**: Automatic threshold selection
- **Parameter**: None (automatic)
- **Best For**: Unknown optimal threshold
- **Recommendation**: Good first approach

#### 3. Change Vector Detection
- **Use Case**: Multi-spectral analysis
- **Parameter**: CVD Threshold (0.0 - 0.5)
- **Best For**: Complex multi-band imagery
- **Recommendation**: Use 0.1 for sensitive detection

#### 4. Vegetation Analysis
- **Use Case**: Environmental monitoring
- **Parameter**: None (NDVI-based)
- **Best For**: Vegetation health, deforestation
- **Recommendation**: Requires NIR band

## 🏗️ Project Structure

```
Satelite_Image_detection/
├── app.py                          # Streamlit BI Dashboard
├── change_detector.py              # Core change detection algorithms
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── snapshot-2025-10-01T00_00_00Z.tif  # Earlier satellite image
└── snapshot-2025-10-06T00_00_00Z.tif  # Later satellite image
```

## 🔬 Technical Details

### Algorithms Implemented

1. **Image Normalization**
   - Band-wise normalization to 0-1 range
   - Handles multi-spectral data

2. **Difference Calculation**
   - Absolute difference
   - Ratio-based
   - Log-ratio

3. **Change Detection**
   - Thresholding
   - Otsu's method
   - Change vector magnitude
   - Morphological filtering

4. **Vegetation Indices**
   - NDVI calculation
   - Temporal NDVI comparison
   - Vegetation gain/loss classification

5. **Post-processing**
   - Morphological opening/closing
   - Noise reduction
   - Connected component analysis

### Supported Image Formats
- GeoTIFF (.tif)
- Multi-band satellite imagery
- NASA satellite data
- Supports various coordinate reference systems

## 📈 Example Use Cases

1. **Deforestation Monitoring**
   - Use vegetation analysis mode
   - Track NDVI changes over time
   - Identify areas of vegetation loss

2. **Urban Development**
   - Use threshold-based or CVD detection
   - Monitor construction and land use changes
   - Track urban sprawl

3. **Disaster Assessment**
   - Use threshold detection with low values
   - Identify affected areas
   - Compare pre/post disaster imagery

4. **Agriculture**
   - Use vegetation analysis
   - Monitor crop health
   - Identify irrigation issues

## 🎯 Interpretation Guide

### Change Percentage
- **< 5%**: Minimal changes, likely noise or seasonal variations
- **5-15%**: Moderate changes, worth investigating
- **15-30%**: Significant changes, major events
- **> 30%**: Extensive changes, dramatic transformation

### NDVI Values
- **< 0**: Water, snow, clouds
- **0 - 0.2**: Barren, urban areas
- **0.2 - 0.5**: Sparse vegetation, grassland
- **0.5 - 0.8**: Dense vegetation, healthy crops
- **> 0.8**: Very dense vegetation

## 🛠️ Customization

### Adding New Detection Methods

Edit `change_detector.py`:

```python
def detect_changes_custom(self, param1, param2):
    """
    Your custom detection method
    """
    # Your implementation
    return change_map
```

### Modifying Visualization

Edit `app.py` to customize:
- Color schemes
- Layout
- Additional metrics
- Export formats

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are installed
   - Activate virtual environment

2. **Memory Issues**
   - Large images may require significant RAM
   - Consider downsampling for initial analysis

3. **No Changes Detected**
   - Try lowering the threshold
   - Use Otsu method for automatic threshold
   - Verify images are from different time periods

4. **GDAL/Rasterio Issues**
   - On Windows: Install OSGeo4W or use conda
   - On Linux: Install GDAL system packages first

## 📚 References

- **Change Detection**: Singh, A. (1989). Digital change detection techniques
- **NDVI**: Rouse et al. (1974). Monitoring vegetation systems
- **Otsu's Method**: Otsu, N. (1979). A threshold selection method

## 🤝 Contributing

This is a technical assessment project. For improvements:
1. Document your changes
2. Test with various image types
3. Update requirements.txt if adding dependencies

## 📄 License

This project is created as a technical assessment.

## 👨‍💻 Author

Created for NASA Satellite Image Analysis Technical Assessment

## 🙏 Acknowledgments

- NASA for satellite imagery
- Open source GIS community
- Streamlit for the dashboard framework
- Rasterio and GDAL projects

---

**Note**: This system is designed for educational and assessment purposes. For production use, consider:
- Cloud deployment (AWS, Azure, GCP)
- Database integration
- User authentication
- API development
- Automated processing pipelines
- Model training for ML-based detection
