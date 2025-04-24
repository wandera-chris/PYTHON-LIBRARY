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


    Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.

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


def analyze_data(df):
    """
    Performs basic data analysis on the input DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
    """
    if df is None:
        print("Error: No data to analyze. Please ensure the dataset was loaded correctly.")
        return

    # 1. Compute basic statistics of numerical columns
    print("\nBasic statistics of numerical columns:")
    print(df.describe().to_markdown(numalign="left", stralign="left"))

    # 2. Perform groupings on a categorical column and compute the mean of a numerical column for each group
    #    For this example, let's group by 'Product' and compute the mean of 'Revenue ($)'
    if 'Product' in df.columns and 'Revenue ($)' in df.columns:
        print("\nMean Revenue by Product:")
        print(df.groupby('Product')['Revenue ($)'].mean().to_markdown(numalign="left", stralign="left"))

        # 3. Identify any patterns or interesting findings
        print("\nPatterns and Findings:")
        # Example 1: Find the product with the highest average revenue
        highest_avg_revenue_product = df.groupby('Product')['Revenue ($)'].mean().idxmax()
        highest_avg_revenue = df.groupby('Product')['Revenue ($)'].mean().max()
        print(f"- The product with the highest average revenue is '{highest_avg_revenue_product}' with an average revenue of ${highest_avg_revenue:.2f}")

        # Example 2: Calculate the total revenue for each day
        daily_revenue = df.groupby('Date')['Revenue ($)'].sum()
        print("- Daily revenue trends:")
        print(daily_revenue.to_markdown(numalign="left", stralign="left"))
    else:
        print("\nError:  The dataset does not contain the necessary columns ('Product' or 'Revenue ($)') to perform the requested analysis.")

if __name__ == "__main__":
    # Load and explore the dataset
    cleaned_df = load_and_explore_dataset()

    # Perform basic data analysis
    if cleaned_df is not None:
        analyze_data(cleaned_df)

    if cleaned_df is not None:
        # You can perform further analysis or visualization with cleaned_df here




        Task 3: Data Visualization
Create at least four different types of visualizations:
Line chart showing trends over time (for example, a time-series of sales data).
Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
Histogram of a numerical column to understand its distribution.
Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
Customize your plots with titles, labels for axes, and legends where necessary.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


def analyze_data(df):
    """
    Performs basic data analysis on the input DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to analyze.
    """
    if df is None:
        print("Error: No data to analyze. Please ensure the dataset was loaded correctly.")
        return

    # 1. Compute basic statistics of numerical columns
    print("\nBasic statistics of numerical columns:")
    print(df.describe().to_markdown(numalign="left", stralign="left"))

    # 2. Perform groupings on a categorical column and compute the mean of a numerical column for each group
    #    For this example, let's group by 'Product' and compute the mean of 'Revenue ($)'
    if 'Product' in df.columns and 'Revenue ($)' in df.columns:
        print("\nMean Revenue by Product:")
        print(df.groupby('Product')['Revenue ($)'].mean().to_markdown(numalign="left", stralign="left"))

        # 3. Identify any patterns or interesting findings
        print("\nPatterns and Findings:")
        # Example 1: Find the product with the highest average revenue
        highest_avg_revenue_product = df.groupby('Product')['Revenue ($)'].mean().idxmax()
        highest_avg_revenue = df.groupby('Product')['Revenue ($)'].mean().max()
        print(f"- The product with the highest average revenue is '{highest_avg_revenue_product}' with an average revenue of ${highest_avg_revenue:.2f}")

        # Example 2: Calculate the total revenue for each day
        daily_revenue = df.groupby('Date')['Revenue ($)'].sum()
        print("- Daily revenue trends:")
        print(daily_revenue.to_markdown(numalign="left", stralign="left"))
    else:
        print("\nError:  The dataset does not contain the necessary columns ('Product' or 'Revenue ($)') to perform the requested analysis.")



def visualize_data(df):
    """
    Creates visualizations of the data.

    Args:
        df (pd.DataFrame): The DataFrame to visualize.
    """
    if df is None:
        print("Error: No data to visualize. Please ensure the dataset was loaded correctly.")
        return

    # 1. Line chart showing trends over time (e.g., time-series of sales data)
    if 'Date' in df.columns and 'Revenue ($)' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Revenue ($)'], marker='o', linestyle='-')
        plt.title('Daily Revenue Trend')
        plt.xlabel('Date')
        plt.ylabel('Revenue ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: Cannot create line chart.  The dataset does not contain the necessary columns ('Date' and 'Revenue ($)').")

    # 2. Bar chart showing the comparison of a numerical value across categories (e.g., average revenue per product)
    if 'Product' in df.columns and 'Revenue ($)' in df.columns:
        plt.figure(figsize=(10, 6))
        avg_revenue_by_product = df.groupby('Product')['Revenue ($)'].mean()
        avg_revenue_by_product.plot(kind='bar', color='skyblue')
        plt.title('Average Revenue by Product')
        plt.xlabel('Product')
        plt.ylabel('Average Revenue ($)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: Cannot create bar chart. The dataset does not contain the necessary columns ('Product' and 'Revenue ($)').")

    # 3. Histogram of a numerical column to understand its distribution (e.g., Distribution of Quantity Sold)
    if 'Quantity Sold' in df.columns:
        plt.figure(figsize=(8, 6))
        plt.hist(df['Quantity Sold'], bins=10, color='lightgreen', edgecolor='black')
        plt.title('Distribution of Quantity Sold')
        plt.xlabel('Quantity Sold')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: Cannot create histogram. The dataset does not contain the necessary column ('Quantity Sold').")

    # 4. Scatter plot to visualize the relationship between two numerical columns (e.g., Quantity Sold vs. Revenue)
    if 'Quantity Sold' in df.columns and 'Revenue ($)' in df.columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(df['Quantity Sold'], df['Revenue ($)'], alpha=0.7, color='salmon')
        plt.title('Quantity Sold vs. Revenue')
        plt.xlabel('Quantity Sold')
        plt.ylabel('Revenue ($)')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("Warning: Cannot create scatter plot. The dataset does not contain the necessary columns ('Quantity Sold' and 'Revenue ($)').")



if __name__ == "__main__":
    # Load and explore the dataset
    cleaned_df = load_and_explore_dataset()

    # Perform basic data analysis
    if cleaned_df is not None:
        analyze_data(cleaned_df)

        # Visualize the data
        visualize_data(cleaned_df)

        print("\nFurther analysis can be done with the cleaned dataframe.")

