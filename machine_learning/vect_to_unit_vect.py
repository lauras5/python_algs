import numpy as np

def normalize_vector(v):
    """Convert a vector to a unit vector."""
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

vector = np.array([3, 4, 5])

unit_vector = normalize_vector(vector)

print("Original vector:", vector)
print("Unit vector:", unit_vector)
