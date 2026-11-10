# Day 30 – Data Analysis and NumPy in Python

## 1. Introduction to Data Analysis

Data Analysis is the process of collecting, organizing, cleaning, and examining data to find useful information and make better decisions.

In simple words, data analysis helps us understand what the data is telling us.

### Real-World Examples

- **Education:** Analyzing student marks to identify performance.
- **Business:** Understanding sales and customer behavior.
- **Healthcare:** Studying patient records and medical data.
- **Banking:** Analyzing transactions and spending patterns.
- **Sports:** Comparing player performance and statistics.

### Steps in Data Analysis

1. **Data Collection:** Gathering data from different sources.
2. **Data Cleaning:** Removing incorrect, duplicate, or missing data.
3. **Data Organization:** Arranging data in a useful format.
4. **Data Analysis:** Performing calculations and identifying patterns.
5. **Data Visualization:** Presenting information using charts and graphs.
6. **Decision Making:** Using the results to make informed decisions.

### Popular Python Libraries for Data Analysis

| Library | Purpose |
|---|---|
| NumPy | Numerical calculations and array operations |
| Pandas | Data manipulation and analysis |
| Matplotlib | Creating charts and graphs |
| Seaborn | Statistical data visualization |
| SciPy | Scientific and mathematical calculations |

### Why Python for Data Analysis?

Python is popular for data analysis because:

- It has simple and readable syntax.
- It provides powerful libraries.
- It can handle large amounts of data efficiently.
- It supports data visualization.
- It is widely used in Data Science and Machine Learning.

## 2. NumPy Basics

NumPy stands for **Numerical Python**.

It is a popular Python library used for numerical calculations and working with multidimensional arrays.

NumPy provides powerful tools for performing mathematical operations on large collections of numbers.

### Installing NumPy

Before using NumPy, we need to install it.

Open the VS Code terminal and run:

```bash
pip install numpy
```

### Importing NumPy

After installation, import the library into your Python program.

```python
import numpy as np
```

Here, `np` is the commonly used alias for NumPy.

### Example 1: Creating a NumPy Array

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

**Output:**

```text
[10 20 30 40 50]
```

### Example 2: NumPy Array vs Python List

Python lists and NumPy arrays both store multiple values, but NumPy arrays are designed for efficient numerical operations.

**Python List:**

```python
numbers = [10, 20, 30]

print(numbers * 2)
```

**Output:**

```text
[10, 20, 30, 10, 20, 30]
```

**NumPy Array:**

```python
import numpy as np

numbers = np.array([10, 20, 30])

print(numbers * 2)
```

**Output:**

```text
[20 40 60]
```

In a NumPy array, multiplication by 2 multiplies every element by 2.

### Advantages of NumPy

- Faster numerical operations for many data workloads.
- Supports multidimensional arrays.
- Provides mathematical functions.
- Uses memory efficiently for homogeneous numerical data.
- Makes array calculations easier.

## 3. Arrays in NumPy

An array is a collection of elements stored in an organized structure.

NumPy supports different types of arrays based on their dimensions.

### 1. One-Dimensional Array (1D)

A one-dimensional array contains elements in a single row.

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
print(arr.ndim)
```

**Output:**

```text
[10 20 30 40]
1
```

Here, `ndim` returns the number of dimensions.

### 2. Two-Dimensional Array (2D)

A two-dimensional array contains rows and columns.

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr)
print(arr.ndim)
```

**Output:**

```text
[[10 20 30]
 [40 50 60]]
2
```

### 3. Three-Dimensional Array (3D)

A three-dimensional array contains multiple two-dimensional arrays.

```python
import numpy as np

arr = np.array([
    [[10, 20], [30, 40]],
    [[50, 60], [70, 80]]
])

print(arr)
print(arr.ndim)
```

**Output:**

```text
[[[10 20]
  [30 40]]

 [[50 60]
  [70 80]]]
3
```

### Important NumPy Array Attributes

NumPy provides useful attributes to understand an array.

| Attribute | Purpose |
|---|---|
| `ndim` | Returns the number of dimensions |
| `shape` | Returns the size of each dimension |
| `size` | Returns the total number of elements |
| `dtype` | Returns the data type of elements |
| `itemsize` | Returns the size of one element in bytes |

### Example: Array Attributes

```python
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
print("Item Size:", arr.itemsize)
```

**Output:**

```text
Dimensions: 2
Shape: (2, 3)
Size: 6
Data Type: int64
Item Size: 8
```

*Note: The data type and item size can vary depending on the system and NumPy configuration.*

### Creating Special Arrays

NumPy provides built-in functions to create arrays easily.

**1. np.zeros()**

Creates an array filled with zeros.

```python
import numpy as np

arr = np.zeros(5)

print(arr)
```

**Output:**

```text
[0. 0. 0. 0. 0.]
```

**2. np.ones()**

Creates an array filled with ones.

```python
arr = np.ones(4)

print(arr)
```

**Output:**

```text
[1. 1. 1. 1.]
```

**3. np.arange()**

Creates an array containing values within a specified range.

```python
arr = np.arange(1, 10)

print(arr)
```

**Output:**

