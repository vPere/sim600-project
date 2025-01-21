import matplotlib.pyplot as plt
import numpy as np
import os

# Define categories and scores for each firewall
categories = [
    "First steps",
    "UI",
    "Rule\nManagement",
    "Logs\nand\nMonitoring",
    "Community\nand\nSupport",
    "Troubleshooting"
]

# Scores for each firewall
scores = {
    "OPNsense": [5.500, 8.500, 6.000, 8.600, 6.700, 8.75],
    "pfSense": [7.200, 8.667, 5.600, 10.000, 9.200, 8],
    "VNS3 Cloud Firewall": [2.700, 3.500, 6.800, 3.500, 4.000, 3.25],
    "FortiGate": [5.750, 7.125, 6.800, 9.200, 8.200, 7.5],
    "Azure Firewall": [3.100, 5.625, 1.300, 0.600, 5.200, 8]
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
output_path = "output/GENERAL_radar_chart.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save the radar chart as a PNG image
plt.savefig(output_path, dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
