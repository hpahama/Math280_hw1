# Applied Homework Assignment 1: A First Look at Principal Component Analysis

## TASK 1:
Load the timbers2024 dataset into Python, or pick your own dataset you like. Pick two variables you think might be correlated, and make a scatterplot of them.

### 1. Install Required Libraries  
Before running the code, install the necessary libraries:

```sh
#-------Step 1
pip install pandas matplotlib
```

### 2. Load the Dataset  
Use `pandas` to read the CSV file:  

```python
#-------Step 2
import pandas as pd

file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path)
```

### 3. Handling Encoding Errors  
If the first attempt gives an encoding error, try specifying `latin1`:

```python
#-------Step 3
import pandas as pd

file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')
```

### 4. Verify Data Load  
Check if the dataset loaded correctly by displaying the first few rows:

```Python
#-------Step 4
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')

print(df.head())
```

### 5. Creating the Scatterplot
Here basically I chose the variables that are the G-PK_per90 and G+A-PK_per90 because I thought it would be interesting to see if they're correlational. So we defined the x and y and used pyplot to create the scatterplot:

```python
#-------Step 5
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')

# Select two variables to plot
x = df['G-PK_per90']
y = df['G+A-PK_per90']

# Create a scatter plot
plt.scatter(x, y)
plt.xlabel('Goals per 90 minutes (G-PK_per90)')
plt.ylabel('Goals + Assists per 90 minutes (G+A-PK_per90)')
plt.title('Scatter plot of Goals vs Goals + Assists per 90 minutes')
plt.show()
```

### 6. Line of Best-Fit 
(Unecessary but I just wanted to see the trend)
I recall reading something in my rstudio code book (Intro to Data Science using R) and it talked about trends and how the line of best-fit would help make it easier for us to visualize and actually have a more precise conclusion about the trend. Here I calculated the line using the linear regression line formula y=mx+b, and then used polyfit:

```python
#-------Step 6
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r"C:\Users\paham\Downloads\timbers2024.csv"
df = pd.read_csv(file_path, encoding='latin1')

x = df['G-PK_per90']
y = df['G+A-PK_per90']

plt.scatter(x, y, color='cornflowerblue', label='Data points')

# Calculate the best fit line
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label='Best fit line')

# Add labels and title
plt.xlabel('Goals per 90 minutes (G-PK_per90)')
plt.ylabel('Goals + Assists per 90 minutes (G+A-PK_per90)')
plt.title('Scatter plot of Goals vs Goals + Assists per 90 minutes')
plt.legend()
plt.show()
```
Note:
For reference look at Scatterplot_sBestFit.png
