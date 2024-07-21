# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load your dataset
df = pd.read_csv('goldstock v1.csv')

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

# Plotting a histogram of the 'Open' column
plt.hist(df['Open'], bins=10)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Open Prices')
plt.show()

# Statistical hypothesis testing (example)
# Conduct t-test between 'Open' and 'Close' prices
t_stat, p_value = stats.ttest_ind(df['Open'], df['Close'])
print("\nT-test Results:")
print(f"T-statistic: {t_stat}, p-value: {p_value}")

# Additional data exploration and analysis goes here
