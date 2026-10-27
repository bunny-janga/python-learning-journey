# Day 17: Python Modules

## 1. Introduction to Modules

A module in Python is a file that contains Python code, such as variables, functions, and classes. Modules help us organize code into separate files and reuse it whenever needed.

Instead of writing all the code in a single file, we can divide it into multiple modules to make the program easier to understand, maintain, and manage.

### Example

Create a file named `calculator.py`.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Here, `calculator.py` is a module containing two functions: `add()` and `subtract()`.

We can use these functions in another Python file by importing the module.

### Advantages of Modules

- **Code Reusability:** Use the same code in multiple programs.
- **Better Organization:** Keep related functions and classes together.
- **Easy Maintenance:** Update code without modifying the entire program.
- **Readability:** Make large programs easier to understand.
- **Avoid Rewriting:** Reuse existing functions instead of writing them again.

---

## 2. Types of Modules

Python modules are commonly classified into three types.

### 1. Built-in Modules

Built-in modules are provided by Python. We can import them directly and use their features.

Examples include `math`, `random`, `os`, and `datetime`.

Example:

```python
import math

print(math.sqrt(25))
print(math.factorial(5))
```

Output:

```text
5.0
120
```

Explanation:
- `math.sqrt(25)` returns the square root of 25.
- `math.factorial(5)` returns the factorial of 5.

### 2. User-Defined Modules

User-defined modules are Python files created by programmers to store their own functions, variables, and classes.

Example:

Create a file named `greetings.py`.

```python
def welcome(name):
    print("Welcome", name)
```

Create another file named `main.py`.

```python
import greetings

greetings.welcome("Rahul")
```

Output:

```text
Welcome Rahul
```

Here, `greetings.py` is our own module, and `main.py` imports and uses its function.

### 3. Third-Party Modules

Third-party modules are developed by individuals or organizations outside Python's standard library. They often need to be installed separately.

Examples include:
- `requests` — used for making HTTP requests.
- `numpy` — used for numerical calculations.
- `pandas` — used for data analysis.
- `matplotlib` — used for creating graphs and charts.

Example:

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

To install the `requests` module, run this command in the terminal:

```bash
pip install requests
```

**Note:** Built-in modules come with Python, user-defined modules are created by us, and third-party modules are usually installed separately.

---

## 3. User-Defined Modules

A user-defined module allows us to create our own Python file and reuse its code in other programs.

This approach is useful when a program contains multiple functions or when the same functionality is needed in different projects.

### Example: Creating and Using a Module

**Step 1: Create a file named `student.py`.**

```python
student_name = "Arun"
student_age = 21

def display_student():
    print("Name:", student_name)
    print("Age:", student_age)
```

**Step 2: Create another file named `main.py` in the same folder.**

```python
import student

student.display_student()
```

Output:

```text
Name: Arun
Age: 21
```

### Explanation

- `student.py` contains variables and a function.
- `main.py` imports the `student` module.
- `student.display_student()` calls the function from that module.
- The dot (`.`) operator is used to access members of the imported module.

### Importing Specific Members

We can import only the function or variable we need.

```python
from student import display_student

display_student()
```

This allows us to call `display_student()` directly without writing `student.display_student()`.

### Using an Alias

We can give a module a shorter name using the `as` keyword.

```python
import student as s

s.display_student()
```

Here, `s` is an alias for the `student` module.

### Important Point

Keep related Python files in the same folder for these beginner examples. Python's module search rules determine where it looks for imported files.

---

## 4. Import Statements

An import statement allows us to access functions, variables, and classes defined in another module.

Python provides different ways to import modules depending on what we need.

### 1. Importing an Entire Module

Syntax:

```python
import module_name
```

Example:

```python
import math

print(math.sqrt(36))
```

Output:

```text
6.0
```

We access the function using the module name followed by a dot.

### 2. Importing a Specific Function

Syntax:

```python
from module_name import function_name
```

Example:

```python
from math import sqrt

print(sqrt(49))
```

Output:

```text
7.0
```

Only the specified function is imported into the current namespace.

### 3. Importing Multiple Functions

We can import multiple members from the same module.

```python
from math import sqrt, factorial

print(sqrt(64))
print(factorial(4))
```

Output:

```text
8.0
24
```

### 4. Importing with an Alias

The `as` keyword gives a module or imported member an alternative name.

```python
import math as m

print(m.sqrt(81))
```

Output:

```text
9.0
```

### 5. Importing All Members

The `*` symbol imports names that a module exposes through its public interface.

```python
from math import *

print(sqrt(100))
print(factorial(5))
```

Output:

```text
10.0
120
```

However, using `from module import *` is generally discouraged because it can make code harder to understand and may cause naming conflicts. Importing specific members is usually better.

### 6. The `__name__` Variable

Python sets a special variable called `__name__` in each module.

When a Python file is run directly, its `__name__` is set to `"__main__"`. When it is imported as a module, its name is normally the module's name.

Example:

```python
def greet():
    print("Hello, Python!")

if __name__ == "__main__":
    greet()
```

This code calls `greet()` when the file is run directly, but not merely when the file is imported.

The `if __name__ == "__main__":` pattern is commonly used to separate code meant for direct execution from reusable module code.

---

## Summary

- A **module** is a Python file containing reusable code.
- **Built-in modules** come with Python.
- **User-defined modules** are created by programmers.
- **Third-party modules** are usually installed separately.
- `import module_name` imports a module.
- `from module_name import name` imports a specific member.
- `as` creates an alias for a module or imported member.
- `__name__` helps determine whether a file is running directly or being imported.

Modules help us write clean, reusable, and well-organized Python programs. They are an important foundation for building larger applications and working with external libraries.
