# Applied Homework Assignment 1: A First Look at Principal Component Analysis

## TASK 2:
Using guess and check, find a unit vector ⃗v that points in a direction close to the direction of maximum variation of your scatterplot from problem 1. Using Python, find the total variability of your dataset in the direction of ⃗v using the Python code sum(np.dot(dataset[[’variable1’,’variable2’]],vector)). Check that you’ve found a good unit vector ⃗v by trying three other unit vectors and verifying that your vector has a larger total variation. Report your findings.

### Step 1: Import Libraries and Load Data
Start by importing the necessary libraries and reading the data from the CSV file.

```python
import pandas as pd
import numpy as np

file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')

data = df[['G-PK_per90', 'G+A-PK_per90']].to_numpy()
```

### Step 2: Initial Guess for Unit Vector
Make an initial guess for the unit vector `v` and normalize it to ensure it is indeed a unit vector.

```python
# Initial guess for unit vector v
v = np.array([0.5, 0.5])
v = v / np.linalg.norm(v)
```

### Step 3: Calculate Total Variation
Define a function to calculate the total variation in the direction of the unit vector `v` and compute the total variation for the initial guess.

```python
# Function to calculate total variation in the direction of v
def calculate_variation(data, vector):
    return np.sum(np.dot(data, vector))

# Initial total variation
initial_variation = calculate_variation(data, v)
print("Total variation for initial unit vector v:", initial_variation)
```

### Step 4: Compare with Other Unit Vectors
Generate three additional unit vectors and compare their total variations with the initial guess.

```python
# Other unit vectors to try
unit_vectors = [
    np.array([1, 0]),
    np.array([0, 1]),
    np.array([0.707, 0.707])  # This is approximately [1, 1] normalized
]

# Calculate and print total variation for each vector
for idx, vec in enumerate(unit_vectors):
    variation = calculate_variation(data, vec)
    print(f"Total variation for unit vector {idx + 1}:", variation)
```

### Step 5: Output conclusion
Carefully compare the total variations and determine which unit vector provides the maximum variation in the data.

- Total variation for the initial unit vector `v`: 6.02
- Total variation for unit vector 1: 3.10
- Total variation for unit vector 2: 5.42
- Total variation for unit vector 3: 6.02
```
Answer:
My initial guess for the unit vector `v` ([0.707, 0.707]) was good, achieving the highest variation. This vector evenly splits between x and y directions, normalized to a magnitude of 1 by dividing `[1, 1]` by `√2`.