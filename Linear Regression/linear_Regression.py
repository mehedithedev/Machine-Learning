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

model = LinearRegression()
model.fit(X_train, y_train)

y_prediction = model.predict(X_test)

print("Predicting Y",y_prediction)

mse = mean_squared_error(y_test, y_pred=y_prediction)

print(mse)
print("Mean Squared value", mse)

plt.scatter(X_test, y_test, color = 'blue')
plt.plot(X_test, y_prediction, color= "red")
plt.xlabel("X")
plt.ylabel("Y")
plt.title(mse)
plt.show()

