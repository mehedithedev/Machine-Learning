import numpy as np
import matplotlib.pyplot as plt

# Example dataset with outliers

data = [2, 4, 6, 8, 12, 14,16, 200]

# Calcualate first and third quartiles 

q1 = np.percentile(data, 20)
q2 = np.percentile(data, 80)

# Calculate Interquartile Range (IQR)

iqr = q2 - q1

print(q1, q2, iqr)

# Define upper and lower bounds for outliers

lower_bound = q1 - 1.5 * iqr
upper_bound = q2 + 1.5 * iqr

# Identify outliers
outliers = [value for value in data if value < lower_bound or value > upper_bound]

print(f"Outliers in the dataset: {outliers}")


# Plotting the data

plt.xlabel("Data")
plt.ylabel("Values")

plt.title("Outliers in the dataset")

plt.scatter(lower_bound, upper_bound, color='red', label='Outliers')
plt.show()

