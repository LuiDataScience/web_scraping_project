import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use the correct file path
file_path = r'C:\Users\Lui\Pictures\Screenshots\DataAnalysisProject\goldstock_v1.csv'

try:
    df = pd.read_csv(file_path)
    # Display the first few rows of the dataset
    print(df.head())

    # Display the column names
    print(df.columns)

    # Check if the required columns exist in the dataframe
    required_columns = ['Close', 'Volume']  # Update with actual column names
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column '{col}' not found in the dataset")

    # Create plots based on column names
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Close'], bins=30, kde=True)  # Replace 'Close' with the actual column name
    plt.title('Histogram of Close')  # Update the title
    plt.xlabel('Close')  # Update the label
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Close', y='Volume', data=df)  # Replace 'Close' and 'Volume' with the actual column names
    plt.title('Scatter Plot of Close vs Volume')  # Update the title
    plt.xlabel('Close')  # Update the x-axis label
    plt.ylabel('Volume')  # Update the y-axis label
    plt.show()

except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except pd.errors.EmptyDataError:
    print("Error: No data found in the file.")
except ValueError as e:
    print(f"Error: {e}")
