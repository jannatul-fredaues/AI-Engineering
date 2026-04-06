import numpy as np

# Taking user input for a 2x2 matrix
print("Enter elements for a 2x2 matrix row by row:")
row1 = [float(x) for x in input("Row 1 (space separated): ").split()]
row2 = [float(x) for x in input("Row 2 (space separated): ").split()]

A = np.array([row1, row2])
print("\nMatrix A:\n", A)