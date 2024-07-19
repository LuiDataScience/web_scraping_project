# Web Scraping Project

## Overview
This project involves web scraping to collect data from various websites. The collected data is then analyzed to extract meaningful insights.

## Project Structure
- `scrape_data.py`: Script to scrape data from websites.
- `analyze_data.py`: Script to analyze the scraped data.
- `headlines.csv`: CSV file containing the scraped headlines.
- `web_scraping_project/`: Directory containing additional project files.

## Statistical Modeling Project

### Overview
In this project, we conducted statistical hypothesis testing and modeling to explore correlations and trends in the gold stock dataset. Using Python and libraries like Pandas and Matplotlib, we performed t-tests, regression analysis, and visualized data to derive insights.

### Results
- Conducted a t-test to compare the means of two columns.
- Identified significant differences between groups.
- Visualized trends over time using line charts and histograms.

For detailed analysis and code, please refer to the Jupyter Notebook or Python scripts provided in this repository.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/LuiDataScience/web_scraping_project.git
   cd web_scraping_project
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
headlines = soup.find_all(['h2', 'h3'], class_=['zone__title', 'zone__title'])

# Extract headline texts
headline_texts = [headline.get_text(strip=True) for headline in headlines]

# Create a DataFrame
df = pd.DataFrame(headline_texts, columns=['Headline'])
print(df.head())

# Save the data to a CSV file
df.to_csv('headlines.csv', index=False)
print("Headlines saved to headlines.csv")

