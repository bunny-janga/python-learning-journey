# Day 31 – Pandas in Python

## 1. Introduction to Pandas

Pandas is a popular Python library used for data manipulation and data analysis.

It helps us work with structured data such as tables, CSV files, and Excel files.

In simple words, Pandas makes it easier to organize, read, filter, update, and clean data.

### Why Do We Use Pandas?

- To read data from CSV and Excel files.
- To organize data into rows and columns.
- To find missing values.
- To remove duplicate records.
- To filter and sort information.
- To perform data analysis.

### Installing Pandas

Before using Pandas, install it using the following command:

```bash
pip install pandas
```

### Importing Pandas

```python
import pandas as pd
```

Here, `pd` is the commonly used alias for Pandas.

## 2. Series in Pandas

A Series is a one-dimensional labeled data structure in Pandas.

It stores values along with their index labels.

In simple words, a Series is similar to a single column in a table.

### Creating a Series

```python
import pandas as pd

data = [10, 20, 30, 40, 50]

s = pd.Series(data)

print(s)
```

**Output:**

```text
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

Here:
- The left side represents index labels.
- The right side represents values.
- Pandas automatically creates index numbers starting from zero.

### Creating a Series with Custom Index

We can also provide our own index labels.

```python
import pandas as pd

marks = [85, 90, 75]

s = pd.Series(marks, index=["Rahul", "Priya", "John"])

print(s)
```

**Output:**

```text
Rahul    85
Priya    90
John     75
dtype: int64
```

### Accessing Series Elements

We can access values using their index labels.

```python
import pandas as pd

marks = pd.Series(
    [85, 90, 75],
    index=["Rahul", "Priya", "John"]
)

print(marks["Rahul"])
print(marks["John"])
```

**Output:**

```text
85
75
```

### Series Attributes

| Attribute | Purpose |
|---|---|
| `index` | Returns index labels |
| `values` | Returns stored values |
| `dtype` | Returns data type |
| `size` | Returns the number of elements |
| `shape` | Returns the dimensions |

**Example:**

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print("Values:", s.values)
print("Index:", s.index)
print("Data Type:", s.dtype)
print("Size:", s.size)
print("Shape:", s.shape)
```

## 3. DataFrames in Pandas

A DataFrame is a two-dimensional labeled data structure containing rows and columns.

It is similar to a table in Excel or a database.

We commonly use DataFrames to store and analyze structured information.

### Creating a DataFrame

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "John"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 75]
}

df = pd.DataFrame(data)

print(df)
```

**Output:**

```text
    Name  Age  Marks
0  Rahul   21     85
1  Priya   22     90
2   John   20     75
```

### Understanding the DataFrame

- Each row represents one student.
- Each column represents a particular type of information.
- The index identifies each row.
- The column names describe the stored data.

### Accessing DataFrame Columns

We can access a particular column using its name.

```python
print(df["Name"])
```

**Output:**

```text
0    Rahul
1    Priya
2     John
Name: Name, dtype: object
```

### Accessing Multiple Columns

```python
print(df[["Name", "Marks"]])
```

**Output:**

```text
    Name  Marks
0  Rahul     85
1  Priya     90
2   John     75
```

### Accessing Rows Using loc and iloc

**1. loc[]**

Used to access rows using index labels.

```python
print(df.loc[0])
```

**Output:**

```text
Name     Rahul
Age         21
Marks       85
Name: 0, dtype: object
```

**2. iloc[]**

Used to access rows using integer positions.

```python
print(df.iloc[1])
```

**Output:**

```text
Name     Priya
Age         22
Marks       90
Name: 1, dtype: object
```

### Important DataFrame Attributes

| Attribute | Purpose |
|---|---|
| `shape` | Returns rows and columns |
| `columns` | Returns column names |
| `index` | Returns row index |
| `dtypes` | Returns data types of columns |
| `size` | Returns total number of elements |
| `values` | Returns the underlying values |

**Example:**

```python
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Index:", df.index)
print("Data Types:")
print(df.dtypes)
print("Total Elements:", df.size)
```

### Useful DataFrame Methods

| Method | Purpose |
|---|---|
| `head()` | Displays the first 5 rows by default |
| `tail()` | Displays the last 5 rows by default |
| `info()` | Displays DataFrame information |
| `describe()` | Provides statistical summary of numeric columns |
| `sample()` | Displays random rows |

**Example:**

```python
print(df.head())
print(df.describe())
print(df.info())
```

## 4. Reading CSV Files in Pandas

CSV stands for Comma-Separated Values.

A CSV file stores data in a table-like format where values are separated by commas.

Example CSV content:

```text
Name,Age,Marks
Rahul,21,85
Priya,22,90
John,20,75
```

Pandas provides the `read_csv()` function to read CSV files.

### Reading a CSV File

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df)
```

**Output:**

```text
    Name  Age  Marks
0  Rahul   21     85
1  Priya   22     90
2   John   20     75
```

### Displaying the First Five Rows

```python
df = pd.read_csv("students.csv")

print(df.head())
```

### Displaying the Last Five Rows

```python
print(df.tail())
```

### Checking CSV File Information

```python
print(df.info())
```

### Finding Statistical Information

```python
print(df.describe())
```

### Selecting Specific Columns

```python
print(df["Name"])
```

### Filtering CSV Data

We can filter records based on conditions.

```python
high_marks = df[df["Marks"] >= 80]

print(high_marks)
```

**Output:**

```text
    Name  Age  Marks
0  Rahul   21     85
1  Priya  22     90
```

### Saving DataFrame into a CSV File

We can also save our DataFrame into a new CSV file.

```python
df.to_csv("output.csv", index=False)
```

Here:
- `output.csv` is the new file name.
- `index=False` prevents Pandas from saving the row index as an extra column.

