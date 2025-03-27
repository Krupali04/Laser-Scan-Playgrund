# Laser Scan Playground

## Project Description
This is a little Python toy I kicked off in early 2024 after a physics class demo on optics got me curious about how lasers scan stuff in manufacturing—like wafers for chips. It’s a simulator that pretends a laser sweeps across a fake 2D surface (think a tiny, scratched-up square), finds "defects" (random bumps I added), and shows you what’s going on with some cool visuals. I started it to mess around with scanning ideas at home, and it’s grown into something kinda neat.

Here’s what it does:
- **Makes a Surface**: Creates a 100x100 grid with wavy patterns (using NumPy) and sprinkles random noise to mimic scratches or dirt.
- **Scans It**: Pretends a laser slides across, row-by-row, grabbing data at a speed you can tweak (faster = coarser).
- **Spots Defects**: Uses OpenCV to find weird spots by comparing the surface to a smoothed-out version—marks them as white dots.
- **Shows Off**: Pops up a Plotly dashboard in your browser with heatmaps of the surface, the scan, and the defects. You can toggle what you see.
- **Saves a Pic**: Dumps a black-and-white defect map to a file (`output/scan_demo.png`) so I can keep it.

It’s not a real factory tool—just me playing with code to see if I could mimic something industrial. Over time, I’ve sped up the scan a bit and added the dashboard because staring at numbers got old.