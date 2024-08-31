import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Add the 'pct_deaths' column to calculate the percentage of deaths per birth
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Add the 'handwashing_start' column to indicate whether the date is before or after June 1847
df['handwashing_start'] = np.where(df['date'] < '1847-06-01', 'Before Handwashing', 'After Handwashing')

# Create the KDE plot
plt.figure(figsize=(10, 6))

# Plot KDE for the 'Before Handwashing' period
sns.kdeplot(data=df[df['handwashing_start'] == 'Before Handwashing'],
            x='pct_deaths',
            fill=True,
            common_norm=False,
            color="blue",
            alpha=0.5,
            linewidth=2,
            clip=(0, 100),  # Clip the KDE to the range [0, 100]
            label='Before Handwashing')

# Plot KDE for the 'After Handwashing' period
sns.kdeplot(data=df[df['handwashing_start'] == 'After Handwashing'],
            x='pct_deaths',
            fill=True,
            common_norm=False,
            color="red",
            alpha=0.5,
            linewidth=2,
            clip=(0, 100),  # Clip the KDE to the range [0, 100]
            label='After Handwashing')

# Add title and labels
plt.title('KDE of Monthly Death Percentages Before and After Handwashing')
plt.xlabel('Percentage of Deaths')
plt.ylabel('Density')

# Show legend
plt.legend()

# Save the plot to a file instead of displaying it
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\kde_plot_clipped.png"
plt.savefig(output_path)

print(f"KDE plot saved to {output_path}")
