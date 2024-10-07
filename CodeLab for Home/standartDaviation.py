import numpy as np

data = [2, 4, 6, 8, 12, 14,16]

data_with_nan = [92, 4, 6, 8, 12, 200, 14,16]

# Calculate standard deviation
std_dev = np.std(data, ddof=1)

# Explaninig ddof : ddof or 'Delta degrees of freedom' is a prameterused in the calculation of the standart deviation, a measeure of how spread out or despresed values are in a set of data

nan_std_dev = np.std(data_with_nan, ddof=0)

print(std_dev)
print(nan_std_dev)