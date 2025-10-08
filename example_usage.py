"""
Simple example of satellite image change detection
"""

from change_detector import ChangeDetector

def main():
    """
    Basic change detection example
    """
    print("🛰️ Satellite Image Change Detection - Example")
    print("=" * 50)
    
    # Initialize detector with sample images
    print("1. Loading images...")
    detector = ChangeDetector(
        'snapshot-2025-10-01T00_00_00Z.tif',
        'snapshot-2025-10-06T00_00_00Z.tif'
    )
    
    # Load and process images
    detector.load_images()
    print("   ✅ Images loaded successfully")
    
    # Get basic metadata
    metadata = detector.get_metadata()
    print(f"   📐 Dimensions: {metadata['image1']['width']} x {metadata['image1']['height']}")
    print(f"   📊 Bands: {metadata['image1']['count']}")
    
    # Run change detection
    print("\n2. Running Change Detection...")
    change_map = detector.detect_changes_threshold(threshold=0.15)
    stats = detector.analyze_change_statistics(change_map)
    
    # Display results
    print("   📊 Results:")
    print(f"   • Changed pixels: {stats['changed_pixels']:,}")
    print(f"   • Change percentage: {stats['change_percentage']:.2f}%")
    print(f"   • Number of regions: {stats['num_change_regions']}")
    
    # Try automatic detection
    print("\n3. Running Automatic Detection...")
    auto_change_map = detector.detect_changes_otsu()
    auto_stats = detector.analyze_change_statistics(auto_change_map)
    print(f"   • Auto-detected changes: {auto_stats['change_percentage']:.2f}%")
    
    print("\n✅ Analysis complete!")
    print("💡 For interactive analysis, run: streamlit run app.py")


if __name__ == "__main__":
    main()