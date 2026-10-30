# Day 20: Python Exception Handling and File Handling

## 1. Introduction to Exception Handling

An exception is an error that occurs while a program is running. If an exception is not handled, the program may stop unexpectedly.

Python provides exception-handling keywords that help us handle errors and allow the program to continue safely.

### Why do we use exception handling?

- To prevent unexpected program termination.
- To handle invalid user input.
- To display meaningful error messages.
- To make programs more reliable.

### Example without exception handling

```python
a = 10
b = 0

result = a / b

print(result)
```

**Output:**

```text
ZeroDivisionError: division by zero
```

The program stops because division by zero is not allowed.

---

## 2. Try Block

The `try` block contains code that might produce an exception.

If an error occurs inside the `try` block, Python looks for a matching `except` block to handle it.

### Syntax

```python
try:
    # Code that may cause an error
    statements
```

### Example

```python
try:
    a = 10
    b = 2

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

**Output:**

```text
Result: 5.0
```

### Explanation

- Python executes the statements inside `try`.
- Since the division is valid, no exception occurs.
- The result is displayed.
- The `except` block is skipped.

---

## 3. Except Block

The `except` block handles exceptions raised inside the `try` block.

We can use different `except` blocks to handle different types of errors.

### Syntax

```python
try:
    statements

except ErrorType:
    statements
```

### Example 1: Handling division by zero

```python
try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide a number by zero.")
```

**Output:**

```text
Cannot divide a number by zero.
```

### Example 2: Handling invalid input

```python
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid integer.")
```

**Sample output:**

```text
Enter a number: hello
Please enter a valid integer.
```

### Example 3: Multiple except blocks

```python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

**Sample output:**

```text
Enter first number: 10
Enter second number: 0
Cannot divide by zero.
```

### Important points

- `except` handles errors from the associated `try` block.
- We can use multiple `except` blocks.
- It is better to handle specific exceptions rather than catching every error unnecessarily.

---

## 4. Else Block

The `else` block executes only when the `try` block completes without any exception.

It is useful when we want to separate successful operations from error-handling code.

### Syntax

```python
try:
    statements

except ErrorType:
    statements

else:
    statements
```

### Example

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)
```

**Sample output:**

```text
Enter a number: 25
You entered: 25
```

### Explanation

- If the input is valid, the `else` block executes.
- If an exception occurs, the `except` block executes instead.
- The `else` block does not execute when an exception occurs in `try`.

---

## 5. Finally Block

The `finally` block executes whether an exception occurs or not.

It is commonly used for cleanup operations, such as closing files or releasing resources.

### Syntax

```python
try:
    statements

except ErrorType:
    statements

finally:
    statements
```

### Example 1: Without an exception

```python
try:
    print("Program started.")

finally:
    print("Finally block executed.")
```

**Output:**

```text
Program started.
Finally block executed.
```

### Example 2: With an exception

```python
try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program completed.")
```

**Output:**

```text
Cannot divide by zero.
Program completed.
```

### Difference between try, except, else, and finally

| Keyword | Purpose |
|---|---|
| `try` | Contains code that may cause an exception |
| `except` | Handles an exception |
| `else` | Runs when no exception occurs in `try` |
| `finally` | Runs during normal or exceptional execution |

---

# File Handling in Python

## 6. Introduction to File Handling

File handling allows us to create, read, update, and store information in files.

Instead of losing data when a program finishes, we can save information in files and use it later.

### Why do we use file handling?

- To store information permanently.
- To read saved information.
- To update existing data.
- To maintain records and reports.
- To work with text files and other file formats.

Python provides the built-in `open()` function to work with files.

---

## 7. File Open

The `open()` function is used to open a file.

### Syntax

```python
file = open("filename.txt", "mode")
```

Here:
- `filename.txt` is the file name.
- `mode` specifies what operation we want to perform.

### Common file modes

| Mode | Purpose |
|---|---|
| `"r"` | Opens a file for reading |
| `"w"` | Opens a file for writing; overwrites existing content |
| `"a"` | Opens a file for appending content |
| `"x"` | Creates a new file; raises an error if it already exists |
| `"rb"` | Opens a file for reading in binary mode |
| `"wb"` | Opens a file for writing in binary mode |

### Example

```python
file = open("sample.txt", "w")

print("File opened successfully.")

