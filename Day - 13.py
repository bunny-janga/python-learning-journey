# Python Functions – Complete Notes

## 1. Functions Introduction

### What is a Function?

A function is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we can create a function and call it whenever needed.

### Why Do We Use Functions?

- Code reusability
- Reduce code duplication
- Improve readability
- Make programs easier to maintain
- Divide large programs into smaller parts

### Example

```python
def greet():
    print("Hello, Welcome to Python!")

greet()
```

**Output:**
```text
Hello, Welcome to Python!
```

**Explanation:**
- `def` is the keyword used to define a function.
- `greet` is the function name.
- The indented statement is the function body.
- `greet()` calls the function.

---

## 2. User-Defined Functions

A user-defined function is a function created by the programmer to perform a particular task.

### Example 1: Adding Two Numbers

```python
def add():
    a = 10
    b = 20
    print("Sum:", a + b)

add()
```

**Output:**
```text
Sum: 30
```

### Example 2: Function with Parameters

```python
def greet(name):
    print("Hello", name)

greet("Rahul")
greet("Priya")
```

**Output:**
```text
Hello Rahul
Hello Priya
```

**Explanation:**
- `name` is a parameter.
- `"Rahul"` and `"Priya"` are arguments passed when calling the function.

---

## 3. Types of Functions

Python functions can be classified in different ways.

### 1. Built-in Functions

These are already available in Python.

Examples: `print()`, `input()`, `len()`, `sum()`, `max()`, `min()`, `type()`.

```python
numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
```

**Output:**
```text
3
60
30
```

### 2. User-Defined Functions

These are created by programmers using `def`.

```python
def square(number):
    print(number * number)

square(5)
```

**Output:**
```text
25
```

### 3. Anonymous (Lambda) Functions

A lambda function is a small function written using the `lambda` keyword.

```python
square = lambda x: x * x

print(square(4))
```

**Output:**
```text
16
```

### Common Function Forms Based on Arguments and Return Values

| Type | Description |
|---|---|
| No arguments, no return value | Receives nothing and returns no result explicitly |
| Arguments, no return value | Receives values and performs a task |
| No arguments, returns a value | Returns a result without receiving arguments |
| Arguments and return value | Receives values and returns a result |

Example:

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)
```

**Output:**
```text
20
```

---

## 4. Function Syntax

### General Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

**Explanation:**
- `def` defines the function.
- `function_name` is the name of the function.
- `parameters` receive values from the caller.
- The function body contains the statements to execute.
- `return` sends a result back to the caller. It is optional.

### Example

```python
def display_message():
    print("Learning Python Functions")

display_message()
```

**Output:**
```text
Learning Python Functions
```

### Function Naming Rules

- Use meaningful names.
- Names can contain letters, digits, and underscores.
- Names cannot start with a digit.
- Function names are case-sensitive.
- Do not use Python keywords as function names.
- By convention, use `snake_case`, such as `calculate_total()`.

---

## 5. Return Statements

The `return` statement sends a value from a function back to the place where the function was called. It also ends the function's execution.

### Example 1: Return a Value

```python
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)
```

**Output:**
```text
Sum: 30
```

### Example 2: Return Multiple Values

```python
def calculate(a, b):
    return a + b, a - b

sum_result, difference = calculate(10, 5)

print("Sum:", sum_result)
print("Difference:", difference)
```

**Output:**
```text
Sum: 15
Difference: 5
```

### Example 3: Function Without an Explicit Return

```python
def greet():
    print("Hello")

result = greet()
print(result)
```

**Output:**
```text
Hello
None
```

**Important:** If a function does not explicitly return a value, Python returns `None`.

### Difference Between `print()` and `return`

- `print()` displays information on the screen.
- `return` sends a value back so the calling code can use it.

---

## 6. Positional Arguments

Positional arguments are passed to a function in the order of the parameters.

### Example

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Rahul", 21)
```

**Output:**
```text
Name: Rahul
Age: 21
```

**Explanation:**
- `"Rahul"` is assigned to `name`.
- `21` is assigned to `age`.
- The order matters.

### Example: Changing the Order

```python
def subtract(a, b):
    print(a - b)

subtract(10, 3)
subtract(3, 10)
```

**Output:**
```text
7
-7
```

**Important:** Positional arguments must match the intended parameter order.

---

## 7. Default Arguments

