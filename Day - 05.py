# Day 05 – Python Strings and Formatting

## 1. Introduction to Strings

A string is a sequence of characters used to store text. In Python, strings belong to the `str` data type.

Strings can contain letters, numbers, spaces, and special characters.

### Creating strings

```python
name = "Bunny"
city = 'Hyderabad'
message = """Welcome to Python"""

print(name)
print(city)
print(message)
```

Output:

```text
Bunny
Hyderabad
Welcome to Python
```

Python supports single quotes, double quotes, and triple quotes for strings.

### Accessing string characters

Each character has an index. Positive indexing starts from `0`, while negative indexing starts from `-1` at the end.

```python
word = "Python"

print(word[0])
print(word[2])
print(word[-1])
```

Output:

```text
P
t
n
```

### String slicing

Slicing extracts a portion of a string using the syntax `string[start:stop:step]`.

```python
word = "Python"

print(word[0:3])
print(word[2:6])
print(word[::-1])
```

Output:

```text
Pyt
thon
nohtyP
```

The `stop` index is not included. The `[::-1]` expression reverses the string.

### Strings are immutable

Once a string is created, its individual characters cannot be changed directly.

```python
word = "Python"

# word[0] = "J"  # This causes a TypeError

word = "J" + word[1:]
print(word)
```

Output:

```text
Jython
```

Instead of changing the original character, we created a new string.

## 2. String Operations

String operations help us join, repeat, compare, and check text.

### Concatenation (`+`)

Concatenation means joining two or more strings.

```python
first_name = "Bunny"
last_name = "Kumar"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Bunny Kumar
```

### Repetition (`*`)

The multiplication operator repeats a string.

```python
text = "Python "

print(text * 3)
```

Output:

```text
Python Python Python
```

### Membership (`in` and `not in`)

These operators check whether some text exists inside another string.

```python
message = "I am learning Python"

print("Python" in message)
print("Java" not in message)
```

Output:

```text
True
True
```

### Comparing strings

Strings can be compared using comparison operators. String comparisons are case-sensitive and follow Unicode code-point order.

```python
print("Python" == "Python")
print("Python" == "python")
print("apple" < "banana")
```

Output:

```text
True
False
True
```

### Finding the length

The `len()` function returns the number of characters in a string, including spaces.

```python
message = "Hello World"

print(len(message))
```

Output:

```text
11
```

## 3. String Methods

Python provides built-in string methods for changing letter case, removing spaces, replacing text, and searching within strings. These methods return results without modifying the original string.

### Changing letter case

```python
text = "Welcome To Python"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
```

Output:

```text
WELCOME TO PYTHON
welcome to python
Welcome To Python
Welcome to python
```

- `upper()` converts letters to uppercase.
- `lower()` converts letters to lowercase.
- `title()` capitalizes the beginning of each word.
- `capitalize()` capitalizes the first character and lowercases the rest.

### Removing spaces

```python
text = "   Hello Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
```

Output:

```text
Hello Python
Hello Python   
   Hello Python
```

- `strip()` removes whitespace from both ends.
- `lstrip()` removes whitespace from the left.
- `rstrip()` removes whitespace from the right.

### Replacing text

```python
message = "I like Java"

new_message = message.replace("Java", "Python")

print(new_message)
```

Output:

```text
I like Python
```

### Searching in strings

```python
text = "Python programming"

print(text.find("programming"))
print(text.count("m"))
print(text.startswith("Python"))
print(text.endswith("ing"))
```

Output:

```text
7
2
True
True
```

- `find()` returns the first matching index, or `-1` if the text is not found.
- `count()` counts occurrences of a substring.
- `startswith()` checks the beginning of a string.
- `endswith()` checks the ending of a string.

### Splitting and joining strings

```python
text = "apple,banana,mango"

fruits = text.split(",")
print(fruits)

result = " | ".join(fruits)
print(result)
```

Output:

```text
['apple', 'banana', 'mango']
apple | banana | mango
```

`split()` separates a string into a list. `join()` combines strings from an iterable using a separator.

### Checking string content

```python
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("   ".isspace())
```

Output:

```text
True
True
True
True
```

These methods return Boolean values indicating whether the string matches the relevant condition.

## 4. Input Formatting

Input formatting means accepting user input and preparing it in the required form before using it.

Python's `input()` function always returns a string. We can convert the input or clean it using string methods.

### Accepting user input

```python
name = input("Enter your name: ")

print("Hello", name)
```

Example input:

```text
Bunny
```

Output:

```text
Hello Bunny
```

### Converting input to a number

```python
age = int(input("Enter your age: "))

print(age + 1)
```

If the user enters `21`, the output is:

```text
22
```

Use `int()` for whole numbers and `float()` for decimal numbers. Invalid numeric input raises a `ValueError`.

### Cleaning user input

```python
name = input("Enter your name: ").strip().title()

print(name)
```

If the user enters `   bunny kumar   `, the output is:

```text
Bunny Kumar
```

Here, `strip()` removes surrounding spaces, and `title()` formats the capitalization.

### Accepting multiple values

```python
name, city = input("Enter name and city: ").split()

print(name)
print(city)
```

Example input:

```text
Bunny Hyderabad
```

Output:

```text
Bunny
Hyderabad
```

The number of separated values must match the number of variables on the left side.

## 5. Output Formatting

Output formatting means displaying information in a clear and readable way.

Python's `print()` function can display multiple values, add separators, and control line endings.

### Using `print()` with multiple values

