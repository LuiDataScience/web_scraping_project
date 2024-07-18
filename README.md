# Web Scraping Project

## Overview
This project involves scraping financial data from a specified website and performing basic data analysis.

## Steps
1. **Web Scraping**:
   BeautifulSoup and Requests libraries are used to scrape data from the web.

   ```python
   import requests
   from bs4 import BeautifulSoup
   import pandas as pd

   # URL of the website to scrape
   url = 'http://example.com'

   # Send a GET request to the website
   response = requests.get(url)

   # Parse the HTML content
   soup = BeautifulSoup(response.content, 'html.parser')

   # Extract data (example: extracting table data)
   table = soup.find('table')
   rows = table.find_all('tr')

   # Extract column names
   columns = [header.text for header in rows[0].find_all('th')]

   # Extract rows data
   data = []
   for row in rows[1:]:
       cells = row.find_all('td')
       data.append([cell.text for cell in cells])

   # Create a DataFrame
   df = pd.DataFrame(data, columns=columns)

   # Save the data to a CSV file
   df.to_csv('scraped_data.csv', index=False)

