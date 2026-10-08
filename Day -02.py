# Day 2 — Python Setup, Git Basics, Variables & Comments

## Topics Covered

1. Python Installation & IDE Setup
2. GitHub Account Creation
3. Git Basics & Drag-and-Drop Usage
4. Tokens & Statements
5. Identifiers
6. Single-Line & Multi-Line Comments
7. Variables & Naming Rules
8. Multiple Assignment
9. Reassignment
10. Swapping Variables
11. Deleting Variables

---

## 1. Python Installation & IDE Setup

Before starting Python programming, we need to install Python on our computer and choose a code editor.

I am using **VS Code** to write and run my Python programs.

### Check Python Installation

Open the terminal and type:

```bash
python --version
```

On some Windows systems, we can also use:

```bash
py --version
```

If Python is installed correctly, it will show the installed version.

Example:

```text
Python 3.x.x
```

### First Python Program

Create a file called `hello.py`:

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

### Simple understanding

* **Python** → Programming language
* **VS Code** → Code editor
* **Terminal** → Used to run commands and programs

---

# 2. GitHub Account Creation

**GitHub** is an online platform used to store, manage, and share code.

I can use GitHub to:

* Store my learning notes
* Track changes
* Maintain projects
* Share my work
* Build my developer portfolio

### Git vs GitHub

These are related, but they are not the same.

```text
Git      → Version control system
GitHub   → Online platform for hosting Git repositories
```

For example, I can create my Python repository locally and then push it to GitHub.

---

# 3. Git Basics & Drag-and-Drop Usage

**Git** helps me track changes in my files and maintain different versions of my work.

Some basic Git commands are:

```bash
git init
git status
git add
git commit
git push
git pull
```

### Basic Git Workflow

```text
Create / Edit Files
        ↓
    git status
        ↓
      git add
        ↓
    git commit
        ↓
     git push
        ↓
      GitHub
```

### Example

After creating my Day 2 notes:

```bash
git status
```

I can add only that file:

```bash
git add Day-02/notes.md
```

Then create a commit:

```bash
git commit -m "Add Day 2 Python setup and variables notes"
```

Finally:

```bash
git push
```

### Drag-and-Drop

GitHub also provides an option to upload files through the website.

However, using Git commands helps me understand how version control actually works.

---

# 4. Tokens & Statements

## Tokens

A **token** is one of the smallest meaningful elements of a Python program.

Example:

```python
name = "Bunny"
```

The important parts are:

```text
name
=
"Bunny"
```

Python has different types of tokens, including:

* Keywords
* Identifiers
* Literals
* Operators
* Delimiters

### Example

```python
age = 20
```

Here:

```text
age → Identifier
=   → Operator
20  → Literal
```

---

## Statements

A **statement** is an instruction that tells Python to perform an action.

Example:

```python
name = "Bunny"
```

This is an assignment statement.

Another example:

```python
print("Hello")
```

This tells Python to display text.

A program can contain multiple statements:

```python
name = "Bunny"
age = 20

print(name)
print(age)
```

---

# 5. Identifiers

An **identifier** is the name given to programming elements such as variables, functions, and classes.

Example:

```python
name = "Bunny"
age = 20
```

Here, `name` and `age` are identifiers.

## Rules for Identifiers

### 1. Letters, numbers and underscore can be used

```python
student_name = "Rahul"
student1 = "Priya"
```

### 2. An identifier cannot start with a number

❌ Incorrect:

```python
1student = "Rahul"
```

✅ Correct:

```python
student1 = "Rahul"
```

### 3. Spaces are not allowed

❌ Incorrect:

```python
student name = "Rahul"
```

✅ Correct:

```python
student_name = "Rahul"
```

### 4. Python keywords cannot be used as identifiers

For example:

```text
if
for
while
class
def
```

should not be used as normal variable names.

### 5. Python is case-sensitive

These are different identifiers:

```python
name = "Bunny"
Name = "Rahul"
NAME = "John"
```

I prefer using **snake_case** for variable names:

```python
student_name = "Rahul"
total_marks = 450
phone_number = "9876543210"
```

---

# 6. Single-Line & Multi-Line Comments

Comments are notes written in code to help humans understand it.

Python does not execute normal comments.

