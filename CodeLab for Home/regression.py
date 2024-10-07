import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data 

x = np.array([1,2,3,4,5]).reshape(-1, 1)
y = np.array([2,4,5,4,5])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Based on the model predict values for y

y_pred = model.predict(x)

# Plot the original data and the regression line

plt.scatter(x, y, label= 'Original Data')
# Plotting the regression line with preddicted value of y
plt.plot(x, y_pred, color='red', label='Regerssion line')
# Adding labels and title
plt.xlabel('Independ Variable (X)')
plt.ylabel('Dependent Variable (Y)')
plt.title('Simple Linear Regression')

# Plot the legend
plt.legend()
# Display the plot
plt.show()