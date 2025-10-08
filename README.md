# 🛰️ Satellite Image Change Detection System# 🛰️ Satellite Image Change Detection System



A Business Intelligence solution for analyzing temporal changes in satellite imagery using computer vision and AI-powered natural language insights.A comprehensive Business Intelligence solution for analyzing temporal changes in satellite imagery. This system provides advanced change detection algorithms and an interactive dashboard for environmental monitoring, urban planning, and natural pattern analysis.



## 🎯 Project Overview## 📋 Overview



This system analyzes satellite images to detect and visualize changes between two time periods, making it useful for:This system analyzes GIS satellite image data to detect and visualize changes between two time periods. It's designed for:

- **Environmental monitoring** (deforestation, urban growth)- **Environmental monitoring** (deforestation, urban growth)

- **Disaster assessment** (flood damage, infrastructure impact)- **Disaster assessment** (flood damage, earthquake impact)

- **Urban planning** (construction monitoring, land development)- **Agricultural analysis** (crop health, vegetation changes)

- **Agricultural analysis** (crop health, vegetation changes)- **Urban planning** (construction monitoring, land use changes)



## ✨ Key Features## ✨ Key Features



### 1. Change Detection Algorithms### 🔍 Change Detection Algorithms

- **Threshold-based Detection**: Configurable pixel difference analysis- **Threshold-based Detection**: Simple pixel difference with configurable sensitivity

- **Otsu Auto-thresholding**: Automatic optimal threshold selection- **Otsu Auto-thresholding**: Automatic optimal threshold calculation

- **Change Vector Detection (CVD)**: Multi-spectral analysis- **Change Vector Detection (CVD)**: Multi-spectral magnitude analysis

- **Vegetation Analysis (NDVI)**: Vegetation health monitoring- **Vegetation Analysis (NDVI)**: Vegetation health monitoring



### 2. Interactive Dashboard### 📊 Business Intelligence Dashboard

- Real-time image upload and comparison- Interactive web interface with real-time analysis

- Side-by-side temporal visualization- Side-by-side temporal image comparison

- Change intensity heatmaps- Change intensity heatmaps and statistics

- KPI metrics and statistics- KPI metrics and export capabilities

- Export capabilities (CSV)- Professional visualizations with Plotly

- **🤖 AI-Powered Summaries**: Natural language insights using Google Gemini API

### 3. AI-Powered Insights

- Natural language summaries using Google Gemini API### 🎯 Pattern Detection

- Converts technical metrics into plain English- **Anthropological patterns**: Urban expansion, construction, infrastructure changes

- Helps non-technical users understand results- **Natural patterns**: Vegetation loss/gain, water body changes, seasonal variations

- **Statistical analysis**: Change percentages, affected areas, region counting

## 🚀 Quick Start

## 🚀 Quick Start

### 1. Install Dependencies

```bash### 1. Setup Environment

# Create virtual environment```bash

python -m venv .venv# Create virtual environment

source .venv/bin/activate  # On Windows: .venv\Scripts\activatepython -m venv .venv



# Install packages# Activate environment

pip install -r requirements.txt# Windows:

```.venv\Scripts\activate

# Linux/Mac:

### 2. Configure API Key (Optional)source .venv/bin/activate

For AI-powered summaries:

1. Get free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)# Install dependencies

2. Copy `.env.example` to `.env`pip install -r requirements.txt

3. Add your key: `GEMINI_API_KEY=your_key_here````



### 3. Run Application### 2. Run the Application

```bash```bash

streamlit run app.pystreamlit run app.py

``````



Open browser at `http://localhost:8501`The dashboard will open in your browser at `http://localhost:8501`



## 📁 Project Structure### 3. Analyze Satellite Images

1. **Upload Images**: Use the sidebar to upload 2+ satellite images (.tif/.tiff format)

```2. **(Optional) Enable AI Summary**: Add your [Google AI Studio API key](https://makersuite.google.com/app/apikey) and enable AI summaries

Satelite_Image_detection/3. **Select Comparison**: Choose "Earlier Image" and "Later Image" 

├── app.py                    # Streamlit dashboard (main UI)4. **Configure Method**: Select detection algorithm and adjust parameters

├── change_detector.py        # Core detection algorithms5. **Run Analysis**: Click "🚀 Run Analysis" button

├── ai_summarizer.py          # AI summary generation6. **View Results**: Explore results in Analysis, Gallery, and Statistics tabs

├── example_usage.py          # Python script usage example7. **Export Data**: Download change maps and statistics as CSV files

├── requirements.txt          # Python dependencies

├── .env.example             # API key template### 4. Get AI-Powered Insights (Optional)

├── README.md                # This file

└── sample_images/           # Sample satellite data**Method 1: Using .env file (Recommended)**

```1. Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

2. Copy `.env.example` to `.env`

## 💻 Usage3. Add your key: `GEMINI_API_KEY=your_key_here`

4. Restart the app - AI summary will auto-enable!

### Via Dashboard (Recommended)

1. Run `streamlit run app.py`**Method 2: Manual entry**

2. Upload 2+ satellite images (.tif format)1. Get your API key

3. Select "Earlier" and "Later" images2. Enter it in the sidebar

4. Choose detection method3. Check "Enable AI Summary"

5. Click "Run Analysis"

6. View results and export dataSee [API_KEY_SETUP.md](API_KEY_SETUP.md) for detailed instructions.



