"""
Example usage script for the Satellite Image Change Detection System
Demonstrates various analysis methods programmatically
"""

from change_detector import ChangeDetector
import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Main function demonstrating the change detection system
    """
    print("=" * 70)
    print("Satellite Image Change Detection System - Example Usage")
    print("=" * 70)
    
    # Initialize the detector
    print("\n1. Initializing Change Detector...")
    detector = ChangeDetector(
        'snapshot-2025-10-01T00_00_00Z.tif',
        'snapshot-2025-10-06T00_00_00Z.tif'
    )
    
    # Load images
    print("2. Loading satellite images...")
    img1, img2 = detector.load_images()
    print(f"   Image 1 shape: {img1.shape}")
    print(f"   Image 2 shape: {img2.shape}")
    
    # Get metadata
    print("\n3. Image Metadata:")
    metadata = detector.get_metadata()
    print(f"   CRS: {metadata['image1']['crs']}")
    print(f"   Dimensions: {metadata['image1']['width']} x {metadata['image1']['height']}")
    print(f"   Bands: {metadata['image1']['count']}")
    
    # Method 1: Threshold-based detection
    print("\n4. Running Threshold-based Change Detection...")
    change_map_threshold = detector.detect_changes_threshold(threshold=0.15)
    stats_threshold = detector.analyze_change_statistics(change_map_threshold)
    print(f"   Changes detected: {stats_threshold['changed_pixels']:,} pixels")
    print(f"   Change percentage: {stats_threshold['change_percentage']:.2f}%")
    print(f"   Number of regions: {stats_threshold['num_change_regions']}")
    
    # Method 2: Otsu auto-thresholding
    print("\n5. Running Otsu Auto-threshold Detection...")
    change_map_otsu = detector.detect_changes_otsu()
    stats_otsu = detector.analyze_change_statistics(change_map_otsu)
    print(f"   Changes detected: {stats_otsu['changed_pixels']:,} pixels")
    print(f"   Change percentage: {stats_otsu['change_percentage']:.2f}%")
    print(f"   Number of regions: {stats_otsu['num_change_regions']}")
    
    # Method 3: Change Vector Detection
    print("\n6. Running Change Vector Detection...")
    change_map_cvd = detector.detect_changes_cvd(threshold=0.1)
    stats_cvd = detector.analyze_change_statistics(change_map_cvd)
    print(f"   Changes detected: {stats_cvd['changed_pixels']:,} pixels")
    print(f"   Change percentage: {stats_cvd['change_percentage']:.2f}%")
    print(f"   Number of regions: {stats_cvd['num_change_regions']}")
    
    # Method 4: Vegetation Analysis
    print("\n7. Running Vegetation Change Analysis...")
    veg_results = detector.detect_vegetation_change()
    if veg_results:
        veg_loss = np.sum(veg_results['vegetation_loss'])
        veg_gain = np.sum(veg_results['vegetation_gain'])
        print(f"   Vegetation loss: {veg_loss:,} pixels")
        print(f"   Vegetation gain: {veg_gain:,} pixels")
        print(f"   Net change: {veg_gain - veg_loss:,} pixels")
    else:
        print("   Vegetation analysis not available (insufficient bands)")
    
    # Create visualizations
    print("\n8. Creating visualizations...")
    
    # Get normalized images
    img1_norm, img2_norm = detector.normalize_images()
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Satellite Image Change Detection Results', fontsize=16, fontweight='bold')
    
    # Display images
    def create_display_image(img):
        if img.shape[0] >= 3:
            rgb = np.stack([img[0], img[1], img[2]], axis=2)
        else:
            gray = img[0]
            rgb = np.stack([gray, gray, gray], axis=2)
        return np.clip(rgb, 0, 1)
    
    display_img1 = create_display_image(img1_norm)
    display_img2 = create_display_image(img2_norm)
    
    # Row 1: Original images and difference
    axes[0, 0].imshow(display_img1)
    axes[0, 0].set_title('Earlier Image (Oct 1, 2025)', fontweight='bold')
    axes[0, 0].axis('off')
    
    axes[0, 1].imshow(display_img2)
    axes[0, 1].set_title('Later Image (Oct 6, 2025)', fontweight='bold')
    axes[0, 1].axis('off')
    
    diff = detector.calculate_difference('absolute')
    im = axes[0, 2].imshow(diff, cmap='hot')
    axes[0, 2].set_title('Change Intensity', fontweight='bold')
    axes[0, 2].axis('off')
    plt.colorbar(im, ax=axes[0, 2], fraction=0.046)
    
    # Row 2: Change detection methods
    axes[1, 0].imshow(change_map_threshold, cmap='RdYlGn_r')
    axes[1, 0].set_title(f'Threshold Detection\n({stats_threshold["change_percentage"]:.2f}% changed)', 
                         fontweight='bold')
    axes[1, 0].axis('off')
    
    axes[1, 1].imshow(change_map_otsu, cmap='RdYlGn_r')
    axes[1, 1].set_title(f'Otsu Detection\n({stats_otsu["change_percentage"]:.2f}% changed)', 
                         fontweight='bold')
    axes[1, 1].axis('off')
    
    axes[1, 2].imshow(change_map_cvd, cmap='RdYlGn_r')
    axes[1, 2].set_title(f'CVD Detection\n({stats_cvd["change_percentage"]:.2f}% changed)', 
                         fontweight='bold')
    axes[1, 2].axis('off')
    
    plt.tight_layout()
    
    # Save figure
    output_file = 'change_detection_results.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"   Visualization saved to: {output_file}")
    
    # Show comparison table
    print("\n9. Comparison of Detection Methods:")
    print("-" * 70)
    print(f"{'Method':<25} {'Changed %':<15} {'Regions':<15}")
    print("-" * 70)
    print(f"{'Threshold (0.15)':<25} {stats_threshold['change_percentage']:<15.2f} "
          f"{stats_threshold['num_change_regions']:<15}")
    print(f"{'Otsu Auto-threshold':<25} {stats_otsu['change_percentage']:<15.2f} "
          f"{stats_otsu['num_change_regions']:<15}")
    print(f"{'CVD (0.1)':<25} {stats_cvd['change_percentage']:<15.2f} "
          f"{stats_cvd['num_change_regions']:<15}")
    print("-" * 70)
    
    print("\n10. Analysis Complete!")
    print("=" * 70)
    print("\nNext Steps:")
    print("  - Run 'streamlit run app.py' for interactive dashboard")
    print("  - Adjust thresholds based on results")
    print("  - Export change maps for GIS analysis")
    print("  - View detailed visualizations")
    
    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()