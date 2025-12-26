import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create example data as a pandas DataFrame
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 15, 7, 12]
})

# Set Seaborn theme for a clean, modern look
sns.set_theme(style="whitegrid")

# Create a bar plot with a custom color palette
sns.barplot(x="Category", y="Values", data=data, palette="coolwarm")

# Set the plot title
plt.title("Seaborn Bar Chart Example")

# Show the plot
plt.show()