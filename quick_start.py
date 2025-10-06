"""
Quick Start Script - Satellite Image Change Detection System
Run this to test the system setup
"""

import sys

def check_imports():
    """Check if all required packages are available"""
    required_packages = {
        'rasterio': 'rasterio',
        'numpy': 'numpy',
        'matplotlib': 'matplotlib',
        'streamlit': 'streamlit',
        'plotly': 'plotly',
        'pandas': 'pandas',
        'PIL': 'Pillow',
        'scipy': 'scipy',
        'cv2': 'opencv-python',
        'skimage': 'scikit-image'
    }
    
    missing = []
    installed = []
    
    print("Checking installed packages...")
    print("-" * 60)
    
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            installed.append(package_name)
            print(f"✓ {package_name:<20} - Installed")
        except ImportError:
            missing.append(package_name)
            print(f"✗ {package_name:<20} - Missing")
    
    print("-" * 60)
    print(f"\nInstalled: {len(installed)}/{len(required_packages)}")
    
    if missing:
        print(f"\nMissing packages: {', '.join(missing)}")
        print("\nTo install missing packages, run:")
        print(f"pip install {' '.join(missing)}")
        return False
    else:
        print("\n✓ All packages are installed!")
        return True

def check_images():
    """Check if satellite images are present"""
    from pathlib import Path
    
    print("\n" + "=" * 60)
    print("Checking for satellite images...")
    print("-" * 60)
    
    current_dir = Path(__file__).parent
    tif_files = list(current_dir.glob("*.tif"))
    
    if len(tif_files) >= 2:
        print(f"✓ Found {len(tif_files)} TIF files:")
        for f in tif_files:
            print(f"  - {f.name}")
        return True
    else:
        print(f"✗ Found only {len(tif_files)} TIF file(s)")
        print("  Need at least 2 satellite images for change detection")
        return False

def test_basic_functionality():
    """Test basic change detection functionality"""
    print("\n" + "=" * 60)
    print("Testing basic functionality...")
    print("-" * 60)
    
    try:
        from pathlib import Path
        import rasterio
        import numpy as np
        
        current_dir = Path(__file__).parent
        tif_files = sorted(list(current_dir.glob("*.tif")))
        
        if len(tif_files) < 2:
            print("✗ Not enough images to test")
            return False
        
        # Try to open images
        print(f"Opening: {tif_files[0].name}")
        with rasterio.open(str(tif_files[0])) as src:
            img1 = src.read()
            print(f"  Shape: {img1.shape}")
            print(f"  Dtype: {img1.dtype}")
            print(f"  CRS: {src.crs}")
        
        print(f"Opening: {tif_files[1].name}")
        with rasterio.open(str(tif_files[1])) as src:
            img2 = src.read()
            print(f"  Shape: {img2.shape}")
            print(f"  Dtype: {img2.dtype}")
            print(f"  CRS: {src.crs}")
        
        # Basic difference calculation
        print("\nCalculating difference...")
        diff = np.abs(img2.astype(float) - img1.astype(float))
        print(f"  Mean difference: {np.mean(diff):.4f}")
        print(f"  Max difference: {np.max(diff):.4f}")
        
        print("\n✓ Basic functionality works!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error during testing: {str(e)}")
        return False

def main():
    """Main quick start check"""
    print("=" * 60)
    print("SATELLITE IMAGE CHANGE DETECTION - QUICK START CHECK")
    print("=" * 60)
    
    # Check packages
    packages_ok = check_imports()
    
    # Check images
    images_ok = check_images()
    
    # Test functionality if everything is available
    if packages_ok and images_ok:
        functionality_ok = test_basic_functionality()
    else:
        functionality_ok = False
    
    # Final summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    if packages_ok and images_ok and functionality_ok:
        print("✓ System is ready to use!")
        print("\nNext steps:")
        print("  1. Run the interactive dashboard:")
        print("     streamlit run app.py")
        print("\n  2. Or run the example script:")
        print("     python example_usage.py")
    else:
        print("✗ System is not ready")
        print("\nPlease fix the issues above and run this script again.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