## 5. Data Cleaning Basics

Data Cleaning is the process of finding and correcting problems in a dataset.

Real-world data is not always perfect. It may contain missing values, duplicate records, incorrect information, or inconsistent formats.

Before analyzing data, we should clean it properly.

### Common Data Cleaning Problems

1. Missing values.
2. Duplicate records.
3. Incorrect data.
4. Unnecessary columns.
5. Inconsistent text formats.

### 1. Detecting Missing Values

We use `isnull()` to identify missing values.

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", None, "John"],
    "Marks": [85, None, 75, 90]
}

df = pd.DataFrame(data)

print(df.isnull())
```

**Output:**

```text
    Name  Marks
0  False  False
1  False   True
2   True  False
3  False  False
```

Here, `True` indicates a missing value.

### 2. Counting Missing Values

```python
print(df.isnull().sum())
```

**Output:**

```text
Name     1
Marks    1
dtype: int64
```

### 3. Removing Missing Values

The `dropna()` method removes rows containing missing values.

```python
cleaned_df = df.dropna()

print(cleaned_df)
```

**Output:**

```text
    Name  Marks
0  Rahul   85.0
3   John   90.0
```

**Note:** `dropna()` returns a cleaned DataFrame without changing the original DataFrame unless the result is assigned or an appropriate in-place operation is used.

### 4. Filling Missing Values

Instead of removing missing values, we can replace them using `fillna()`.

```python
df["Marks"] = df["Marks"].fillna(0)

print(df)
```

**Output:**

```text
    Name  Marks
0  Rahul   85.0
1  Priya    0.0
2   None   75.0
3   John   90.0
```

We can also fill missing numeric values using the column average.

```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

### 5. Removing Duplicate Records

Sometimes the same record appears more than once.

We can use `duplicated()` to identify duplicate rows and `drop_duplicates()` to remove them.

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Rahul"],
    "Marks": [85, 90, 85]
}

df = pd.DataFrame(data)

print(df.drop_duplicates())
```

**Output:**

```text
    Name  Marks
0  Rahul     85
1  Priya     90
```

### 6. Renaming Columns

We can change column names using `rename()`.

```python
df = df.rename(columns={"Name": "Student_Name"})

print(df)
```

### 7. Removing Unnecessary Columns

We can remove columns that are not needed for our analysis.

```python
df = df.drop(columns=["Marks"])

print(df)
```

### 8. Changing Data Types

Sometimes a column contains values in the wrong data type.

We can use `astype()` to convert the data type.

```python
import pandas as pd

df = pd.DataFrame({
    "Age": ["21", "22", "20"]
})

df["Age"] = df["Age"].astype(int)

print(df.dtypes)
```

**Output:**

```text
Age    int64
dtype: object
```

## 6. Mini Project – Student Data Cleaning

Let's apply the Pandas concepts in a small real-world example.

Our goal is to create a student dataset, identify missing values, remove duplicates, fill missing marks, and display the cleaned data.

### Complete Program

```python
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "John", "Rahul", None],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, None, 75, 85, 90]
}

df = pd.DataFrame(data)

print("Original Student Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing names
df["Name"] = df["Name"].fillna("Unknown")

# Fill missing marks with average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Student Data:")
print(df)

print("\nStudent Statistics:")
print(df.describe())
```

### Sample Output

```text
Original Student Data:
    Name  Age  Marks
0  Rahul   21   85.0
1  Priya   22    NaN
2   John   20   75.0
3  Rahul   21   85.0
4   None   23   90.0

Missing Values:
Name     1
Age      0
Marks    1

Cleaned Student Data:
      Name  Age  Marks
0    Rahul   21   85.0
1    Priya   22   83.333333
2     John   20   75.0
4  Unknown   23   90.0
```

The average used to fill the missing mark is calculated from the available marks: `(85 + 75 + 90) / 3 = 83.33`.

## 7. How to Install and Run Pandas in VS Code

1. Open Visual Studio Code.
2. Create a Python file named `pandas_basics.py`.
3. Open the terminal.
4. Install Pandas:

```bash
pip install pandas
```

5. Import Pandas:

```python
import pandas as pd
```

6. Write your program and save the file.
7. Run the program:

```bash
python pandas_basics.py
```

**For CSV examples:** Keep `students.csv` in the same folder as your Python file, or provide its correct file path.

## 8. What I Learned Today

After completing Day 31, I understood:

- What Pandas is and why it is used.
- How to create and work with Series.
- How to create and access DataFrames.
- How to read and write CSV files.
- How to select and filter data.
- How to identify missing values.
- How to remove duplicate records.
- How to fill missing values.
- How to rename columns and change data types.
- How to clean a student dataset using Pandas.

## 9. Day 31 – Quick Revision

| Function / Method | Purpose |
|---|---|
| `pd.Series()` | Creates a Series |
| `pd.DataFrame()` | Creates a DataFrame |
| `pd.read_csv()` | Reads a CSV file |
| `df.to_csv()` | Saves data into a CSV file |
| `df.head()` | Displays the first rows |
| `df.tail()` | Displays the last rows |
| `df.info()` | Displays DataFrame information |
| `df.describe()` | Displays statistical summary |
| `df.loc[]` | Accesses rows using labels |
| `df.iloc[]` | Accesses rows using positions |
| `df.isnull()` | Checks missing values |
| `df.dropna()` | Removes rows with missing values |
| `df.fillna()` | Fills missing values |
| `df.drop_duplicates()` | Removes duplicate rows |
| `df.rename()` | Renames columns |
| `df.astype()` | Changes data types |

**Day 31 completed: Pandas Series, DataFrames, CSV Files and Data Cleaning Basics.**
