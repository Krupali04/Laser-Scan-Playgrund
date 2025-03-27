import numpy as np
import cv2

def generate_surface(width=100, height=100, noise_level=0.1):
    """
    Create a synthetic 2D surface with smooth variation and random defects.
    """
    # Base surface: smooth gradient
    x, y = np.meshgrid(np.linspace(0, 1, width), np.linspace(0, 1, height))
    surface = 255 * (0.5 * np.sin(2 * np.pi * x) + 0.5 * np.cos(2 * np.pi * y))
    
    # Add random noise to simulate defects
    noise = np.random.random((height, width)) * noise_level * 255
    surface_with_defects = surface + noise
    
    # Clip to 0-255 range (like an 8-bit grayscale image)
    return np.clip(surface_with_defects, 0, 255).astype(np.uint8)

def simulate_laser_scan(surface, scan_speed=1):
    """
    Simulate a laser sweeping across the surface row-by-row.
    Returns a list of scanned rows over time.
    """
    height, width = surface.shape
    scan_data = []
    
    for y in range(0, height, scan_speed):
        row = surface[y, :]
        scan_data.append(row)
    
    return np.array(scan_data)


def detect_defects(surface, threshold=50):
    """
    Detect defects by thresholding deviations from a blurred version of the surface.
    """
    # Blur the surface to get a "normal" baseline
    blurred = cv2.GaussianBlur(surface, (5, 5), 0)
    
    # Difference between original and blurred = potential defects
    diff = cv2.absdiff(surface, blurred)
    
    # Threshold to highlight defects
    _, defect_mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    
    return defect_mask

def count_defects(defect_mask):
    """Count the number of defect pixels."""
    return np.sum(defect_mask > 0) // 255