### Via Python Script## 📁 Project Structure

```python

from change_detector import ChangeDetector```

Satelite_Image_detection/

# Initialize detector├── app.py                          # Main Streamlit dashboard

detector = ChangeDetector('image_before.tif', 'image_after.tif')├── change_detector.py              # Core change detection algorithms

detector.load_images()├── ai_summarizer.py                # AI-powered natural language summary

├── example_usage.py                # Python script usage example

# Run detection├── requirements.txt                # Python dependencies

change_map = detector.detect_changes_threshold(threshold=0.15)├── .env.example                    # Environment variables template

stats = detector.analyze_change_statistics(change_map)├── .env                            # Your API keys (create from .env.example)

├── README.md                       # This file

print(f"Changed area: {stats['change_percentage']:.2f}%")├── API_KEY_SETUP.md                # Detailed API key setup guide

```└── sample_images/                  # Sample satellite data

```

## 🛠️ Technologies Used

## 🛠️ System Requirements

| Technology | Purpose |

|------------|---------|- **Python**: 3.8 or higher

| **Python 3.8+** | Core programming language |- **RAM**: 4GB minimum, 8GB recommended

| **Streamlit** | Web dashboard framework |- **OS**: Windows 10/11, Linux, macOS

| **Rasterio** | GeoTIFF satellite image processing |- **Disk Space**: 500MB for dependencies

| **NumPy** | Numerical computations |

| **OpenCV** | Computer vision operations |## 📦 Dependencies

| **Scikit-image** | Image processing algorithms |

| **Matplotlib/Plotly** | Data visualization || Package | Purpose |

| **Google Gemini API** | AI-powered summaries ||---------|---------|

| `rasterio` | Reading GeoTIFF satellite images |

## 📊 Algorithm Details| `numpy` | Numerical computations |

| `matplotlib` | Static visualizations |

### Change Detection Methods| `streamlit` | Interactive web dashboard |

| `plotly` | Interactive charts and maps |

1. **Threshold-based**: Simple pixel difference| `scikit-image` | Image processing algorithms |

   ```python| `opencv-python` | Computer vision operations |

   change = abs(image2 - image1) > threshold| `pandas` | Data analysis and statistics |

   ```| `scipy` | Scientific computing |

| `Pillow` | Image handling |

2. **Otsu**: Automatic threshold calculation using histogram analysis| `google-generativeai` | AI-powered natural language summaries (optional) |



3. **CVD**: Magnitude-based multi-spectral change## 💻 Usage Examples

   ```python

   magnitude = sqrt(sum((band2 - band1)²))### Example 1: Dashboard Usage

   ```1. Launch: `streamlit run app.py`

2. Upload 2 satellite images via sidebar

4. **NDVI**: Vegetation index comparison3. Select images and detection method

   ```python4. Click "Run Analysis"

   NDVI = (NIR - Red) / (NIR + Red)5. View results and export data

   ```

### Example 2: Python Script Usage

## 🎨 Dashboard Features```python

from change_detector import ChangeDetector

- **📊 Analysis Tab**: Visual results and change maps

- **🖼️ Gallery Tab**: All loaded images with thumbnails# Initialize detector

- **📈 Statistics Tab**: Detailed metrics and chartsdetector = ChangeDetector(

- **🤖 AI Summary**: Natural language insights    'snapshot-2025-10-01T00_00_00Z.tif',

    'snapshot-2025-10-06T00_00_00Z.tif'

## 🔒 Security)



- API keys stored in `.env` file (git-ignored)# Load and analyze images

- No hardcoded credentialsdetector.load_images()

- Secure environment variable managementchange_map = detector.detect_changes_threshold(threshold=0.15)

stats = detector.analyze_change_statistics(change_map)

## 📝 Sample Output

print(f"Changed pixels: {stats['changed_pixels']:,}")

**Technical Metrics:**print(f"Change percentage: {stats['change_percentage']:.2f}%")

- Changed pixels: 4,523 (6.07%)```

- Number of regions: 89## 🎨 Dashboard Interface

- Average region size: 51 pixels

### Sidebar Controls

**AI Summary:**- **Image Management**: Upload files or use existing samples

> "Moderate changes affecting 6% of the area. The 89 scattered regions suggest localized modifications rather than large-scale development."- **Analysis Parameters**: Select images, methods, and thresholds

- **Actions**: Run analysis and clear images

## 🎯 Use Cases

### Main Tabs

1. **Urban Development**: Track city expansion- **📊 Analysis**: Visual results, change maps, and comparisons

2. **Environmental Monitoring**: Detect deforestation- **🖼️ Gallery**: Thumbnail view of all loaded images

3. **Disaster Assessment**: Measure damage extent- **📈 Statistics**: Detailed metrics, charts, and export options

4. **Agricultural Analysis**: Monitor crop health

## 🔧 Troubleshooting

## 📦 Requirements

### Common Issues

- Python 3.8+

- 4GB RAM minimum**"streamlit: command not found"**

- Modern web browser```bash

pip install streamlit

---```



**Developed by:** Birendra K Sharma  **"rasterio installation failed"**

**Purpose:** Satellite GIS Data Analysis & Business Intelligence Solution  ```bash

**Tech Stack:** Python | Streamlit | Computer Vision | AI/ML# Use conda for easier GDAL installation

conda install -c conda-forge rasterio

🛰️ **Turning satellite data into actionable insights!** ✨```


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
