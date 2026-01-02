"""Job Stress Data Analysis with Multiple Charts

This module analyzes job stress data and creates multiple visualizations
including correlation heatmaps, scatterplots, and regression plots.
All charts are automatically saved to the 'output' directory.
"""

import os
import numpy as np
import pandas as pd 
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Create output directory for saved charts
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

#Let's read the data into Pandas dataframe:
data = pd.read_csv("https://raw.githubusercontent.com/swapnilsaurav/BookPythonAppsOnVSCode/main/JobStressData.csv")

print("Dataset shape:", data.shape)  # shows number of rows, columns

summary = data.describe()
print("\nData Summary:")
print(summary)


# Filter the data for job role = MANAGER
manager_df = data.loc[data['Role'] == "MANAGER"]
manager_df = manager_df.drop('Role', axis=1)
print("\nManager Data Correlation:")
print(manager_df.corr())

# Chart 1: Correlation heatmap
plt.figure(figsize=(10, 8))
ax = sns.heatmap(manager_df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Heatmap - Manager Data")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_correlation_heatmap.png", dpi=300, bbox_inches='tight')
print(f"Saved: {OUTPUT_DIR}/01_correlation_heatmap.png")
plt.close()

# Chart 2: Scatterplot - Initial
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x="WorkFamilyConflict", y="JobStress", data=manager_df)
ax.set_title("Job Stress vs. Work-Family Conflict (All Data)")
ax.set_xlabel("Work-Family Conflict")
ax.set_ylabel("Job Stress")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_scatterplot_all_data.png", dpi=300, bbox_inches='tight')
print(f"Saved: {OUTPUT_DIR}/02_scatterplot_all_data.png")
plt.close()

# Let's use .loc to restrict values of 'WorkFamilyConflict' displayed
manager_df = manager_df.loc[manager_df['WorkFamilyConflict'].between(0, 70)]

# Chart 3: Scatterplot - Filtered data
plt.figure(figsize=(10, 6))
ax = sns.scatterplot(x="WorkFamilyConflict", y="JobStress", data=manager_df)
ax.set_title("Job Stress vs. Work-Family Conflict (Filtered 0-70)")
ax.set_xlabel("Work-Family Conflict")
ax.set_ylabel("Job Stress")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_scatterplot_filtered.png", dpi=300, bbox_inches='tight')
print(f"Saved: {OUTPUT_DIR}/03_scatterplot_filtered.png")
plt.close()

# Chart 4: Linear regression plot
plt.figure(figsize=(10, 6))
ax = sns.lmplot(x="WorkFamilyConflict", y="JobStress", data=manager_df, height=6, aspect=1.5)
ax.set(title="Job Stress vs. Work-Family Conflict (with Regression Line)")
ax.set(xlabel="Work-Family Conflict", ylabel="Job Stress")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_regression_plot.png", dpi=300, bbox_inches='tight')
print(f"Saved: {OUTPUT_DIR}/04_regression_plot.png")
plt.close()

# Chart 5: Multi-dimensional analysis with Family Support
plt.figure(figsize=(12, 6))
ax = sns.lmplot(x="WorkFamilyConflict", y="JobStress",
                hue="FamilySupportScore", data=manager_df, height=6, aspect=1.8)
ax.set(title="Job Stress vs. Work-Family Conflict (by Family Support Score)")
ax.set(xlabel="Work-Family Conflict", ylabel="Job Stress")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/05_multidimensional_plot.png", dpi=300, bbox_inches='tight')
print(f"Saved: {OUTPUT_DIR}/05_multidimensional_plot.png")
plt.close()

# Coefficient of correlation
corr, p_value = pearsonr(manager_df['JobStress'], manager_df['WorkFamilyConflict'])
print(f'\n{"="*50}')
print(f"Pearson Correlation Coefficient: {corr:.3f}")
print(f"P-value: {p_value:.4f}")
print(f'{"="*50}')

print(f"\nAll charts have been saved to the '{OUTPUT_DIR}' directory.")