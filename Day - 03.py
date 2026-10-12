#Day 03 – Python Data Types and Type Conversion

## 1. Numeric Datatypes

Python has three main numeric data types: `int`, `float`, and `complex`.

### Integer (`int`)

An integer is a whole number without a decimal point.

```python
age = 21
number = -10
count = 100

print(age)
print(type(age))
```

Output:
```text
21
<class 'int'>
```

### Float (`float`)

A float is a number that contains a decimal point.

```python
price = 99.50
height = 155.5

print(price)
print(type(price))
```

Output:
```text
99.5
<class 'float'>
```

### Complex (`complex`)

A complex number contains a real part and an imaginary part. Python uses `j` for the imaginary part.

```python
number = 3 + 4j

print(number)
print(type(number))
print(number.real)
print(number.imag)
```

Output:
```text
(3+4j)
<class 'complex'>
3.0
4.0
```

**Remember:** `int` = whole numbers, `float` = decimal numbers, and `complex` = numbers with an imaginary part.

## 2. Strings

A string (`str`) is a sequence of characters. We use single quotes or double quotes to create strings.

```python
name = "Bunny"
city = 'Hyderabad'
message = "Welcome to Python"

print(name)
print(city)
print(message)
```

### Accessing characters

We can access individual characters using indexing. Indexing starts from `0`.

```python
word = "Python"

print(word[0])
print(word[1])
print(word[-1])
```

Output:
```text
P
y
n
```

### String slicing

Slicing is used to get a part of a string.

```python
word = "Python"

print(word[0:3])
print(word[2:6])
```

Output:
```text
Pyt
thon
```

The ending index is not included.

### String methods

Python provides useful methods to work with strings.

```python
text = "  hello python  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("python", "world"))
```

Output:
```text
  HELLO PYTHON
  hello python
hello python
  hello world
```

### String concatenation

Concatenation means joining strings using the `+` operator.

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

### f-strings

An f-string allows us to insert variables directly into a string.

```python
name = "Bunny"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:
```text
My name is Bunny and I am 21 years old.
```

**Remember:** Strings are immutable, which means we cannot change an individual character directly after creating a string.

## 3. Lists

A list is used to store multiple values in a single variable. Lists are ordered, changeable (mutable), and allow duplicate values.

```python
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
print(fruits[-1])
```

Output:
```text
['apple', 'banana', 'mango']
apple
mango
```

### Adding elements

`append()` adds an element at the end, while `insert()` adds an element at a specified position.

```python
fruits = ["apple", "banana"]

fruits.append("mango")
fruits.insert(1, "orange")

print(fruits)
```

Output:
```text
['apple', 'orange', 'banana', 'mango']
```

### Removing elements

```python
fruits = ["apple", "banana", "mango"]

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)
```

Output:
```text
['apple', 'mango']
['apple']
```

`remove()` removes a matching value. `pop()` removes an element by index, or the last element if no index is given.

### Updating a list

```python
numbers = [10, 20, 30]

numbers[1] = 25

print(numbers)
```

Output:
```text
[10, 25, 30]
```

### Useful list operations

```python
numbers = [40, 10, 30, 20]

print(len(numbers))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
```

Output:
```text
4
[10, 20, 30, 40]
[40, 30, 20, 10]
```

**Remember:** Lists use square brackets `[]` and can be modified after creation.

## 4. Tuples

A tuple is used to store multiple values in a single variable. Tuples are ordered and allow duplicates, but they are immutable.

```python
colors = ("red", "green", "blue")

print(colors)
print(colors[0])
print(colors[-1])
print(type(colors))
```

Output:
```text
('red', 'green', 'blue')
red
blue
<class 'tuple'>
```

### Creating a single-element tuple

A comma is required when creating a tuple with only one element.

```python
value = (10,)

print(type(value))
```

Output:
```text
<class 'tuple'>
```

Without the comma, `(10)` is simply an integer expression.

### Tuple methods

Tuples have methods such as `count()` and `index()`.

```python
numbers = (10, 20, 10, 30)

print(numbers.count(10))
print(numbers.index(20))
```

Output:
```text
2
1
```

**Remember:** Tuples use parentheses `()` and cannot be modified after creation.

## 5. Dictionaries

A dictionary stores data as key-value pairs. Dictionaries are changeable, and keys must be unique.

```python
student = {
    "name": "Bunny",
    "age": 21,
    "course": "Python"
}

print(student)
print(student["name"])
print(student["age"])
```

Output:
```text
{'name': 'Bunny', 'age': 21, 'course': 'Python'}
Bunny
21
```

### Adding and updating values

```python
student = {"name": "Bunny", "age": 21}

