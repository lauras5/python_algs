# code to verify that the numpy norm method gives accurate results
import numpy as np

def calculate_norm(vector):
    """Calculate the Euclidean norm of a vector."""
    squared_sum = sum(x ** 2 for x in vector)
    return np.sqrt(squared_sum)

vector = np.array([3, 4, 5])
# Numpy result
norm_np = np.linalg.norm(vector)
# Manual result
norm_manual = calculate_norm(vector)

# Verify result
if np.isclose(norm_np, norm_manual):
    print("np.linalg.norm gives the expected result.")
else:
    print("np.linalg.norm does not give the expected result.")
