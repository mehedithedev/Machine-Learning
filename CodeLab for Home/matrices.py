import numpy as np
# Creating matrices 
matrix_a = np.matrix(
    [
        [1,2,3],[4,5,6], [7,8,9]
    ]
    )

matrix_b = np.matrix(
    [
        [9,8,7],[6,5,4], [3,2,1]
    ]
    )

# Displaying matrices
print("MatrixA: ", matrix_a)
print("\nMatrix B :", matrix_b)

# Matrix addition: 
addition_result = matrix_a+ matrix_b

print("\nmatrix Addition (A+B): ")
print(addition_result)

# Matrix multiplication
multiplication_result = np.dot(matrix_a, matrix_b)
print("\nMatrix Multiplication (A*B): ")
print(multiplication_result)
