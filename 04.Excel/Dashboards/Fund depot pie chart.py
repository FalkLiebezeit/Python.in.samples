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

# Set the window size to 800 x 600 pixels (8 inches x 6 inches at 100 dpi)
plt.figure(figsize=(8, 6))

# Create a pie chart of the fund values
plt.pie(
    data["€"],
    labels=data["Fund name"],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("coolwarm", len(data))
)

# Set the plot title
plt.title("Fund Portfolio Value Distribution")

# Ensure the pie chart is a circle
plt.axis('equal')

# Show the plot
plt.tight_layout()
plt.show()