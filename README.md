# 🛰️ Satellite Image Change Detection System

A comprehensive Business Intelligence solution for analyzing temporal changes in satellite imagery. This system provides advanced change detection algorithms and an interactive dashboard for environmental monitoring, urban planning, and natural pattern analysis.

## 📋 Overview

This system analyzes GIS satellite image data to detect and visualize changes between two time periods. It's designed for:
- **Environmental monitoring** (deforestation, urban growth)
- **Disaster assessment** (flood damage, earthquake impact)
- **Agricultural analysis** (crop health, vegetation changes)
- **Urban planning** (construction monitoring, land use changes)

## ✨ Key Features

### 🔍 Change Detection Algorithms
- **Threshold-based Detection**: Simple pixel difference with configurable sensitivity
- **Otsu Auto-thresholding**: Automatic optimal threshold calculation
- **Change Vector Detection (CVD)**: Multi-spectral magnitude analysis
- **Vegetation Analysis (NDVI)**: Vegetation health monitoring

### 📊 Business Intelligence Dashboard
- Interactive web interface with real-time analysis
- Side-by-side temporal image comparison
- Change intensity heatmaps and statistics
- KPI metrics and export capabilities
- Professional visualizations with Plotly

### 🎯 Pattern Detection
- **Anthropological patterns**: Urban expansion, construction, infrastructure changes
- **Natural patterns**: Vegetation loss/gain, water body changes, seasonal variations
- **Statistical analysis**: Change percentages, affected areas, region counting

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

### 3. Analyze Satellite Images
1. **Upload Images**: Use the sidebar to upload 2+ satellite images (.tif/.tiff format)
2. **Select Comparison**: Choose "Earlier Image" and "Later Image" 
3. **Configure Method**: Select detection algorithm and adjust parameters
4. **Run Analysis**: Click "🚀 Run Analysis" button
5. **View Results**: Explore results in Analysis, Gallery, and Statistics tabs
6. **Export Data**: Download change maps and statistics as CSV files

## 📁 Project Structure

```
Satelite_Image_detection/
├── app.py                          # Main Streamlit dashboard
├── change_detector.py              # Core change detection algorithms
├── example_usage.py                # Python script usage example
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── snapshot-*.tif                  # Sample satellite images
└── sample_images/                  # Additional sample data
```

## 🛠️ System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **OS**: Windows 10/11, Linux, macOS
- **Disk Space**: 500MB for dependencies

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `rasterio` | Reading GeoTIFF satellite images |
| `numpy` | Numerical computations |
| `matplotlib` | Static visualizations |
| `streamlit` | Interactive web dashboard |
| `plotly` | Interactive charts and maps |
| `scikit-image` | Image processing algorithms |
| `opencv-python` | Computer vision operations |
| `pandas` | Data analysis and statistics |
| `scipy` | Scientific computing |
| `Pillow` | Image handling |

## 💻 Usage Examples

### Example 1: Dashboard Usage
1. Launch: `streamlit run app.py`
2. Upload 2 satellite images via sidebar
3. Select images and detection method
4. Click "Run Analysis"
5. View results and export data

### Example 2: Python Script Usage
```python
from change_detector import ChangeDetector

# Initialize detector
detector = ChangeDetector(
    'snapshot-2025-10-01T00_00_00Z.tif',
    'snapshot-2025-10-06T00_00_00Z.tif'
)

# Load and analyze images
detector.load_images()
change_map = detector.detect_changes_threshold(threshold=0.15)
stats = detector.analyze_change_statistics(change_map)

print(f"Changed pixels: {stats['changed_pixels']:,}")
print(f"Change percentage: {stats['change_percentage']:.2f}%")
```
## 🎨 Dashboard Interface

### Sidebar Controls
- **Image Management**: Upload files or use existing samples
- **Analysis Parameters**: Select images, methods, and thresholds
- **Actions**: Run analysis and clear images

### Main Tabs
- **📊 Analysis**: Visual results, change maps, and comparisons
- **🖼️ Gallery**: Thumbnail view of all loaded images
- **📈 Statistics**: Detailed metrics, charts, and export options

## 🔧 Troubleshooting

### Common Issues

**"streamlit: command not found"**
```bash
pip install streamlit
```

**"rasterio installation failed"**
```bash
# Use conda for easier GDAL installation
conda install -c conda-forge rasterio
```

**"No images loaded"**
- Use sidebar upload button or existing file options
- Ensure files are .tif or .tiff format

**"Analysis button disabled"**
- Need at least 2 images loaded
- Select different images for comparison

## 🎯 Business Intelligence Features

### Real-time KPIs
- Change detection percentage
- Total affected area (pixels/hectares)
- Number of change regions
- Vegetation health indices

### Interactive Visualizations
- Before/after image comparisons
- Change intensity heatmaps
- Statistical trend charts
- Geographic overlay maps

### Export Capabilities
- CSV files with change coordinates
- Statistical summary reports
- High-resolution visualization images
- Timestamped file naming

## 🌍 Supported Data Formats

- **GeoTIFF** (.tif, .tiff) - Primary format
- **Multi-band satellite imagery** (Landsat, Sentinel, etc.)
- **Single or multi-temporal datasets**
- **Various spatial resolutions** (10m, 20m, 30m pixels)

## 📈 Performance Tips

- **Memory**: Larger images require more RAM
- **Processing**: Multi-band images take longer to process
- **Visualization**: Complex overlays may slow rendering
- **Export**: Large datasets create bigger CSV files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## � License

This project is open source and available under the MIT License.

---

**Perfect for analyzing satellite GIS data and providing Business Intelligence solutions with interactive interfaces! 🛰️✨**
