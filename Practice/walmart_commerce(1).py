# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading a CSV file into a DataFrame using pandas
# The delimiter parameter specifies that the columns in the CSV are separated by semicolons
# The quotechar parameter specifies that double quotes are used to enclose fields
df = pd.read_csv('/kaggle/input/walmart-commerce-data/WalmartSQL repository..csv', delimiter=';', quotechar='"')

# Displaying the first few rows of the DataFrame to inspect the column names and data
print(df.head())

# Plotting total sales by customer_type if the 'customer_type' column exists
if 'customer_type' in df.columns:
    # Creating a bar plot
    plt.figure(figsize=(10, 6))
    # Grouping the data by 'customer_type' and summing the 'total' column for each group
    df.groupby('customer_type')['total'].sum().plot(kind='bar', color='skyblue')
    # Adding title and labels to the plot
    plt.title('Total Sales by Customer Type')
    plt.xlabel('Customer Type')
    plt.ylabel('Total Sales')
    # Displaying the plot
    plt.show()
else:
    # Printing a message if the 'customer_type' column is not found
    print("Column 'customer_type' not found in the dataset.")

# Plotting total sales by gender if the 'gender' column exists
if 'gender' in df.columns:
    # Creating a bar plot
    plt.figure(figsize=(10, 6))
    # Grouping the data by 'gender' and summing the 'total' column for each group
    df.groupby('gender')['total'].sum().plot(kind='bar', color='lightcoral')
    # Adding title and labels to the plot
    plt.title('Total Sales by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Total Sales')
    # Displaying the plot
    plt.show()
else:
    # Printing a message if the 'gender' column is not found
    print("Column 'gender' not found in the dataset.")

# Plotting total spent on each product_line if the 'product_line' column exists
if 'product_line' in df.columns:
    # Creating a bar plot
    plt.figure(figsize=(14, 6))
    # Grouping the data by 'product_line' and summing the 'total' column for each group
    df.groupby('product_line')['total'].sum().plot(kind='bar', color='lightgreen')
    # Adding title and labels to the plot
    plt.title('Total Spent on Each Product Line')
    plt.xlabel('Product Line')
    plt.ylabel('Total Sales')
    # Displaying the plot
    plt.show()
else:
    # Printing a message if the 'product_line' column is not found
    print("Column 'product_line' not found in the dataset.")
