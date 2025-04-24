# PYTHON-LIBRARY
Analyzing Data with Pandas and Visualizing Results with Matplotlib
Objective For this Assignment:

To load and analyze a dataset using the pandas library in Python.
To create simple plots and charts with the matplotlib library for visualizing the data.

Submission Requirements
Submit a Jupyter notebook (.ipynb file) or Python script (.py file) containing:
Data loading and exploration steps.
Basic data analysis results.
Visualizations.
Any findings or observations.
Task 1: Load and Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.

import pandas as pd

def load_and_explore_dataset(csv_file="sales_data.csv"):
    """
    Loads a dataset from a CSV file, explores its structure, and cleans it.

    Args:
        csv_file (str, optional): The path to the CSV file. Defaults to "sales_data.csv".
    """
    try:
        # 1. Load the dataset using pandas
        df = pd.read_csv(csv_file)
        print(f"Dataset loaded successfully from '{csv_file}'.\n")

        # 2. Display the first few rows of the dataset
        print("First 5 rows of the dataset:")
        print(df.head().to_markdown(index=False, numalign="left", stralign="left"))  # Use to_markdown for better output

        # 3. Explore the structure of the dataset
        print("\nDataset information (structure and data types):")
        df.info()  # Use df.info() for a concise summary

        # 4. Check for missing values
        print("\nMissing values per column:")
        missing_values = df.isnull().sum()
        print(missing_values.to_markdown(numalign="left", stralign="left")) # Use to_markdown for better output

        # 5. Clean the dataset by handling missing values
        # For demonstration, let's fill numerical missing values with the mean and categorical with the mode
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col].fillna(df[col].mean(), inplace=True)
            elif pd.api.types.is_categorical_dtype(df[col]) or pd.api.types.is_object_dtype(df[col]):
                df[col].fillna(df[col].mode()[0], inplace=True)
        print("\nDataset after cleaning (missing values handled):")
        print(df.head().to_markdown(index=False, numalign="left", stralign="left")) # print first 5 rows of cleaned dataframe

        print("\nMissing values after cleaning:") # Check if there are any missing values after cleaning
        missing_values = df.isnull().sum()
        print(missing_values.to_markdown(numalign="left", stralign="left"))

        return df  # Return the cleaned DataFrame for further use

    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return None  # Return None to indicate failure
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Return None to indicate failure

if __name__ == "__main__":
    # Load and explore the dataset
    cleaned_df = load_and_explore_dataset()
    if cleaned_df is not None:
        # You can perform further analysis or visualization with cleaned_df here
        print("\nFurther analysis can be done with the cleaned dataframe.")

