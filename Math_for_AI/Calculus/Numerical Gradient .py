import numpy as np

# Sample data (e.g., y = x^2)
x = np.array([0, 1, 2, 3, 4])
y = x**2

# Compute gradient (change in y / change in x)
# Default spacing is 1
grad = np.gradient(y) 
print(grad) # Output: [1. 2. 4. 6. 7.] (approximate derivatives)
