

```python
import os
import pandas as pd

# Paths to the datasets
file_paths = [
    r'C:\Users\Lui\Documents\web_scraping_project\goldstock v1.csv',
    r'C:\Users\Lui\Documents\web_scraping_project\goldstock v2.csv'
]

# Function to load and process data
def load_and_process_data(file_path):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}")
        print(df.head())
        return df
    else:
        print(f"File does not exist: {file_path}")
        return None

# Load and process each dataset
dfs = [load_and_process_data(path) for path in file_paths]

# Combine datasets if needed
combined_df = pd.concat(dfs, ignore_index=True)

# Save combined data to a new CSV file
output_path = 'combined_goldstock_data.csv'
combined_df.to_csv(output_path, index=False)
print(f"Combined data saved to {output_path}")
