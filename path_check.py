import os

# Use the exact file path
# Check if the file exists
file_path = r'C:\Users\Lui\Documents\web_scraping_project\goldstock v1.csv'
if os.path.exists(file_path):
    print(f"File exists: {file_path}")
else:
    print(f"File does not exist: {file_path}")



