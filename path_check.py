import os

# Define the exact file path
file_path = r'C:\Users\Lui\Documents\web_scraping_project\goldstock v1.csv'

# Check if the file exists
if os.path.exists(file_path):
    print(f"File exists: {file_path}")
else:
    print(f"File does not exist: {file_path}")




