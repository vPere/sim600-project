import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the data for the radar chart
categories = ["Onboarding and Initial Setup", "UX/UI", "Rule Management", "Logging and Monitoring", "Community and Support", "Default Features", "Troubleshooting/Diagnostics Tools"]

# Scores for each firewall
firewalls = {
    "OPNsense": [5.6, 8.8, 7.18, 8.6, 6.7, 8.25, 9.5],
    "pfSense": [8.0, 8.4, 7.21, 10.0, 9.2, 5.5, 8.0],
    "VNS3 Cloud Firewall": [2.8, 2.8, 6.15, 3.5, 4.0, 3.5, 4.5],
    "FortiGate": [5.55, 6.4, 7.73, 9.2, 8.2, 7.5, 5.0],
    "Azure Firewall": [4.1, 5.6, 4.6, 0.6, 5.2, 2.0, 6.0]
}

# Convert to a DataFrame
data = pd.DataFrame(firewalls, index=categories)

def make_spider(row, title, color):
    labels = data.index
    num_vars = len(labels)

    # Compute angle for each category
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]

    # Initialize plot
    ax = plt.subplot(2, 3, row+1, polar=True)

    # Draw one axe per variable and add labels
    plt.xticks(angles[:-1], labels, color='grey', size=8)

    # Draw y-labels
    ax.set_rscale('linear')
    ax.set_ylim(0, 10)

    # Ind1
    values = data.iloc[:, row].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Title
    plt.title(title, size=11, color=color, y=1.1)

# Initialize figure
plt.figure(figsize=(10, 8), dpi=100)

# Create a radar chart for each firewall
colors = ["blue", "green", "red", "orange", "purple"]
for i, firewall in enumerate(data.columns):
    make_spider(i, firewall, colors[i])

plt.tight_layout()
plt.show()