# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load your dataset
df = pd.read_csv('goldstock_v1.csv')

# Display the first few rows of the dataset
print(df.head())

# Calculate basic statistics
statistics = df.describe()
print("\nBasic Statistics:")
print(statistics)

# Calculate correlations between columns
correlations = df.corr()
print("\nCorrelation Matrix:")
print(correlations)

# Plotting a histogram of a specific column
# Replace 'column_name' with the actual column name from your dataset
plt.hist(df['column_name'], bins=10)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Column')
plt.show()

# Statistical hypothesis testing (example)
# Replace 'column1' and 'column2' with actual column names from your dataset
t_stat, p_value = stats.ttest_ind(df['column1'], df['column2'])
print("\nT-test Results:")
print(f"T-statistic: {t_stat}, p-value: {p_value}")

# Additional data exploration and analysis goes here
