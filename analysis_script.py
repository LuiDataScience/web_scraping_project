import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Lui\Documents\web_scraping_project\combined_goldstock_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe(include='all'))

# Calculate correlations between numeric columns only
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlations = numeric_df.corr()
print("\nCorrelation Matrix:")
print(correlations)

# Plotting a histogram of the 'Close' column
plt.hist(df['Close'], bins=30, edgecolor='k')
plt.xlabel('Close Price')
plt.ylabel('Frequency')
plt.title('Histogram of Close Prices')
plt.show()

# Additional data exploration and analysis goes here