file.close()
```

**Output:**

```text
File opened successfully.
```

The file `sample.txt` is created if it does not already exist.

---

## 8. Read Operation

The `read()` method is used to read content from a file.

### Example

```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

**Output (if the file contains this text):**

```text
Hello Python!
Welcome to file handling.
```

### Other reading methods

**1. read()**

Reads the entire remaining content of a file.

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
```

**2. readline()**

Reads one line at a time.

```python
file = open("sample.txt", "r")

print(file.readline())
print(file.readline())

file.close()
```

**3. readlines()**

Reads all lines and returns them as a list.

```python
file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()
```

---

## 9. Write Operation

The `write()` method is used to write content into a file.

When we open a file using `"w"` mode:
- A new file is created if it does not exist.
- Existing content is overwritten if the file already exists.

### Example

```python
file = open("sample.txt", "w")

file.write("Hello Python!\n")
file.write("Learning file handling.")

file.close()

print("Data written successfully.")
```

**Output:**

```text
Data written successfully.
```

**Content inside sample.txt:**

```text
Hello Python!
Learning file handling.
```

### Important point

The `\n` character creates a new line in the file.

---

## 10. Append Operation

The `append` operation adds new content to the end of an existing file without deleting its previous content.

We use `"a"` mode for appending.

### Example

```python
file = open("sample.txt", "a")

file.write("\nWelcome to Python programming.")

file.close()

print("Data appended successfully.")
```

**Output:**

```text
Data appended successfully.
```

**Updated content inside sample.txt:**

```text
Hello Python!
Learning file handling.
Welcome to Python programming.
```

### Difference between write and append

| Write (`"w"`) | Append (`"a"`) |
|---|---|
| Writes content to a file | Adds content to the end |
| Overwrites old content | Preserves old content |
| Creates file if missing | Creates file if missing |

---

## 11. Close Operation

The `close()` method is used to close an opened file.

Closing a file releases the resources associated with it and helps ensure that buffered data is written.

### Example

```python
file = open("sample.txt", "r")

print(file.read())

file.close()

print("File closed:", file.closed)
```

**Output (based on the sample file):**

```text
Hello Python!
Learning file handling.
Welcome to Python programming.
File closed: True
```

### Why should we close files?

- To release system resources.
- To finish writing buffered content.
- To avoid keeping unnecessary files open.

### Better approach: Using with

Python provides the `with` statement to manage files automatically.

The file is closed automatically when the `with` block finishes, even if an exception occurs.

```python
with open("sample.txt", "w") as file:
    file.write("Learning Python file handling.")

print("File operation completed.")
```

**Output:**

```text
File operation completed.
```

Using `with` is generally recommended instead of manually opening and closing files.

---

## 12. Complete File Handling Example

This example combines writing, reading, and appending operations.

```python
# Writing content into a file

with open("student.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Course: Python\n")

print("File created and data written.")

# Reading file content

with open("student.txt", "r") as file:
    print("\nStudent Details:")
    print(file.read())

# Appending new information

with open("student.txt", "a") as file:
    file.write("Status: Learning\n")

print("New information added.")

# Reading updated content

with open("student.txt", "r") as file:
    print("\nUpdated Student Details:")
    print(file.read())
```

**Output:**

```text
File created and data written.

Student Details:
Name: Rahul
Course: Python

New information added.

Updated Student Details:
Name: Rahul
Course: Python
Status: Learning
```

---

## 13. Quick Revision

| Topic | Main purpose |
|---|---|
| `try` | Tests code that may cause an exception |
| `except` | Handles errors |
| `else` | Runs when no exception occurs |
| `finally` | Executes during normal or exceptional execution |
| `open()` | Opens a file |
| `read()` | Reads file content |
| `write()` | Writes or replaces file content |
| `append` mode | Adds content to the end of a file |
| `close()` | Closes an opened file |
| `with` | Automatically manages file closing |

## 14. What I Learned Today

- How to handle exceptions using `try` and `except`.
- How to use multiple `except` blocks.
- How the `else` block works.
- Why the `finally` block is useful.
- How to open files using Python.
- How to read file content using `read()`, `readline()`, and `readlines()`.
- How to write data using `write()`.
- How to append new data without removing existing content.
- How to close files using `close()`.
- How to use the `with` statement for safer file handling.

**Day 20 completed: Python Exception Handling and File Handling.**