student["city"] = "Hyderabad"
student["age"] = 22

print(student)
```

Output:
```text
{'name': 'Bunny', 'age': 22, 'city': 'Hyderabad'}
```

### Accessing values safely

The `get()` method returns a value for a key. If the key is missing, it returns `None` by default.

```python
student = {"name": "Bunny"}

print(student.get("name"))
print(student.get("marks"))
```

Output:
```text
Bunny
None
```

### Removing a key

```python
student = {
    "name": "Bunny",
    "age": 21
}

student.pop("age")

print(student)
```

Output:
```text
{'name': 'Bunny'}
```

### Useful dictionary methods

```python
student = {
    "name": "Bunny",
    "age": 21
}

print(student.keys())
print(student.values())
print(student.items())
```

These methods return the dictionary's keys, values, and key-value pairs.

**Remember:** Dictionaries use curly brackets `{}` with key-value pairs separated by colons.

## 6. Sets

A set stores unique values. Sets do not guarantee a fixed order, and duplicate elements are removed automatically.

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Output:
```text
{10, 20, 30}
```

The order of elements in the output may vary.

### Adding elements

```python
fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)
```

### Removing elements

```python
fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)
```

`remove()` raises a `KeyError` if the value does not exist. `discard()` does not raise an error when the value is missing.

### Set operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
```

Output:
```text
{1, 2, 3, 4, 5}
{3}
{1, 2}
```

- `union()` combines the elements of both sets.
- `intersection()` returns the common elements.
- `difference()` returns elements in the first set that are not in the second.

### Creating an empty set

```python
empty_set = set()
empty_dictionary = {}

print(type(empty_set))
print(type(empty_dictionary))
```

Output:
```text
<class 'set'>
<class 'dict'>
```

**Remember:** Use `set()` to create an empty set. Empty curly brackets `{}` create a dictionary.

## 7. Type Conversion

Type conversion means changing a value from one data type to another.

Python supports built-in conversion functions such as `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, and `dict()`.

### Integer conversion

```python
number = int("100")

print(number)
print(type(number))
```

Output:
```text
100
<class 'int'>
```

A valid integer string can be converted into an integer. However, `int("hello")` raises a `ValueError`.

### Float conversion

```python
price = float("99.5")

print(price)
print(type(price))
```

Output:
```text
99.5
<class 'float'>
```

### String conversion

```python
age = 21

text = str(age)

print(text)
print(type(text))
```

Output:
```text
21
<class 'str'>
```

The value becomes a string, even though it looks like a number when printed.

### Converting between collections

```python
numbers = [1, 2, 2, 3]

print(tuple(numbers))
print(set(numbers))
```

Output:
```text
(1, 2, 2, 3)
{1, 2, 3}
```

Converting a list to a set removes duplicate values.

### Converting input into a number

The `input()` function returns a string, even when the user enters a number.

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters `21`, the type is still `str`.

To perform arithmetic, convert the input:

```python
age = int(input("Enter your age: "))

print(age + 1)
```

If the user enters `21`, the output is:

```text
22
```

### Implicit and explicit conversion

**Implicit conversion:** Python automatically converts a value when appropriate.

```python
a = 10
b = 2.5

result = a + b

print(result)
print(type(result))
```

Output:
```text
12.5
<class 'float'>
```

**Explicit conversion:** We manually convert a value using a function such as `int()` or `float()`.

```python
number = "50"
number = int(number)

print(number + 10)
```

Output:
```text
60
```

## Quick Revision

| Data type | Example | Main feature |
|---|---|---|
| `int` | `10` | Whole numbers |
| `float` | `10.5` | Decimal numbers |
| `complex` | `2 + 3j` | Real and imaginary parts |
| `str` | `"Python"` | Text; immutable |
| `list` | `[10, 20, 30]` | Ordered and mutable |
| `tuple` | `(10, 20, 30)` | Ordered and immutable |
| `dict` | `{"name": "Bunny"}` | Key-value pairs |
| `set` | `{10, 20, 30}` | Unique elements |

## What I Learned Today

- Python numeric types include integers, floats, and complex numbers.
- Strings store text and support indexing, slicing, and useful methods.
- Lists are mutable, while tuples are immutable.
- Dictionaries store values using keys.
- Sets automatically remove duplicates and support mathematical set operations.
- Type conversion helps us work with values in the required data type.
- `input()` returns a string, so numeric input often needs conversion before calculations.
