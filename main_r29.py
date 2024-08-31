import pandas as pd
import plotly.express as px
import numpy as np

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Add the 'pct_deaths' column to calculate the percentage of deaths per birth
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Add the 'handwashing_start' column to indicate whether the date is before or after June 1847
df['handwashing_start'] = np.where(df['date'] < '1847-06-01', 'Before Handwashing', 'After Handwashing')

# Create overlapping histograms with a box plot on top using Plotly Express
fig = px.histogram(df,
                   x='pct_deaths',
                   color='handwashing_start',  # Differentiate by handwashing period
                   nbins=20,
                   title='Distribution of Monthly Death Percentages Before and After Handwashing',
                   labels={'pct_deaths': 'Percentage of Deaths'},
                   opacity=0.7,  # Set opacity for overlapping effect
                   barmode='overlay',  # Overlay the histograms
                   histnorm='percent',  # Normalize to percent
                   marginal='box')  # Add a box plot on top

# Customize the layout and style
fig.update_layout(
    xaxis_title="Percentage of Deaths",
    yaxis_title="Percentage of Months",
    bargap=0.1  # Adjust the gap between bars
)

# Display the plot
fig.show()
