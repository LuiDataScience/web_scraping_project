import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('headlines.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Create a simple bar plot of the top 10 most frequent words in headlines
word_counts = df['Headline'].str.split(expand=True).stack().value_counts()
top_10_words = word_counts.head(10)

# Plot the top 10 words
plt.figure(figsize=(10, 6))
top_10_words.plot(kind='bar')
plt.title('Top 10 Most Frequent Words in Headlines')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
