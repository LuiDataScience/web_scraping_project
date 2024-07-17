import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'https://www.bbc.com/news'  # Replace with the actual URL of the news website

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find the relevant data (e.g., headlines)
headlines = soup.find_all('h3', class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')  # Adjust the class as per the actual HTML structure

# Print the headlines to check if they are being scraped correctly
for headline in headlines:
    print(headline.text.strip())

# Save the headlines to a CSV file
with open('headlines.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])

    # Write the headlines to the CSV file
    for headline in headlines:
        writer.writerow([headline.text.strip()])





