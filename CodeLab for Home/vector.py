import numpy as np
# Creating vectors

vector_a = np.array([1,2,3,4,5])
vector_b = np.array([6,7,8,9,10])

# Displaying vectors
print("Vector A: ", vector_a)
print("\nVector B: ", vector_b)

# Vector addition
addition_result = vector_a + vector_b
print("\nVector Addition (A+B): ")
print(addition_result)

# Vector dot product
dot_product_result = np.dot(vector_a, vector_b)
print("\nVector Dot Product (A.B): ")
print(dot_product_result)