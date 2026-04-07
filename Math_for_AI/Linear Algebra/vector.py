import numpy as np

# 1. Take user input for two vectors
try:
    v1_input = input("Enter components of Vector 1 (space-separated): ").split()
    v2_input = input("Enter components of Vector 2 (space-separated): ").split()

    # Convert strings to numpy arrays (floats)
    v1 = np.array([float(x) for x in v1_input])
    v2 = np.array([float(x) for x in v2_input])

    if v1.shape != v2.shape:
        print("Error: Vectors must have the same number of components!")
    else:
        # 2. Basic Operations
        print(f"\nVector 1: {v1}")
        print(f"Vector 2: {v2}")
        print(f"Addition (v1 + v2): {v1 + v2}")
        print(f"Subtraction (v1 - v2): {v1 - v2}")
        print(f"Scalar Multiplication (v1 * 2): {v1 * 2}")

except ValueError:
    print("Invalid input! Please enter numbers only.")