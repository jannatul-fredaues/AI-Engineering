import numpy as np

try:
    # Get user input for vectors
    v1 = np.array([float(x) for x in input("Enter Vector 1 (space-separated): ").split()])
    v2 = np.array([float(x) for x in input("Enter Vector 2 (space-separated): ").split()])

    if v1.shape != v2.shape:
        print("Error: Vectors must be the same length for a dot product.")
    else:
        # Calculate dot product
        result = np.dot(v1, v2)
        
        print("-" * 20)
        print(f"Vector 1: {v1}")
        print(f"Vector 2: {v2}")
        print(f"Dot Product: {result}")

except ValueError:
    print("Invalid input! Please enter numbers only.")