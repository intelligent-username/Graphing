import matplotlib.pyplot as plt
import numpy as np

transformations = [
    {"prob": 0.01, "coeffs": [0, 0, 0, 0.16, 0, 0]},
    {"prob": 0.85, "coeffs": [0.85, 0.04, -0.04, 0.85, 0, 1.6]},
    {"prob": 0.07, "coeffs": [0.2, -0.26, 0.23, 0.22, 0, 1.6]},
    {"prob": 0.07, "coeffs": [-0.15, 0.28, 0.26, 0.24, 0, 0.44]},
]

# Initial point
x, y = 0, 0

iterations = 100000

# Lists to store points
x_points = []
y_points = []

# Function to apply the affine transformation
def apply_transformation(transformation, x, y):
    a, b, c, d, e, f = transformation
    x_new = a * x + b * y + e
    y_new = c * x + d * y + f
    return x_new, y_new

# Chaos Game for Barnsley Fern
for _ in range(iterations):
    # Choose a random transformation based on the probabilities
    r = np.random.rand()
    cumulative_prob = 0
    for transform in transformations:
        cumulative_prob += transform["prob"]
        if r <= cumulative_prob:
            x, y = apply_transformation(transform["coeffs"], x, y)
            break
    x_points.append(x)
    y_points.append(y)

# Plotting the points
plt.figure(figsize=(6, 10))
plt.plot(x_points, y_points, 'g.', markersize=0.1)
plt.title("Barnsley Fern")
plt.show()
