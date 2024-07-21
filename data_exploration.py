import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Lui\Documents\web_scraping_project\combined_goldstock_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Display the column names
print(df.columns)

# Calculate basic statistics
statistics = df.describe()
print("\nBasic Statistics:")
print(statistics)

# Calculate correlations between numeric columns only
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlations = numeric_df.corr()
print("\nCorrelation Matrix:")
print(correlations)

# Plotting a histogram of the 'Close' column
plt.figure(figsize=(10, 6))
sns.histplot(df['Close'], bins=30, kde=True)
plt.xlabel('Close Price')
plt.ylabel('Frequency')
plt.title('Histogram of Close Prices')
plt.show()

# Plotting a scatter plot of 'Close' vs 'Volume'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Close', y='Volume', data=df)
plt.xlabel('Close Price')
plt.ylabel('Volume')
plt.title('Scatter Plot of Close Price vs Volume')
plt.show()

# Additional data exploration and analysis goes here

