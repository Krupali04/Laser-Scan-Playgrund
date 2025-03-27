import numpy as np
import cv2
from scan_sim import generate_surface, simulate_laser_scan, detect_defects, count_defects
from visualize import plot_dashboard

def main():
    # Generate synthetic surface
    surface = generate_surface(width=100, height=100, noise_level=0.2)
    
    # Simulate laser scan (e.g., halfway through)
    scan_speed = 2
    scan_data = simulate_laser_scan(surface, scan_speed)
    scan_step = len(scan_data)  # Show full scan; tweak this for "real-time" feel
    
    # Detect defects
    defect_mask = detect_defects(surface, threshold=40)
    defect_count = count_defects(defect_mask)
    print(f"Detected {defect_count} defect pixels")
    
    # Save a snapshot (like you added this later)
    cv2.imwrite("output/scan_demo.png", defect_mask)
    print("Defect map saved to output/scan_demo.png")
    
    # Visualize
    plot_dashboard(surface, scan_data, defect_mask, scan_step)

if __name__ == "__main__":
    main()