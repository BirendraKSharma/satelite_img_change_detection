import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
import rasterio
from change_detector import ChangeDetector
from ai_summarizer import generate_summary, get_quick_insight
from datetime import datetime
import tempfile
from typing import Dict
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Satellite Change Detection BI Dashboard",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploaded_images' not in st.session_state:
    st.session_state.uploaded_images = []
if 'image_metadata' not in st.session_state:
    st.session_state.image_metadata = []
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None
if 'temp_files' not in st.session_state:
    st.session_state.temp_files = []

# Helper functions
def save_uploaded_file(uploaded_file) -> str:
    """Save uploaded file to temporary location and return path"""
    temp_dir = tempfile.mkdtemp()
    temp_path = Path(temp_dir) / uploaded_file.name
    
    with open(temp_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    st.session_state.temp_files.append(str(temp_path))
    return str(temp_path)

def get_image_info(file_path: str) -> Dict:
    """Extract metadata from satellite image"""
    try:
        with rasterio.open(file_path) as src:
            return {
                'name': Path(file_path).name,
                'path': file_path,
                'width': src.width,
                'height': src.height,
                'bands': src.count,
                'crs': str(src.crs),
                'dtype': str(src.dtypes[0]),
                'bounds': src.bounds,
                'transform': src.transform,
                'nodata': src.nodata
            }
    except Exception as e:
        return {
            'name': Path(file_path).name,
            'path': file_path,
            'error': str(e)
        }

def create_thumbnail(file_path: str, max_size: int = 200) -> np.ndarray:
    """Create thumbnail for image preview"""
    try:
        with rasterio.open(file_path) as src:
            # Read the image at lower resolution
            out_shape = (
                src.count,
                max_size,
                max_size
            )
            
            data = src.read(
                out_shape=out_shape,
                resampling=rasterio.enums.Resampling.average
            )
            
            # Normalize to 0-1
            normalized = np.zeros_like(data, dtype=np.float32)
            for i in range(data.shape[0]):
                band = data[i].astype(np.float32)
                band_min, band_max = band.min(), band.max()
                if band_max > band_min:
                    normalized[i] = (band - band_min) / (band_max - band_min)
                else:
                    normalized[i] = band
            
            # Create RGB composite
            if normalized.shape[0] >= 3:
                rgb = np.stack([normalized[0], normalized[1], normalized[2]], axis=2)
            else:
                gray = normalized[0]
                rgb = np.stack([gray, gray, gray], axis=2)
            
            return np.clip(rgb, 0, 1)
    except Exception as e:
        st.error(f"Error creating thumbnail: {e}")
        return np.zeros((max_size, max_size, 3))

def remove_image(index: int):
    """Remove image from session state"""
    if 0 <= index < len(st.session_state.uploaded_images):
        st.session_state.uploaded_images.pop(index)
        st.session_state.image_metadata.pop(index)

# Title
st.markdown('<div class="main-header">🛰️ Satellite Image Change Detection System</div>', 
            unsafe_allow_html=True)
st.markdown("### Real-Time Business Intelligence Dashboard for Environmental Monitoring")

# Sidebar
st.sidebar.title("🔧 Configuration")
st.sidebar.markdown("---")

# AI Summary Configuration
st.sidebar.subheader("🤖 AI Summary")

# Try to load API key from .env file first
default_api_key = os.getenv('GEMINI_API_KEY', '')

gemini_api_key = st.sidebar.text_input(
    "Google AI API Key",
    value=default_api_key,
    type="password",
    help="Get your free API key from https://makersuite.google.com/app/apikey or set GEMINI_API_KEY in .env file",
    placeholder="Enter your Gemini API key or add to .env..."
)

if default_api_key:
    st.sidebar.caption("✅ API key loaded from .env file")

enable_ai_summary = st.sidebar.checkbox(
    "Enable AI Summary",
    value=bool(default_api_key),  # Auto-enable if key exists in .env
    help="Generate natural language summary of results"
)
st.sidebar.markdown("---")

# Image Management Section
st.sidebar.subheader("📁 Image Management")

upload_mode = st.sidebar.radio(
    "Image Source",
    ["Upload Files", "Use Existing Files"],
    help="Choose to upload new images or use images from the directory"
)

if upload_mode == "Upload Files":
    st.sidebar.markdown("##### 📤 Upload Satellite Images")
    uploaded_files = st.sidebar.file_uploader(
        "Choose TIF/TIFF files",
        type=['tif', 'tiff'],
        accept_multiple_files=True,
        help="Upload multiple satellite images for comparison"
    )
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Check if already uploaded
            if not any(img['name'] == uploaded_file.name for img in st.session_state.image_metadata):
                with st.spinner(f"Processing {uploaded_file.name}..."):
                    file_path = save_uploaded_file(uploaded_file)
                    metadata = get_image_info(file_path)
                    
                    st.session_state.uploaded_images.append(file_path)
                    st.session_state.image_metadata.append(metadata)
                    st.sidebar.success(f"✅ Loaded: {uploaded_file.name}")

else:  # Use existing files
    current_dir = Path(__file__).parent
    
    # Search in both current directory and sample_images subdirectory
    tif_files = []
    tif_files.extend(current_dir.glob("*.tif"))
    tif_files.extend(current_dir.glob("*.tiff"))
    
    # Also check sample_images directory
    sample_dir = current_dir / "sample_images"
    if sample_dir.exists():
        tif_files.extend(sample_dir.glob("*.tif"))
        tif_files.extend(sample_dir.glob("*.tiff"))
    
    tif_files = sorted(tif_files)
    
    if tif_files:
        st.sidebar.markdown("##### 📂 Available Files")
        
        # Group files by location for better organization
        root_files = [f for f in tif_files if f.parent == current_dir]
        sample_files = [f for f in tif_files if f.parent != current_dir]
        
        # Display files from sample_images first (professional dataset)
        if sample_files:
            st.sidebar.markdown("**🌍 Professional Dataset (Onera):**")
            for tif_file in sample_files:
                if st.sidebar.button(f"➕ {tif_file.name}", key=f"add_{tif_file.name}"):
                    if not any(img['name'] == tif_file.name for img in st.session_state.image_metadata):
                        file_path = str(tif_file)
                        metadata = get_image_info(file_path)
                        
                        st.session_state.uploaded_images.append(file_path)
                        st.session_state.image_metadata.append(metadata)
                        st.sidebar.success(f"✅ Added: {tif_file.name}")
                    else:
                        st.sidebar.warning(f"Already added: {tif_file.name}")
        
        # Display files from root directory
        if root_files:
            if sample_files:  # Add separator if we showed sample files
                st.sidebar.markdown("**📁 Root Directory:**")
            for tif_file in root_files:
                if st.sidebar.button(f"➕ {tif_file.name}", key=f"add_{tif_file.name}"):
                    if not any(img['name'] == tif_file.name for img in st.session_state.image_metadata):
                        file_path = str(tif_file)
                        metadata = get_image_info(file_path)
                        
                        st.session_state.uploaded_images.append(file_path)
                        st.session_state.image_metadata.append(metadata)
                        st.sidebar.success(f"✅ Added: {tif_file.name}")
                    else:
                        st.sidebar.warning(f"Already added: {tif_file.name}")
    else:
        st.sidebar.warning("No TIF files found in directory")

# Display loaded images count
st.sidebar.markdown("---")
st.sidebar.metric("Loaded Images", len(st.session_state.uploaded_images))

# Detection parameters (only show if we have at least 2 images)
if len(st.session_state.uploaded_images) >= 2:
    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ Analysis Parameters")
    
    # Image selection for comparison
    image_names = [meta['name'] for meta in st.session_state.image_metadata]
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        image1_idx = st.selectbox(
            "Earlier Image",
            range(len(image_names)),
            format_func=lambda x: f"#{x+1}: {image_names[x]}"
        )
    
    with col2:
        image2_idx = st.selectbox(
            "Later Image",
            range(len(image_names)),
            index=min(1, len(image_names)-1),
            format_func=lambda x: f"#{x+1}: {image_names[x]}"
        )
    
    detection_method = st.sidebar.selectbox(
        "Detection Method",
        ["Threshold-based", "Otsu Auto-threshold", "Change Vector Detection", "Vegetation Analysis"],
        help="Choose the algorithm for change detection"
    )
    
    if detection_method == "Threshold-based":
        threshold = st.sidebar.slider(
            "Change Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.15,
            step=0.05,
            help="Lower values detect more changes"
        )
    elif detection_method == "Change Vector Detection":
        threshold = st.sidebar.slider(
            "CVD Threshold",
            min_value=0.0,
            max_value=0.5,
            value=0.1,
            step=0.02,
            help="Magnitude threshold for change detection"
        )
    else:
        threshold = None
    
    # Visualization options
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎨 Visualization Options")
    
    show_overlay = st.sidebar.checkbox("Show Change Overlay", value=True)
    show_heatmap = st.sidebar.checkbox("Show Intensity Heatmap", value=True)
    
    # Analysis button
    st.sidebar.markdown("---")
    analyze_button = st.sidebar.button("🚀 Run Analysis", type="primary", width='stretch')
    
    if st.sidebar.button("🗑️ Clear All Images", width='stretch'):
        st.session_state.uploaded_images = []
        st.session_state.image_metadata = []
        st.session_state.analysis_results = None
        st.rerun()

# Main content area
tab1, tab2, tab3 = st.tabs(["📊 Analysis", "🖼️ Image Gallery", "📈 Statistics"])

# Tab 1: Analysis
with tab1:
    if len(st.session_state.uploaded_images) == 0:
        st.markdown("### 👈 Get Started")
        st.markdown("""
        **Step 1:** Upload satellite images using the sidebar or use existing files  
        **Step 2:** Select at least 2 images for comparison  
        **Step 3:** Configure analysis parameters  
        **Step 4:** Click 'Run Analysis'
        
        #### 📌 Supported Formats
        - GeoTIFF (.tif, .tiff)
        - Multi-band satellite imagery
        - NASA satellite data
        """)
    
    elif len(st.session_state.uploaded_images) < 2:
        st.warning("⚠️ Please add at least 2 images to perform change detection analysis.")
        
        # Show uploaded image
        st.markdown("### 📸 Currently Loaded Image")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            thumbnail = create_thumbnail(st.session_state.uploaded_images[0])
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(thumbnail)
            ax.axis('off')
            ax.set_title(st.session_state.image_metadata[0]['name'])
            st.pyplot(fig)
            plt.close()
        
        with col2:
            st.markdown("#### Image Metadata")
            metadata = st.session_state.image_metadata[0]
            st.json(metadata)
    
    else:
        # We have enough images for analysis
        if analyze_button or (st.session_state.analysis_results and image1_idx == st.session_state.analysis_results.get('image1_idx') and image2_idx == st.session_state.analysis_results.get('image2_idx')):
            with st.spinner("🔄 Processing satellite images..."):
                try:
                    # Create detector
                    detector = ChangeDetector(
                        st.session_state.uploaded_images[image1_idx],
                        st.session_state.uploaded_images[image2_idx]
                    )
                    detector.load_images()
                    
                    # Run analysis
                    if detection_method == "Threshold-based":
                        change_map = detector.detect_changes_threshold(threshold)
                        veg_results = None
                    elif detection_method == "Otsu Auto-threshold":
                        change_map = detector.detect_changes_otsu()
                        veg_results = None
                    elif detection_method == "Change Vector Detection":
                        change_map = detector.detect_changes_cvd(threshold)
                        veg_results = None
                    else:  # Vegetation Analysis
                        veg_results = detector.detect_vegetation_change()
                        if veg_results:
                            change_map = veg_results.get('vegetation_loss', np.zeros((100, 100)))
                        else:
                            change_map = np.zeros((100, 100))
                    
                    stats = detector.analyze_change_statistics(change_map)
                    
                    # Store results
                    st.session_state.analysis_results = {
                        'detector': detector,
                        'change_map': change_map,
                        'stats': stats,
                        'veg_results': veg_results,
                        'method': detection_method,
                        'image1_idx': image1_idx,
                        'image2_idx': image2_idx
                    }
                    
                    st.success("✅ Analysis completed successfully!")
                    
                    # Display results
                    st.markdown("---")
                    st.markdown("### 📊 Key Performance Indicators")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric(
                            label="Total Area Analyzed",
                            value=f"{stats['total_pixels']:,}",
                            delta="pixels"
                        )
                    
                    with col2:
                        st.metric(
                            label="Changed Area",
                            value=f"{stats['changed_pixels']:,}",
                            delta=f"{stats['change_percentage']:.2f}%"
                        )
                    
                    with col3:
                        st.metric(
                            label="Change Regions",
                            value=f"{stats['num_change_regions']:,}",
                            delta="detected"
                        )
                    
                    with col4:
                        st.metric(
                            label="Avg Region Size",
                            value=f"{stats['mean_region_size']:.0f}",
                            delta="pixels"
                        )
                    
                    # AI-Powered Summary
                    if enable_ai_summary:
                        st.markdown("---")
                        st.markdown("### 🤖 AI-Powered Insight")
                        
                        with st.spinner("🔄 Generating natural language summary..."):
                            summary = generate_summary(stats, detection_method, gemini_api_key)
                        
                        # Display summary in a nice box
                        st.info(f"**📝 Summary:**\n\n{summary}")
                        
                        # Quick insight (no API needed)
                        quick_insight = get_quick_insight(stats['change_percentage'])
                        st.caption(f"**Quick Insight:** {quick_insight}")
                    
                    # Visualizations
                    st.markdown("---")
                    st.markdown("### 🗺️ Change Detection Visualizations")
                    
                    # Get normalized images for display
                    img1_norm, img2_norm = detector.normalize_images()
                    
                    # Create display images
                    def create_display_image(img):
                        if img.shape[0] >= 3:
                            rgb = np.stack([img[0], img[1], img[2]], axis=2)
                        else:
                            gray = img[0]
                            rgb = np.stack([gray, gray, gray], axis=2)
                        return np.clip(rgb, 0, 1)
                    
                    display_img1 = create_display_image(img1_norm)
                    display_img2 = create_display_image(img2_norm)
                    
                    # Create overlay
                    overlay = display_img2.copy()
                    overlay[change_map == 1] = [1, 0, 0]  # Red for changes
                    
                    # Display images
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("##### 📅 Earlier Image")
                        fig1, ax1 = plt.subplots(figsize=(8, 8))
                        ax1.imshow(display_img1)
                        ax1.axis('off')
                        ax1.set_title(st.session_state.image_metadata[image1_idx]['name'], fontsize=10)
                        st.pyplot(fig1)
                        plt.close()
                    
                    with col2:
                        st.markdown("##### 📅 Later Image")
                        fig2, ax2 = plt.subplots(figsize=(8, 8))
                        ax2.imshow(display_img2)
                        ax2.axis('off')
                        ax2.set_title(st.session_state.image_metadata[image2_idx]['name'], fontsize=10)
                        st.pyplot(fig2)
                        plt.close()
                    
                    with col3:
                        if show_overlay:
                            st.markdown("##### 🔴 Change Detection")
                            fig3, ax3 = plt.subplots(figsize=(8, 8))
                            ax3.imshow(overlay)
                            ax3.axis('off')
                            ax3.set_title("Changes Highlighted in Red", fontsize=10)
                            st.pyplot(fig3)
                            plt.close()
                    
                    # Additional visualizations
                    if show_heatmap or show_overlay:
                        st.markdown("---")
                        cols = st.columns(2)
                        
                        if show_overlay:
                            with cols[0]:
                                st.markdown("##### 🗺️ Binary Change Map")
                                fig4, ax4 = plt.subplots(figsize=(10, 8))
                                im = ax4.imshow(change_map, cmap='RdYlGn_r', interpolation='nearest')
                                ax4.axis('off')
                                ax4.set_title("Red = Changed, Green = Unchanged", fontsize=12)
                                plt.colorbar(im, ax=ax4)
                                st.pyplot(fig4)
                                plt.close()
                        
                        if show_heatmap:
                            with cols[1]:
                                st.markdown("##### 📈 Change Intensity Heatmap")
                                diff = detector.calculate_difference('absolute')
                                fig5, ax5 = plt.subplots(figsize=(10, 8))
                                im = ax5.imshow(diff, cmap='hot', interpolation='bilinear')
                                ax5.axis('off')
                                ax5.set_title("Intensity of Changes", fontsize=12)
                                plt.colorbar(im, ax=ax5, label='Change Magnitude')
                                st.pyplot(fig5)
                                plt.close()
                    
                    # Vegetation analysis
                    if veg_results and detection_method == "Vegetation Analysis":
                        st.markdown("---")
                        st.markdown("### 🌿 Vegetation Change Analysis")
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.markdown("##### NDVI - Earlier")
                            fig, ax = plt.subplots(figsize=(8, 8))
                            im = ax.imshow(veg_results['ndvi1'], cmap='RdYlGn', vmin=-1, vmax=1)
                            ax.axis('off')
                            plt.colorbar(im, ax=ax, label='NDVI')
                            st.pyplot(fig)
                            plt.close()
                        
                        with col2:
                            st.markdown("##### NDVI - Later")
                            fig, ax = plt.subplots(figsize=(8, 8))
                            im = ax.imshow(veg_results['ndvi2'], cmap='RdYlGn', vmin=-1, vmax=1)
                            ax.axis('off')
                            plt.colorbar(im, ax=ax, label='NDVI')
                            st.pyplot(fig)
                            plt.close()
                        
                        with col3:
                            st.markdown("##### NDVI Change")
                            fig, ax = plt.subplots(figsize=(8, 8))
                            im = ax.imshow(veg_results['ndvi_change'], cmap='RdBu', vmin=-0.5, vmax=0.5)
                            ax.axis('off')
                            plt.colorbar(im, ax=ax, label='NDVI Δ')
                            st.pyplot(fig)
                            plt.close()
                        
                        # Vegetation stats
                        veg_loss_pixels = np.sum(veg_results['vegetation_loss'])
                        veg_gain_pixels = np.sum(veg_results['vegetation_gain'])
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric(
                                "Vegetation Loss",
                                f"{veg_loss_pixels:,} pixels",
                                f"-{(veg_loss_pixels/stats['total_pixels']*100):.2f}%"
                            )
                        with col2:
                            st.metric(
                                "Vegetation Gain",
                                f"{veg_gain_pixels:,} pixels",
                                f"+{(veg_gain_pixels/stats['total_pixels']*100):.2f}%"
                            )
                    
                    # Export section
                    st.markdown("---")
                    st.markdown("### 💾 Export Results")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        # Export change map
                        change_df = pd.DataFrame(change_map)
                        csv = change_df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Change Map (CSV)",
                            data=csv,
                            file_name=f"change_map_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
                    
                    with col2:
                        # Export statistics
                        stats_df = pd.DataFrame({
                            'Metric': list(stats.keys()),
                            'Value': list(stats.values())
                        })
                        stats_csv = stats_df.to_csv(index=False)
                        st.download_button(
                            label="📥 Download Statistics (CSV)",
                            data=stats_csv,
                            file_name=f"statistics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
                    
                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")
                    st.exception(e)
        else:
            st.info("👈 Configure your analysis parameters in the sidebar and click 'Run Analysis'")

# Tab 2: Image Gallery
with tab2:
    st.markdown("### 🖼️ Image Gallery")
    
    if len(st.session_state.uploaded_images) == 0:
        st.info("No images loaded yet. Upload images using the sidebar.")
    else:
        # Display images in a grid
        cols_per_row = 3
        for i in range(0, len(st.session_state.uploaded_images), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                idx = i + j
                if idx < len(st.session_state.uploaded_images):
                    with col:
                        # Image preview
                        thumbnail = create_thumbnail(st.session_state.uploaded_images[idx])
                        fig, ax = plt.subplots(figsize=(6, 6))
                        ax.imshow(thumbnail)
                        ax.axis('off')
                        st.pyplot(fig)
                        plt.close()
                        
                        # Metadata
                        metadata = st.session_state.image_metadata[idx]
                        st.markdown(f"**#{idx+1}: {metadata['name']}**")
                        st.text(f"Size: {metadata['width']}x{metadata['height']}")
                        st.text(f"Bands: {metadata['bands']}")
                        st.text(f"Type: {metadata['dtype']}")
                        
                        # Remove button
                        if st.button("🗑️ Remove", key=f"remove_{idx}"):
                            remove_image(idx)
                            st.rerun()

# Tab 3: Statistics
with tab3:
    st.markdown("### 📈 Detailed Statistics")
    
    if st.session_state.analysis_results:
        stats = st.session_state.analysis_results['stats']
        
        # Statistics table
        stats_df = pd.DataFrame({
            'Metric': [
                'Total Pixels',
                'Changed Pixels',
                'Unchanged Pixels',
                'Change Percentage',
                'Number of Change Regions',
                'Mean Region Size',
                'Maximum Region Size'
            ],
            'Value': [
                f"{stats['total_pixels']:,}",
                f"{stats['changed_pixels']:,}",
                f"{stats['unchanged_pixels']:,}",
                f"{stats['change_percentage']:.2f}%",
                f"{stats['num_change_regions']:,}",
                f"{stats['mean_region_size']:.2f} px",
                f"{stats['max_region_size']:.0f} px"
            ]
        })
        
        st.dataframe(stats_df, width='stretch', hide_index=True)
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            fig = go.Figure(data=[go.Pie(
                labels=['Changed', 'Unchanged'],
                values=[stats['changed_pixels'], stats['unchanged_pixels']],
                hole=.3,
                marker_colors=['#e74c3c', '#2ecc71']
            )])
            fig.update_layout(title_text="Pixel Distribution")
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            # Bar chart
            fig = go.Figure(data=[
                go.Bar(name='Metrics', x=['Change %', 'Regions', 'Avg Size'],
                       y=[stats['change_percentage'], stats['num_change_regions'], stats['mean_region_size']/10],
                       marker_color='#667eea')
            ])
            fig.update_layout(title_text="Key Metrics")
            st.plotly_chart(fig, width='stretch')
        
        # Image comparison info
        st.markdown("---")
        st.markdown("### 📊 Comparison Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Earlier Image**")
            meta1 = st.session_state.image_metadata[st.session_state.analysis_results['image1_idx']]
            st.json(meta1)
        
        with col2:
            st.markdown("**Later Image**")
            meta2 = st.session_state.image_metadata[st.session_state.analysis_results['image2_idx']]
            st.json(meta2)
    else:
        st.info("Run an analysis first to see statistics.")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d; padding: 1rem;'>
        🛰️ Satellite Image Change Detection System | Real-Time Environmental Monitoring BI Dashboard
    </div>
""", unsafe_allow_html=True)
