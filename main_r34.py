import pandas as pd
from scipy import stats
import numpy as np

# Load the CSV file into a DataFrame
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Calculate the percentage of deaths per birth
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Categorize data before and after handwashing implementation
df['handwashing_start'] = np.where(df['date'] < '1847-06-01', 'Before Handwashing', 'After Handwashing')

# Separate the data into two groups
before_handwashing = df[df['handwashing_start'] == 'Before Handwashing']['pct_deaths']
after_handwashing = df[df['handwashing_start'] == 'After Handwashing']['pct_deaths']

# Perform the independent t-test
t_statistic, p_value = stats.ttest_ind(before_handwashing, after_handwashing, equal_var=False)

# Print the t-statistic and p-value
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