```python
name = "Bunny"
age = 21

print("Name:", name, "Age:", age)
```

Output:

```text
Name: Bunny Age: 21
```

### Using the `sep` parameter

The `sep` parameter controls the separator between multiple values.

```python
print("2026", "10", "23", sep="-")
print("Python", "Java", "SQL", sep=" | ")
```

Output:

```text
2026-10-23
Python | Java | SQL
```

### Using the `end` parameter

By default, `print()` ends with a newline. The `end` parameter changes what appears at the end.

```python
print("Hello", end=" ")
print("Python")
```

Output:

```text
Hello Python
```

### Controlling decimal places

The `round()` function can round a number, while formatted output can control how many decimal places are displayed.

```python
price = 123.4567

print(round(price, 2))
print(f"{price:.2f}")
```

Output:

```text
123.46
123.46
```

The formatted expression `:.2f` displays exactly two digits after the decimal point.

## 6. Modulo Formatting

Modulo formatting is an older method of formatting strings using the `%` operator. It inserts values into placeholders in a string.

**Note:** Here, `%` is being used for string formatting, not for calculating the remainder.

### Common formatting placeholders

| Placeholder | Purpose |
|---|---|
| `%s` | String representation |
| `%d` | Integer |
| `%f` | Floating-point number |
| `%.2f` | Float displayed to two decimal places |

### Formatting a string

```python
name = "Bunny"

print("Hello, %s!" % name)
```

Output:

```text
Hello, Bunny!
```

### Formatting integers

```python
age = 21

print("My age is %d" % age)
```

Output:

```text
My age is 21
```

### Formatting decimal numbers

```python
price = 99.567

print("Price: %.2f" % price)
```

Output:

```text
Price: 99.57
```

### Formatting multiple values

```python
name = "Bunny"
age = 21
marks = 89.567

print("Name: %s, Age: %d, Marks: %.2f" % (name, age, marks))
```

Output:

```text
Name: Bunny, Age: 21, Marks: 89.57
```

Modulo formatting is still supported, but f-strings and the `format()` method are generally easier to read in modern Python code.

## 7. F-Strings

F-strings are a modern and readable way to insert variables and expressions into strings. Put the letter `f` before the opening quote and write variables or expressions inside `{}`.

### Basic f-string

```python
name = "Bunny"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Bunny and I am 21 years old.
```

### Using expressions

```python
a = 10
b = 20

print(f"Sum = {a + b}")
print(f"Product = {a * b}")
```

Output:

```text
Sum = 30
Product = 200
```

### Formatting decimal values

```python
price = 123.4567

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 123.46
```

### Alignment and width

```python
name = "Python"

print(f"|{name:<10}|")
print(f"|{name:>10}|")
print(f"|{name:^10}|")
```

Output:

```text
|Python    |
|    Python|
|  Python  |
```

- `<` aligns text to the left.
- `>` aligns text to the right.
- `^` centers text.
- `10` sets the field width to 10 characters.

### Formatting percentages

```python
score = 0.875

print(f"Score: {score:.1%}")
```

Output:

```text
Score: 87.5%
```

### F-strings with dictionaries

```python
student = {"name": "Bunny", "age": 21}

print(f"Name: {student['name']}, Age: {student['age']}")
```

Output:

```text
Name: Bunny, Age: 21
```

**Remember:** F-strings are usually the best choice for readable string formatting in modern Python.

## 8. Dot `format()` Method

The `format()` method is another way to insert values into strings. It uses `{}` placeholders and calls `.format()` on the string.

### Basic formatting

```python
name = "Bunny"
age = 21

message = "My name is {} and I am {} years old.".format(name, age)

print(message)
```

Output:

```text
My name is Bunny and I am 21 years old.
```

### Using positional indexes

You can choose which value goes into each placeholder using an index.

```python
message = "{1} is learning {0}".format("Python", "Bunny")

print(message)
```

Output:

```text
Bunny is learning Python
```

Index `0` refers to the first argument, and index `1` refers to the second.

### Using named placeholders

```python
message = "Name: {name}, Course: {course}".format(
    name="Bunny",
    course="Python"
)

print(message)
```

Output:

```text
Name: Bunny, Course: Python
```

### Formatting decimal values

```python
price = 123.4567

print("Price: {:.2f}".format(price))
```

Output:

```text
Price: 123.46
```

### Formatting alignment

```python
name = "Python"

print("|{:<10}|".format(name))
print("|{:>10}|".format(name))
print("|{:^10}|".format(name))
```

Output:

```text
|Python    |
|    Python|
|  Python  |
```

### Difference between formatting methods

| Method | Example | Main point |
|---|---|---|
| Modulo formatting | `"%s" % name` | Older formatting style |
| F-string | `f"{name}"` | Clear and convenient |
| `format()` method | `"{}".format(name)` | Uses placeholders and arguments |

## Quick Revision

- A string stores text and is immutable.
- Indexing accesses individual characters, and slicing extracts part of a string.
- String operations include concatenation, repetition, comparison, and membership checking.
- String methods help clean, search, replace, and transform text.
- `input()` returns a string; convert it when you need a numeric value.
- `print()` supports output controls such as `sep` and `end`.
- Modulo formatting uses placeholders such as `%s`, `%d`, and `%f`.
- F-strings insert variables and expressions directly into strings.
- The `.format()` method inserts values into `{}` placeholders.

## What I Learned Today

Today I learned how to work with Python strings, use string methods, accept and clean user input, format printed output, and display variables using modulo formatting, f-strings, and the `format()` method.
