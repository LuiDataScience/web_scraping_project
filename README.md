# Web Scraping Project

## Overview
This project involves scraping headlines from the CNN World News page and performing basic data analysis.

## Steps
1. **Web Scraping**: Using BeautifulSoup and Requests libraries to scrape headlines from CNN.

### Example Code

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'https://www.cnn.com/world'

# Send a GET request to the website
response = requests.get(url)
print(f"Response status code: {response.status_code}")

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all potential headline tags and classes
headlines = soup.find_all(['h2', 'h3'], class_=['cd__headline', 'zone__title', 'cd__headline-text'])

# Extract headline texts
headline_texts = [headline.get_text(strip=True) for headline in headlines]

# Create a DataFrame
df = pd.DataFrame(headline_texts, columns=['Headline'])
print(df.head())

# Save the data to a CSV file
df.to_csv('headlines.csv', index=False)
print("Headlines saved to headlines.csv")




