import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(df):
    """
    Visualizes key aspects of a sales dataset.

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
    # Create a sample DataFrame to run the visualization
    data = {
        'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-02', '2023-01-03']),
        'Product': ['A', 'B', 'A', 'B', 'A'],
        'Quantity Sold': [10, 5, 12, 8, 15],
        'Revenue ($)': [100, 75, 120, 120, 150]
    }
    sample_df = pd.DataFrame(data)
    visualize_data(sample_df)