## Single-Line Comment

We use `#` for a single-line comment.

```python
# This is my first Python comment

name = "Bunny"
print(name)
```

The line beginning with `#` is ignored by Python.

We can also write a comment beside code:

```python
age = 20  # Student age
```

---

## Multi-Line Comments

Python does not have a separate official multi-line comment syntax.

Triple quotes can be used for documentation-style multi-line text:

```python
"""
This program demonstrates
basic Python variables.
"""

name = "Bunny"
print(name)
```

Technically, triple quotes create a **multi-line string**, rather than a true comment. They are commonly used for documentation and docstrings.

### Why comments are useful

Comments help me:

* Understand my own code later
* Explain code to others
* Make programs easier to read
* Remember the purpose of a particular section

---

# 7. Variables & Naming Rules

A **variable** is a name that refers to a value.

Example:

```python
name = "Bunny"
age = 20
course = "Python"
```

Here:

```text
name   → "Bunny"
age    → 20
course → "Python"
```

We can use these variables later:

```python
name = "Bunny"

print("My name is", name)
```

Output:

```text
My name is Bunny
```

## Good Variable Names

Meaningful names make code easier to understand.

```python
student_name = "Rahul"
student_age = 20
student_marks = 85
```

Instead of unclear names like:

```python
x = "Rahul"
a = 20
b = 85
```

For larger programs, meaningful variable names are much easier to work with.

---

# 8. Multiple Assignment

Python allows us to assign values to multiple variables in one statement.

Example:

```python
name, age, course = "Bunny", 20, "Python"
```

Now:

```python
print(name)
print(age)
print(course)
```

Output:

```text
Bunny
20
Python
```

### Assigning the same value

We can also assign one value to multiple variables:

```python
x = y = z = 100
```

Now all three variables contain `100`.

```python
print(x)
print(y)
print(z)
```

Output:

```text
100
100
100
```

---

# 9. Reassignment

A variable can be given a new value.

Example:

```python
age = 20

print(age)

age = 21

print(age)
```

Output:

```text
20
21
```

The second assignment changes what `age` refers to.

Another example:

```python
course = "Python"

course = "Full Stack Python"

print(course)
```

Output:

```text
Full Stack Python
```

Python also allows a variable to refer to different types of values:

```python
value = 10
value = "Python"

print(value)
```

Output:

```text
Python
```

---

# 10. Swapping Variables

**Swapping** means exchanging the values of two variables.

For example:

```text
Before:
a = 10
b = 20

After:
a = 20
b = 10
```

Python makes this simple:

```python
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)
```

Output:

```text
a = 20
b = 10
```

In many programming languages, a temporary variable is commonly used:

```python
a = 10
b = 20

temp = a
a = b
b = temp
```

But Python allows the shorter approach:

```python
a, b = b, a
```

This is one of the convenient features of Python.

---

# 11. Deleting Variables

Python provides the `del` keyword to remove a variable.

Example:

```python
name = "Bunny"

print(name)

del name
```

After deleting the variable, trying to access it will cause a `NameError`.

```python
print(name)
```

Example:

```python
age = 20

print(age)

del age

# print(age)  # NameError
```

We can also delete multiple variables:

```python
a = 10
b = 20

del a, b
```

---

# 🧠 Day 2 Quick Revision

```text
Python
  ↓
Installation & VS Code
  ↓
Git & GitHub
  ↓
Tokens & Statements
  ↓
Identifiers
  ↓
Comments
  ↓
Variables
  ↓
Multiple Assignment
  ↓
Reassignment
  ↓
Swapping
  ↓
Deleting Variables
```

## Important Syntax

```python
# Comment

name = "Bunny"

# Multiple assignment
name, age = "Bunny", 20

# Same value to multiple variables
x = y = 100

# Reassignment
age = 20
age = 21

# Swapping
a, b = b, a

# Delete a variable
del name
```

# Day 2 Takeaway

Today I learned how to set up Python and started working with the basic building blocks of Python.

The main concepts I learned were **Git and GitHub, tokens, statements, identifiers, comments, variables, multiple assignment, reassignment, swapping, and deleting variables**.

These are simple concepts, but they are important because I will use them throughout my Python learning journey.
