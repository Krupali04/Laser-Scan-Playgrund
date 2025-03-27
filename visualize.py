import plotly.graph_objects as go
import numpy as np

def plot_dashboard(surface, scan_data, defect_mask, scan_step):
    """
    Create an interactive Plotly dashboard with surface, scan, and defects.
    """
    fig = go.Figure()

    # Full surface heatmap
    fig.add_trace(go.Heatmap(z=surface, colorscale="gray", name="Surface"))
    
    # Scanned portion so far
    if scan_step > 0:
        scanned = np.zeros_like(surface)
        scanned[:scan_step, :] = scan_data[:scan_step, :]
        fig.add_trace(go.Heatmap(z=scanned, colorscale="viridis", name="Scanned", opacity=0.5))
    
    # Defects overlay
    fig.add_trace(go.Heatmap(z=defect_mask, colorscale="hot", name="Defects", opacity=0.7))

    # Layout
    fig.update_layout(
        title="Laser Scan Playground",
        updatemenus=[{
            "buttons": [
                {"label": "Surface", "method": "update", "args": [{"visible": [True, False, False]}]},
                {"label": "Scan", "method": "update", "args": [{"visible": [False, True, False]}]},
                {"label": "Defects", "method": "update", "args": [{"visible": [False, False, True]}]},
                {"label": "All", "method": "update", "args": [{"visible": [True, True, True]}]}
            ],
            "direction": "down",
            "showactive": True
        }]
    )
    fig.show()