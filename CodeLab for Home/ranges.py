import numpy as np
data = [2,4,6,8,10, 12, 14, 16, 18, 20] 

# using the numpy library to calculate range
range_np = np.ptp(data)

print(f"Range using numpy library: {range_np}")