A default argument is a parameter that has a predefined value. If the caller does not supply that argument, Python uses the default value.

### Example

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rahul")
```

**Output:**
```text
Hello Guest
Hello Rahul
```

### Example: Default Tax Rate

```python
def calculate_price(price, tax=5):
    total = price + (price * tax / 100)
    return total

print(calculate_price(100))
print(calculate_price(100, 10))
```

**Output:**
```text
105.0
110.0
```

**Important Rules:**
- Parameters with default values must come after parameters without default values.
- Default values are used only when the caller does not provide an argument for that parameter.

Correct:

```python
def student(name, age=18):
    print(name, age)
```

Incorrect:

```python
# SyntaxError
# def student(age=18, name):
#     print(name, age)
```

---

## 8. Keyword Arguments

Keyword arguments are passed using parameter names. Their order does not matter when the argument names are specified.

### Example

```python
def student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student(age=21, city="Hyderabad", name="Rahul")
```

**Output:**
```text
Name: Rahul
Age: 21
City: Hyderabad
```

### Example: Mixing Positional and Keyword Arguments

```python
def display(name, age):
    print(name, age)

display("Priya", age=20)
```

**Output:**
```text
Priya 20
```

**Important:** Positional arguments must come before keyword arguments in a function call.

Correct:

```python
display("Priya", age=20)
```

Incorrect:

```python
# SyntaxError
# display(name="Priya", 20)
```

---

## 9. Variable-Length Arguments (`*args`)

Variable-length arguments allow a function to accept any number of positional arguments.

The `*args` syntax collects extra positional arguments into a tuple.

### Example 1: Adding Multiple Numbers

```python
def add(*args):
    total = 0

    for number in args:
        total += number

    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

**Output:**
```text
30
60
15
```

### Example 2: Display Multiple Names

```python
def display_names(*args):
    for name in args:
        print(name)

display_names("Rahul", "Priya", "Arjun")
```

**Output:**
```text
Rahul
Priya
Arjun
```

**Important Points:**
- `*args` can accept zero or more positional arguments.
- Inside the function, `args` is a tuple.
- The name `args` is conventional; the `*` is what provides the behavior.

---

## 10. Keyword Variable-Length Arguments (`**kwargs`)

The `**kwargs` syntax allows a function to accept any number of keyword arguments. Python collects them into a dictionary.

### Example 1: Student Details

```python
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Rahul", age=21, city="Hyderabad")
```

**Output:**
```text
name : Rahul
age : 21
city : Hyderabad
```

### Example 2: Product Details

```python
def product(**kwargs):
    print(kwargs)

product(name="Laptop", price=50000, brand="Dell")
```

**Output:**
```text
{'name': 'Laptop', 'price': 50000, 'brand': 'Dell'}
```

**Important Points:**
- `**kwargs` accepts zero or more keyword arguments.
- Inside the function, `kwargs` is a dictionary.
- The name `kwargs` is conventional; the double asterisks provide the behavior.

### Difference Between `*args` and `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Accepts | Extra positional arguments | Extra keyword arguments |
| Stored as | Tuple | Dictionary |
| Example call | `func(10, 20, 30)` | `func(name="Rahul", age=21)` |

### Combining Different Argument Types

```python
def example(name, *args, city="Unknown", **kwargs):
    print("Name:", name)
    print("Extra positional arguments:", args)
    print("City:", city)
    print("Extra keyword arguments:", kwargs)

example("Rahul", 10, 20, city="Hyderabad", age=21)
```

**Output:**
```text
Name: Rahul
Extra positional arguments: (10, 20)
City: Hyderabad
Extra keyword arguments: {'age': 21}
```

---

## Summary

- **Functions:** Reusable blocks of code that perform tasks.
- **User-Defined Functions:** Functions created using `def`.
- **Types of Functions:** Built-in, user-defined, and lambda functions.
- **Function Syntax:** Defines the function name, parameters, and body.
- **Return Statement:** Sends a result back to the caller.
- **Positional Arguments:** Values are matched by order.
- **Default Arguments:** Parameters have predefined values.
- **Keyword Arguments:** Values are passed using parameter names.
- **`*args`:** Accepts extra positional arguments as a tuple.
- **`**kwargs`:** Accepts extra keyword arguments as a dictionary.

Functions help make Python programs reusable, readable, organized, and easier to maintain.