```text
[1 2 3 4 5 6 7 8 9]
```

**4. np.linspace()**

Creates evenly spaced values between a starting and ending point.

```python
arr = np.linspace(1, 10, 5)

print(arr)
```

**Output:**

```text
[ 1.    3.25  5.5   7.75 10.  ]
```

**5. np.eye()**

Creates an identity matrix with ones on the main diagonal and zeros elsewhere.

```python
arr = np.eye(3)

print(arr)
```

**Output:**

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

## 4. Operations on NumPy Arrays

NumPy allows us to perform mathematical operations directly on arrays without writing separate loops.

### 1. Arithmetic Operations

We can perform addition, subtraction, multiplication, and division.

**Addition:**

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
```

**Output:**

```text
[11 22 33]
```

**Subtraction:**

```python
print(a - b)
```

**Output:**

```text
[ 9 18 27]
```

**Multiplication:**

```python
print(a * b)
```

**Output:**

```text
[10 40 90]
```

**Division:**

```python
print(a / b)
```

**Output:**

```text
[10. 10. 10.]
```

These operations are performed element by element for arrays with compatible shapes.

### 2. Mathematical Operations

NumPy provides built-in mathematical functions.

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))
```

**Output:**

```text
Sum: 100
Mean: 25.0
Maximum: 40
Minimum: 10
Standard Deviation: 11.180339887498949
```

### 3. Array Indexing

Indexing is used to access individual elements from an array.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])
```

**Output:**

```text
10
30
50
```

Remember: Array indexing starts from zero.

### 4. Array Slicing

Slicing is used to access a selected portion of an array.

**Syntax:**

```python
array[start:stop:step]
```

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[::2])
```

**Output:**

```text
[20 30 40]
[10 20 30]
[10 30 50]
```

### 5. Comparison Operations

NumPy supports comparison operators such as greater than, less than, and equal to.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr > 25)
print(arr == 30)
```

**Output:**

```text
[False False  True  True  True]
[False False  True False False]
```

### 6. Boolean Indexing

Boolean indexing helps us select elements based on a condition.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 25]

print(result)
```

**Output:**

```text
[30 40 50]
```

### 7. Reshaping an Array

The `reshape()` function changes the shape of an array without changing its elements.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

result = arr.reshape(2, 3)

print(result)
```

**Output:**

```text
[[1 2 3]
 [4 5 6]]
```

The total number of elements must remain the same when reshaping.

### 8. Transpose of an Array

Transpose changes rows into columns and columns into rows.

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)
```

**Output:**

```text
[[1 4]
 [2 5]
 [3 6]]
```

### 9. Joining Arrays

The `concatenate()` function combines arrays.

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))

print(result)
```

**Output:**

```text
[10 20 30 40 50 60]
```

## 5. Real-World Example: Student Marks Analysis Using NumPy

Let's use NumPy to analyze student marks.

```python
import numpy as np

marks = np.array([85, 90, 75, 60, 95])

print("Student Marks:", marks)

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

passed = marks[marks >= 40]

print("Passed Students' Marks:", passed)
```

**Output:**

```text
Student Marks: [85 90 75 60 95]
Total Marks: 405
Average Marks: 81.0
Highest Marks: 95
Lowest Marks: 60
Passed Students' Marks: [85 90 75 60 95]
```

This example shows how NumPy can help us analyze numerical data easily.

## 6. How to Install and Run NumPy in VS Code

1. Open Visual Studio Code.
2. Create a Python file named `numpy_basics.py`.
3. Open the terminal.
4. Install NumPy:

```bash
pip install numpy
```

5. Import NumPy:

```python
import numpy as np
```

6. Write your program and save the file.
7. Run it using:

```bash
python numpy_basics.py
```

If you use a virtual environment, make sure NumPy is installed in the same environment selected by VS Code.

## 7. What I Learned Today

After completing Day 30, I understood:

- What Data Analysis means and why it is important.
- Different steps involved in Data Analysis.
- Popular Python libraries used for Data Analysis.
- What NumPy is and how to install it.
- How to create one-dimensional, two-dimensional, and three-dimensional arrays.
- How to use NumPy array attributes.
- How to perform arithmetic and mathematical operations.
- How to use indexing and slicing.
- How to reshape and transpose arrays.
- How to analyze student marks using NumPy.

## 8. Day 30 – Quick Revision

| Function / Attribute | Purpose |
|---|---|
| `np.array()` | Creates an array |
| `np.zeros()` | Creates an array filled with zeros |
| `np.ones()` | Creates an array filled with ones |
| `np.arange()` | Creates values within a range |
| `np.linspace()` | Creates evenly spaced values |
| `np.eye()` | Creates an identity matrix |
| `np.sum()` | Calculates the sum |
| `np.mean()` | Calculates the average |
| `np.max()` | Finds the maximum value |
| `np.min()` | Finds the minimum value |
| `np.reshape()` | Changes the array shape |
| `np.concatenate()` | Combines arrays |
| `ndim` | Returns the number of dimensions |
| `shape` | Returns the array shape |
| `size` | Returns the total number of elements |

**Day 30 completed: Introduction to Data Analysis and NumPy Basics.**
