"""
Satellite Image Change Detection Module
Analyzes temporal changes in satellite imagery
"""

import rasterio
import numpy as np
from skimage import filters, morphology
from skimage.metrics import structural_similarity as ssim
from scipy import ndimage
import cv2
from typing import Tuple, Dict, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChangeDetector:
    """
    Main class for detecting changes between two satellite images
    """
    
    def __init__(self, image1_path: str, image2_path: str):
        """
        Initialize the change detector with two image paths
        
        Args:
            image1_path: Path to the first (earlier) satellite image
            image2_path: Path to the second (later) satellite image
        """
        self.image1_path = image1_path
        self.image2_path = image2_path
        self.image1 = None
        self.image2 = None
        self.metadata1 = None
        self.metadata2 = None
        
    def load_images(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Load the satellite images and their metadata
        
        Returns:
            Tuple of two numpy arrays containing the image data
        """
        logger.info(f"Loading image 1: {self.image1_path}")
        with rasterio.open(self.image1_path) as src1:
            self.image1 = src1.read()
            self.metadata1 = {
                'crs': src1.crs,
                'transform': src1.transform,
                'bounds': src1.bounds,
                'width': src1.width,
                'height': src1.height,
                'count': src1.count
            }
            
        logger.info(f"Loading image 2: {self.image2_path}")
        with rasterio.open(self.image2_path) as src2:
            self.image2 = src2.read()
            self.metadata2 = {
                'crs': src2.crs,
                'transform': src2.transform,
                'bounds': src2.bounds,
                'width': src2.width,
                'height': src2.height,
                'count': src2.count
            }
            
        logger.info(f"Image 1 shape: {self.image1.shape}")
        logger.info(f"Image 2 shape: {self.image2.shape}")
        
        return self.image1, self.image2
    
    def normalize_images(self) -> Tuple[np.ndarray, np.ndarray]:
        """
        Normalize images to 0-1 range for consistent processing
        
        Returns:
            Tuple of normalized images
        """
        def normalize(img):
            img = img.astype(np.float32)
            # Handle each band separately
            normalized = np.zeros_like(img, dtype=np.float32)
            for i in range(img.shape[0]):
                band = img[i]
                band_min, band_max = band.min(), band.max()
                if band_max > band_min:
                    normalized[i] = (band - band_min) / (band_max - band_min)
                else:
                    normalized[i] = band
            return normalized
        
        img1_norm = normalize(self.image1)
        img2_norm = normalize(self.image2)
        
        return img1_norm, img2_norm
    
    def calculate_difference(self, method: str = 'absolute') -> np.ndarray:
        """
        Calculate pixel-wise difference between images
        
        Args:
            method: Method to use ('absolute', 'ratio', 'log_ratio')
            
        Returns:
            Difference image
        """
        img1_norm, img2_norm = self.normalize_images()
        
        if method == 'absolute':
            # Absolute difference
            diff = np.abs(img2_norm - img1_norm)
        elif method == 'ratio':
            # Ratio (avoid division by zero)
            diff = np.divide(img2_norm, img1_norm + 1e-10)
        elif method == 'log_ratio':
            # Log ratio
            diff = np.log(np.divide(img2_norm + 1e-10, img1_norm + 1e-10))
        else:
            raise ValueError(f"Unknown method: {method}")
        
        # Aggregate across bands (mean)
        if len(diff.shape) == 3:
            diff_aggregated = np.mean(diff, axis=0)
        else:
            diff_aggregated = diff
            
        return diff_aggregated
    
    def detect_changes_threshold(self, threshold: float = 0.15) -> np.ndarray:
        """
        Detect changes using simple thresholding
        
        Args:
            threshold: Threshold value for change detection (0-1)
            
        Returns:
            Binary change map
        """
        diff = self.calculate_difference('absolute')
        change_map = (diff > threshold).astype(np.uint8)
        
        # Apply morphological operations to reduce noise
        kernel = morphology.disk(2)
        change_map = morphology.binary_opening(change_map, kernel)
        change_map = morphology.binary_closing(change_map, kernel)
        
        return change_map
    
    def detect_changes_otsu(self) -> np.ndarray:
        """
        Detect changes using Otsu's automatic thresholding
        
        Returns:
            Binary change map
        """
        diff = self.calculate_difference('absolute')
        
        # Normalize to 0-255 for Otsu
        diff_scaled = (diff * 255).astype(np.uint8)
        
        # Apply Otsu's thresholding
        threshold = filters.threshold_otsu(diff_scaled)
        change_map = (diff_scaled > threshold).astype(np.uint8)
        
        # Clean up noise
        kernel = morphology.disk(2)
        change_map = morphology.binary_opening(change_map, kernel)
        change_map = morphology.binary_closing(change_map, kernel)
        
        return change_map
    
    def detect_changes_cvd(self, threshold: float = 0.1) -> np.ndarray:
        """
        Change Vector Detection - detects magnitude of change across all bands
        
        Args:
            threshold: Threshold for change magnitude
            
        Returns:
            Binary change map
        """
        img1_norm, img2_norm = self.normalize_images()
        
        # Calculate change vector magnitude
        diff_vector = img2_norm - img1_norm
        magnitude = np.sqrt(np.sum(diff_vector ** 2, axis=0))
        
        # Threshold
        change_map = (magnitude > threshold).astype(np.uint8)
        
        # Clean up
        kernel = morphology.disk(2)
        change_map = morphology.binary_opening(change_map, kernel)
        
        return change_map
    
    def calculate_vegetation_index(self, image: np.ndarray, 
                                   red_band: int = 0, 
                                   nir_band: int = 1) -> np.ndarray:
        """
        Calculate NDVI (Normalized Difference Vegetation Index)
        
        Args:
            image: Input image array
            red_band: Index of red band
            nir_band: Index of near-infrared band
            
        Returns:
            NDVI array
        """
        if image.shape[0] <= max(red_band, nir_band):
            logger.warning("Not enough bands for NDVI calculation")
            return None
            
        red = image[red_band].astype(np.float32)
        nir = image[nir_band].astype(np.float32)
        
        # Calculate NDVI
        ndvi = np.divide(nir - red, nir + red + 1e-10)
        
        return ndvi
    
    def detect_vegetation_change(self) -> Dict[str, np.ndarray]:
        """
        Detect vegetation changes using NDVI
        
        Returns:
            Dictionary with NDVI maps and change detection
        """
        ndvi1 = self.calculate_vegetation_index(self.image1)
        ndvi2 = self.calculate_vegetation_index(self.image2)
        
        if ndvi1 is None or ndvi2 is None:
            logger.warning("Cannot calculate vegetation change - insufficient bands")
            return {}
        
        ndvi_change = ndvi2 - ndvi1
        
        # Classify changes
        vegetation_loss = (ndvi_change < -0.1).astype(np.uint8)
        vegetation_gain = (ndvi_change > 0.1).astype(np.uint8)
        
        return {
            'ndvi1': ndvi1,
            'ndvi2': ndvi2,
            'ndvi_change': ndvi_change,
            'vegetation_loss': vegetation_loss,
            'vegetation_gain': vegetation_gain
        }
    
    def analyze_change_statistics(self, change_map: np.ndarray) -> Dict[str, float]:
        """
        Calculate statistics about detected changes
        
        Args:
            change_map: Binary change map
            
        Returns:
            Dictionary of statistics
        """
        total_pixels = change_map.size
        changed_pixels = np.sum(change_map)
        unchanged_pixels = total_pixels - changed_pixels
        
        change_percentage = (changed_pixels / total_pixels) * 100
        
        # Label connected components
        labeled_array, num_features = ndimage.label(change_map)
        
        # Calculate sizes of change regions
        sizes = ndimage.sum(change_map, labeled_array, range(num_features + 1))
        
        stats = {
            'total_pixels': int(total_pixels),
            'changed_pixels': int(changed_pixels),
            'unchanged_pixels': int(unchanged_pixels),
            'change_percentage': float(change_percentage),
            'num_change_regions': int(num_features),
            'mean_region_size': float(np.mean(sizes[1:])) if num_features > 0 else 0,
            'max_region_size': float(np.max(sizes[1:])) if num_features > 0 else 0
        }
        
        return stats
    
    def create_change_visualization(self, change_map: np.ndarray) -> np.ndarray:
        """
        Create an RGB visualization of changes overlaid on original images
        
        Args:
            change_map: Binary change map
            
        Returns:
            RGB visualization array
        """
        img1_norm, img2_norm = self.normalize_images()
        
        # Create RGB composite (use first 3 bands if available)
        def create_rgb(img):
            if img.shape[0] >= 3:
                rgb = np.stack([img[0], img[1], img[2]], axis=2)
            else:
                # Grayscale to RGB
                gray = img[0]
                rgb = np.stack([gray, gray, gray], axis=2)
            return rgb
        
        rgb1 = create_rgb(img1_norm)
        rgb2 = create_rgb(img2_norm)
        
        # Create change overlay (red for changes)
        overlay = rgb2.copy()
        overlay[change_map == 1] = [1, 0, 0]  # Red for changes
        
        return overlay
    
    def get_metadata(self) -> Dict:
        """
        Get metadata information about the images
        
        Returns:
            Dictionary containing metadata
        """
        return {
            'image1': self.metadata1,
            'image2': self.metadata2
        }
