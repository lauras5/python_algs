import numpy as np

def cosine_similarity(u, v):
    """Compute the cosine similarity between two vectors."""
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    return dot_product / (norm_u * norm_v)

vect_1 = np.array([1, 0, -1, 2])
vect_2 = np.array([3, 1, 0, 1])

# Compute cosine similarity
cosine_angle = cosine_similarity(vect_1, vect_2)

# Compute angle in degrees
angle_degrees = np.arccos(cosine_angle) * 180 / np.pi

print("Cosine similarity between u and v:", cosine_angle)  # .615
print("Angle between u and v in degrees:", angle_degrees)  # 52.015
