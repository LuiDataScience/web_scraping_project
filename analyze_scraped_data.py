import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Lui\Documents\web_scraping_project\scraped_data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(df.head())

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe(include='all'))

# Display the column names
print("\nColumn Names:")
print(df.columns)

# Check if the required columns exist in the dataframe
required_columns = ['Tag', 'Text']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Column '{col}' not found in the dataset")

# Create a count plot of the 'Tag' column
plt.figure(figsize=(10, 6))
sns.countplot(y='Tag', data=df, order=df['Tag'].value_counts().index)
plt.title('Count of Tags')
plt.xlabel('Count')
plt.ylabel('Tag')
plt.show()

# Create a word frequency plot for the 'Text' column

# Combine all text into one large string
all_text = ' '.join(df['Text'].dropna().values)

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Text')
plt.show()

# Additional data exploration and analysis goes here
