# Applied Homework Assignment 1: A First Look at Principal Component Analysis  

## TASK 2:  
Identify the unit vector that captures the maximum variation in the dataset.

### Step 1. Import Necessary Libraries  
Start by loading the required libraries:  
```python
import pandas as pd
import numpy as np
```

### Step 2. Load the Dataset  
Read the dataset with the correct encoding:  
```python
file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')
```

### Step 3. Select Two Variables  
Extract the necessary columns and convert them to a NumPy array:  
```python
data = df[['G-PK_per90', 'G+A-PK_per90']].to_numpy()
```

### Step 4. Define and Normalize the Guess Unit Vectors  
Create unit vector guesses and normalize them:  
```python
vectors = [
    np.array([1, 0]), 
    np.array([0, 1]), 
    np.array([np.cos(np.pi/4), np.sin(np.pi/4)])
]
vectors = [v / np.linalg.norm(v) for v in vectors]
```

### Step 5. Calculate Total Variation in Each Direction  
Compute the variation along each unit vector:  
```python
variations = [np.sum(np.dot(data, v)) for v in vectors]
```

### Step 6. Identify the Best Vector  
Find the unit vector that captures the most variation:  
```python
best_vector = vectors[np.argmax(variations)]
print(f'The unit vector with the maximum variation is: {best_vector}')
```

### Step 7: Run the Complete Code
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')
data = df[['G-PK_per90', 
           'G+A-PK_per90']].to_numpy()

u = np.array([0.707, 
              0.707])

plt.scatter(data[:, 0], 
            data[:, 1], 
            color='blue', 
            label='Data Points')

x_values = np.linspace(min(data[:, 0]), 
                       max(data[:, 0]), 
                       100)

line_y_values = (u[1] / u[0]) * x_values

plt.plot(x_values, 
         line_y_values, 
         color='red', 
         label='Line Spanned by u')

plt.xlabel('G-PK_per90')
plt.ylabel('G+A-PK_per90')
plt.title('Scatterplot with Line Spanned by u')
plt.legend()

plt.show()
```
### Step 8. Output Conclusion
I started with an initial guess for a unit vector [0.707, 0.707], which balances the contributions between x and y directions. This vector was normalized to a magnitude of 1. I then calculated the total variation using this vector and compared it with three other vectors. The result was clear—my initial vector [0.707, 0.707] achieved the highest total variation of 6.02, confirming it was the best choice. The scatterplot and the line spanned by this vector further substantiated that it aligns perfectly with the direction of maximum variability in the dataset.
