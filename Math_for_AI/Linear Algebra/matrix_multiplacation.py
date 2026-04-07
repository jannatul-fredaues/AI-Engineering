import numpy as np

def get_matrix(name):
    r = int(input(f"Enter rows for Matrix {name}: "))
    c = int(input(f"Enter columns for Matrix {name}: "))
    print(f"Enter {r*c} elements separated by spaces:")
    elements = list(map(float, input().split()))
    return np.array(elements).reshape(r, c)

try:
    mat_A = get_matrix("A")
    mat_B = get_matrix("B")

    if mat_A.shape[1] != mat_B.shape[0]:
        print(f"\nError: Matrix A columns ({mat_A.shape[1]}) must match Matrix B rows ({mat_B.shape[0]})!")
    else:
        result = mat_A @ mat_B
        print("\nResulting Matrix:")
        print(result)
        print(f"New Shape: {result.shape}")

except Exception as e:
    print(f"An error occurred: {e}")