# 🚀 QUICK START GUIDE

## Getting Started in 3 Easy Steps

### Step 1: Setup Environment

**Windows:**
```bash
setup.bat
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

This will:
- ✅ Create a virtual environment
- ✅ Install all required packages
- ✅ Verify Python installation

---

### Step 2: Run the Application

**Windows:**
```bash
run_app.bat
```

**Linux/Mac:**
```bash
chmod +x run_app.sh
./run_app.sh
```

Or manually:
```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Run the app
streamlit run app.py
```

The dashboard will automatically open at: **http://localhost:8501**

---

### Step 3: Upload and Analyze

1. **Upload Images**
   - Click sidebar → "Upload Files"
   - Select 2+ satellite images (.tif/.tiff)
   - Or use "Use Existing Files" for images in project folder

2. **Configure Analysis**
   - Select "Earlier Image" and "Later Image"
   - Choose detection method
   - Adjust parameters if needed

3. **Run Analysis**
   - Click "🚀 Run Analysis"
   - View results in 3 tabs:
     - **Analysis**: Visualizations
     - **Gallery**: Image previews
     - **Statistics**: Detailed metrics

4. **Export Results**
   - Download change maps (CSV)
   - Export statistics
   - Save visualizations

---

## 📦 What's Included

```
Satelite_Image_detection/
├── app.py                          # Main Streamlit dashboard ⭐
├── change_detector.py              # Core detection algorithms
├── example_usage.py                # Python script example
├── quick_start.py                  # System verification
├── requirements.txt                # Python dependencies
├── README.md                       # Full documentation
├── UI_GUIDE.md                     # Detailed UI guide
├── INSTALL.md                      # Installation help
├── setup.bat / setup.sh            # Setup scripts
├── run_app.bat / run_app.sh        # Launch scripts
└── snapshot-*.tif                  # Sample satellite images
```

---

## 💡 Key Features

### 🎯 Real-Time Upload
- Upload multiple images via drag & drop
- Add images dynamically without restart
- Remove unwanted images on-the-fly

### 🔬 4 Detection Methods
1. **Threshold-based** - Manual sensitivity control
2. **Otsu Auto-threshold** - Automatic optimal detection
3. **Change Vector Detection** - Multi-band analysis
4. **Vegetation Analysis** - NDVI-based monitoring

### 📊 Professional UI
- Three-tab interface (Analysis/Gallery/Statistics)
- Real-time thumbnails and previews
- Interactive Plotly charts
- Export capabilities (CSV)

### 🌍 GIS Features
- Automatic metadata extraction
- CRS and bounds detection
- Multi-band image support
- GeoTIFF compatibility

---

## 🎨 UI Overview

### Sidebar
```
📁 Image Management
  ├── Upload Files / Use Existing
  ├── File uploader
  └── Loaded images counter

⚙️ Analysis Parameters
  ├── Image selection (Earlier/Later)
  ├── Detection method
  ├── Threshold sliders
  └── Visualization options

🚀 Actions
  ├── Run Analysis
  └── Clear All Images
```

### Main Tabs
```
📊 Analysis
  ├── KPI metrics (4 cards)
  ├── Image comparison (side-by-side)
  ├── Change overlay (red highlights)
  ├── Binary change map
  ├── Intensity heatmap
  └── Export buttons

🖼️ Gallery
  ├── All loaded images (grid view)
  ├── Thumbnails with metadata
  └── Remove buttons

📈 Statistics
  ├── Detailed metrics table
  ├── Interactive pie/bar charts
  └── Image metadata comparison
