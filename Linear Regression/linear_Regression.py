import numpy as np  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

np.random.seed(34)

# Generate syntetic data
x = 2 * np.random.rand(100,1) # Generate 100 random numbers between 0 and 2
y = 4 + 4 * x + np.random.randn(100, 1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=500)

print(X_train)