import matplotlib.pyplot as plt
import numpy as np
import os

# Define categories and scores for each firewall
categories = ["Log Clarity", "Log Filtering", "Real-Time\nMonitoring"]


# Scores for each firewall
scores = {
    "OPNsense": [8, 8, 10],
    "pfSense": [10, 10, 10],
    "VNS3 Cloud Firewall": [2, 4, 5],
    "FortiGate": [8, 10, 10],
    "Azure Firewall": [0, 2, 0]
}

# Convert categories to angles for the radar chart
num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop by appending the start angle

# Create the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Loop through each firewall and plot its data
for firewall, firewall_scores in scores.items():
    data = firewall_scores + firewall_scores[:1]  # Complete the loop
    ax.plot(angles, data, label=firewall, linewidth=1.5)
    ax.fill(angles, data, alpha=0.25)

# Add category labels
ax.set_yticks([1,2,3,4,5,6,7,8,9,10])
ax.set_ylim(0, 10)  # Set the radial axis limit from 0 to 10
ax.set_yticklabels([])  # Hide the radial axis numbers
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.xaxis.set_tick_params(pad=28)  # Adjust 'pad' to control the distance

# Add legend and title
ax.legend(loc='upper left', bbox_to_anchor=(-1.15, 0.9), fontsize=12)
#plt.title("Firewall Usability Comparison", fontsize=14, pad=20)

# Ensure the output directory exists
output_path = "output/Logs_radar_chart.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save the radar chart as a PNG image
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
