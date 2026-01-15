import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create the fund data as a pandas DataFrame
data = pd.DataFrame({
    "Fund name": [
        "Amundi Ex China UCITS ETF Acc",
        "Amundi Semiconductor",
        "iShares South Africa",
        "iShares S&P 500 ",
        "UBS Solactive China"
    ],
    "€": [
        40462.95,
        41790.59,
        9880.13,
        57340.94,
        38343.43
    ]
})

# Set Seaborn theme for a clean, modern look
sns.set_theme(style="whitegrid")

# Set the window size to 800 x 600 pixels (8 inches x 6 inches at 100 dpi)
plt.figure(figsize=(8, 6))

# Create a bar plot with a custom color palette
sns.barplot(x="Fund name", y="€", data=data, palette="coolwarm")

# Set the plot title
plt.title("Fund Portfolio Value by Fund")

# Rotate x-axis labels for better readability
plt.xticks(rotation=20, ha='right')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