```

---

## 📝 Usage Examples

### Example 1: Quick 2-Image Analysis
```
1. Run: run_app.bat
2. Upload: 2 satellite images
3. Select: Image #1 (earlier) vs #2 (later)
4. Method: "Otsu Auto-threshold"
5. Click: "Run Analysis"
6. View: Results in all tabs
7. Export: Download CSV files
```

### Example 2: Multiple Comparisons
```
1. Upload: 5 images from different dates
2. Gallery: View all thumbnails
3. Compare: Image 1 vs 5 (full period)
4. Analyze: Run detection
5. Compare: Image 2 vs 3 (sub-period)
6. Compare: Different methods on same pair
```

### Example 3: Vegetation Monitoring
```
1. Upload: Quarterly images (4 per year)
2. Select: Q1 vs Q4
3. Method: "Vegetation Analysis"
4. View: NDVI changes
5. Metrics: Vegetation loss/gain
6. Export: Results for reporting
```

---

## 🔧 Troubleshooting

### Common Issues

**1. "streamlit: command not found"**
```bash
# Solution: Run setup script
setup.bat  # Windows
./setup.sh # Linux/Mac
```

**2. "rasterio installation failed"**
```bash
# Solution: Use conda
conda install -c conda-forge rasterio
```

**3. "No images loaded"**
```
Solution: Use sidebar Upload button or Add existing files
```

**4. "Analysis button disabled"**
```
Solution: Need at least 2 images loaded
```

**5. "Memory error"**
```
Solution: Clear some images, reduce file sizes, or restart app
```

---

## 🎯 Tips for Best Results

### Image Tips
✅ Use GeoTIFF format (.tif, .tiff)
✅ Same geographic area and CRS
✅ Similar resolution and bands
✅ Clear temporal separation

### Analysis Tips
✅ Start with Otsu method (automatic)
✅ Adjust threshold if too sensitive/insensitive
✅ Use Vegetation method for environmental changes
✅ Check Gallery tab to verify images loaded correctly

### Performance Tips
✅ Upload 2-10 images for flexibility
✅ Remove unused images periodically
✅ Close other browser tabs for large images
✅ Use thumbnails in Gallery for quick preview

---

## 📊 Understanding Results

### KPI Metrics
- **Total Area**: Total pixels analyzed
- **Changed Area**: Number and % of changed pixels
- **Change Regions**: Number of separate change zones
- **Avg Region Size**: Average size of change areas

### Change Percentage Guide
- **< 5%**: Minimal changes (noise/seasonal)
- **5-15%**: Moderate changes (worth investigating)
- **15-30%**: Significant changes (major events)
- **> 30%**: Extensive transformation

### NDVI Values (Vegetation)
- **< 0**: Water, snow, clouds
- **0-0.2**: Barren, urban areas
- **0.2-0.5**: Sparse vegetation
- **0.5-0.8**: Dense vegetation
- **> 0.8**: Very dense vegetation

---

## 🎓 Real-World Applications

### 1. Deforestation Monitoring
- Upload: Yearly forest images
- Method: Vegetation Analysis
- Track: NDVI decline
- Export: Loss maps for reports

### 2. Urban Development
- Upload: Annual city images
- Method: Change Vector Detection
- Track: Construction and expansion
- Export: Development statistics

### 3. Disaster Assessment
- Upload: Pre/post disaster images
- Method: Threshold-based (0.2-0.3)
- Track: Damaged areas
- Export: Damage assessment maps

### 4. Agriculture Monitoring
- Upload: Seasonal crop images
- Method: Vegetation Analysis
- Track: Crop health (NDVI)
- Export: Field-by-field analysis

---

## 📞 Support

### Check Installation
```bash
python quick_start.py
```

### View Documentation
- `README.md` - Complete system guide
- `UI_GUIDE.md` - Detailed UI documentation
- `INSTALL.md` - Installation troubleshooting

### Manual Installation
```bash
pip install -r requirements.txt
```

---

## 🎉 You're Ready!

1. ✅ Run setup script
2. ✅ Launch app
3. ✅ Upload images
4. ✅ Analyze changes
5. ✅ Export results

**Launch Command:**
```bash
run_app.bat    # Windows
./run_app.sh   # Linux/Mac
```

**Dashboard URL:**
```
http://localhost:8501
```

---

## 📌 Quick Reference Card

| Action | Command |
|--------|---------|
| Setup | `setup.bat` or `./setup.sh` |
| Run | `run_app.bat` or `./run_app.sh` |
| Test | `python quick_start.py` |
| URL | http://localhost:8501 |
| Upload | Sidebar → Upload Files |
| Analyze | Select 2 images → Run Analysis |
| Export | Analysis tab → Download buttons |
| Clear | Sidebar → Clear All Images |

---

**Perfect for your technical assessment! Ready to impress! 🛰️✨**
