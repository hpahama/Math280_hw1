import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Load Dataset
file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')

# 2. Select Three Variables (using 'G+A_per90' as the third variable)
data = df[['G-PK_per90', 'G+A-PK_per90', 'G+A_per90']].to_numpy()

# 3. Normalize the Guess Unit Vector
# Initial guess unit vector for 3 dimensions normalized
v = np.array([1, 1, 1]) / np.linalg.norm([1, 1, 1])

# Function to calculate total variation in the direction of v
def calculate_variation(data, vector):
    return np.sum(np.dot(data, vector))

# 4. Calculate Total Variation for Initial Vector
initial_variation = calculate_variation(data, v)
print("Initial variation for unit vector v:", initial_variation)

# 5. Try Other Unit Vectors
unit_vectors = [
    np.array([1, 0, 0]),
    np.array([0, 1, 0]),
    np.array([0, 0, 1]),
    np.array([1, 1, 1]) / np.linalg.norm([1, 1, 1])
]

# Calculate variations for each unit vector
variations = [calculate_variation(data, vec) for vec in unit_vectors]

# Identify the best unit vector
best_vector = unit_vectors[np.argmax(variations)]
print("Best unit vector:", best_vector)

# 6. Plot 3D Scatterplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data[:, 0], data[:, 1], data[:, 2], color='blue', label='Data Points')

# Create the line using the best unit vector
line_x = np.linspace(min(data[:, 0]), max(data[:, 0]), 100)
line_y = (best_vector[1] / best_vector[0]) * line_x
line_z = (best_vector[2] / best_vector[0]) * line_x

# Plot the line
ax.plot(line_x, line_y, line_z, color='red', label='Line Spanned by v')

# 7. Add labels and legend
ax.set_xlabel('G-PK_per90')
ax.set_ylabel('G+A-PK_per90')
ax.set_zlabel('G+A_per90')  # Updated column label
ax.set_title('3D Scatterplot with Line Spanned by v')
ax.legend()

# Show plot
plt.show()
