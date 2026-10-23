# Day 07 – Python Sets and Dictionaries

## 1. Introduction to Sets

A set is a Python collection used to store unique elements. Sets are mutable, do not support indexing, and do not guarantee a fixed order.

Sets are useful when we want to remove duplicate values or perform mathematical set operations.

### Creating a set

```python
fruits = {"apple", "banana", "mango"}

print(fruits)
print(type(fruits))
```

Output:

```text
{'apple', 'banana', 'mango'}
<class 'set'>
```

The order of elements in the output may vary.

### Sets remove duplicates

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

Duplicate values are stored only once.

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

### Adding elements

The `add()` method adds one element to a set.

```python
fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)
```

Output contains:

```text
{'apple', 'banana', 'mango'}
```

The display order may vary.

### Adding multiple elements

The `update()` method adds elements from another iterable.

```python
numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)
```

Output contains:

```text
{1, 2, 3, 4, 5, 6}
```

### Removing elements

```python
fruits = {"apple", "banana", "mango"}

fruits.remove("banana")
print(fruits)

fruits.discard("grapes")
print(fruits)
```

`remove()` raises a `KeyError` if the element does not exist. `discard()` does not raise an error when the element is missing.

### Sets do not support indexing

```python
numbers = {10, 20, 30}

# print(numbers[0])  # This causes a TypeError
```

Sets are unordered collections, so we cannot access their elements using positions such as `[0]`.

## 2. Set Operations

Set operations help compare collections, find common elements, and combine unique values.

Consider these two sets:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

### Union (`|`)

Union combines elements from both sets without duplicates.

```python
print(a | b)
print(a.union(b))
```

Output:

```text
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
```

### Intersection (`&`)

Intersection returns only the common elements.

```python
print(a & b)
print(a.intersection(b))
```

Output:

```text
{3, 4}
{3, 4}
```

### Difference (`-`)

Difference returns elements present in the first set but not in the second.

```python
print(a - b)
print(b - a)
```

Output:

```text
{1, 2}
{5, 6}
```

The order matters: `a - b` is different from `b - a`.

### Symmetric difference (`^`)

Symmetric difference returns elements found in either set, but not in both.

```python
print(a ^ b)
print(a.symmetric_difference(b))
```

Output:

```text
{1, 2, 5, 6}
{1, 2, 5, 6}
```

### Subset (`<=`)

A set is a subset if all its elements are present in another set.

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a <= b)
print(a.issubset(b))
```

Output:

```text
True
True
```

### Superset (`>=`)

A set is a superset if it contains all the elements of another set.

```python
a = {1, 2, 3, 4}
b = {1, 2}

print(a >= b)
print(a.issuperset(b))
```

Output:

```text
True
True
```

### Disjoint sets

Two sets are disjoint if they have no common elements.

```python
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))
```

Output:

```text
True
```

**Remember:** Set operations are useful for finding common items, removing duplicates, and comparing groups of data.

## 3. Set Functions and Methods

Python provides built-in functions and set methods for working with set elements.

### `len()`

Returns the number of unique elements in a set.

```python
numbers = {10, 20, 30, 20}

print(len(numbers))
```

Output:

```text
3
```

### `min()` and `max()`

Return the smallest and largest elements.

```python
numbers = {40, 10, 30, 20}

print(min(numbers))
print(max(numbers))
```

Output:

```text
10
40
```

These functions require elements that can be compared.

### `sum()`

Returns the sum of numeric set elements.

```python
numbers = {10, 20, 30}

print(sum(numbers))
```

Output:

```text
60
```

### `sorted()`

Returns a sorted list of the set elements.

```python
numbers = {40, 10, 30, 20}

result = sorted(numbers)

print(result)
print(type(result))
```

Output:

```text
[10, 20, 30, 40]
<class 'list'>
```

**Note:** `sorted()` returns a list, not a set.

### `pop()`

Removes and returns an arbitrary element from the set. It does not guarantee which element will be removed.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)
print(numbers)
```

The removed value can vary because sets do not guarantee a fixed order.

### `clear()`

Removes all elements from a set.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

Output:

```text
set()
```

### `copy()`

Creates a shallow copy of a set.

```python
original = {1, 2, 3}
new_set = original.copy()

new_set.add(4)

print(original)
print(new_set)
```

Output:

```text
{1, 2, 3}
{1, 2, 3, 4}
```

### Common set methods

| Method | Purpose |
|---|---|
| `add()` | Adds one element |
| `update()` | Adds elements from an iterable |
| `remove()` | Removes an element; raises an error if missing |
| `discard()` | Removes an element if present |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |
| `copy()` | Creates a shallow copy |
| `union()` | Combines elements |
| `intersection()` | Finds common elements |
| `difference()` | Finds elements in the first set only |
| `symmetric_difference()` | Finds elements that are not common |
| `issubset()` | Checks whether a set is a subset |
| `issuperset()` | Checks whether a set is a superset |
| `isdisjoint()` | Checks whether sets have no common elements |

## 4. Introduction to Dictionaries

A dictionary stores data as **key-value pairs**. Each key maps to a value.

Dictionaries are mutable, preserve insertion order in modern Python, and require unique keys. Keys must be hashable; common examples include strings, numbers, and tuples containing only hashable elements.

### Creating a dictionary

```python
student = {
    "name": "Bunny",
    "age": 21,
    "course": "Python"
}

print(student)
print(type(student))
```

Output:

```text
{'name': 'Bunny', 'age': 21, 'course': 'Python'}
<class 'dict'>
```

### Accessing values

We can access a value using its key.

```python
student = {
    "name": "Bunny",
    "age": 21,
    "course": "Python"
}

print(student["name"])
print(student["age"])
```

Output:

```text
Bunny
21
```

Using a key that does not exist with square brackets raises a `KeyError`.

### Using `get()`

The `get()` method safely retrieves a value. If the key is missing, it returns `None` by default.

```python
student = {"name": "Bunny"}

print(student.get("name"))
print(student.get("marks"))
print(student.get("marks", 0))
```

Output:

```text
Bunny
None
0
```

### Duplicate keys

Dictionary keys must be unique. If the same key is specified more than once, the last value is retained.

```python
student = {
    "name": "Bunny",
    "age": 20,
    "age": 21
}

print(student)
```

Output:

```text
{'name': 'Bunny', 'age': 21}
```

### Dictionary values can have different data types

```python
student = {
    "name": "Bunny",
    "age": 21,
    "marks": 89.5,
    "passed": True,
    "subjects": ["Python", "SQL"]
}

print(student)
```

A dictionary can store strings, numbers, Boolean values, lists, and other dictionaries as values.

## 5. Dictionary Operations

Dictionary operations help us add, update, access, delete, and iterate over key-value pairs.

### Adding a new key-value pair

```python
student = {"name": "Bunny", "age": 21}

student["city"] = "Hyderabad"

print(student)
```

Output:

```text
{'name': 'Bunny', 'age': 21, 'city': 'Hyderabad'}
```

### Updating a value

```python
student = {"name": "Bunny", "age": 21}

student["age"] = 22

print(student)
```

Output:

```text
{'name': 'Bunny', 'age': 22}
```

### Updating multiple values with `update()`

```python
student = {"name": "Bunny", "age": 21}

student.update({"age": 22, "city": "Hyderabad"})

print(student)
```

Output:

```text
{'name': 'Bunny', 'age': 22, 'city': 'Hyderabad'}
```

### Removing a key with `pop()`

```python
student = {"name": "Bunny", "age": 21, "city": "Hyderabad"}

age = student.pop("age")

print(age)
print(student)
```

Output:

```text
21
{'name': 'Bunny', 'city': 'Hyderabad'}
```

`pop()` removes the specified key and returns its value.

### Removing the last inserted pair with `popitem()`

```python
student = {"name": "Bunny", "age": 21}

item = student.popitem()

print(item)
print(student)
```

Output:

```text
('age', 21)
{'name': 'Bunny'}
```

In modern Python, `popitem()` removes and returns the last inserted key-value pair.

### Deleting a key with `del`

```python
student = {"name": "Bunny", "age": 21}

del student["age"]

print(student)
```

Output:

```text
{'name': 'Bunny'}
```

### Checking whether a key exists

The `in` operator checks dictionary keys by default.

```python
student = {"name": "Bunny", "age": 21}

print("name" in student)
print("marks" in student)
```

Output:

```text
True
False
```

To check dictionary values, use `values()`:

```python
student = {"name": "Bunny", "age": 21}

print("Bunny" in student.values())
```

Output:

```text
True
```

### Iterating through a dictionary

```python
student = {
    "name": "Bunny",
    "age": 21,
    "course": "Python"
}

for key in student:
    print(key, student[key])
```

Output:

```text
name Bunny
age 21
course Python
```

### Iterating through key-value pairs

The `items()` method provides each key and value together.

```python
student = {"name": "Bunny", "age": 21}

for key, value in student.items():
    print(f"{key}: {value}")
```

Output:

```text
name: Bunny
age: 21
```

### Merging dictionaries

The `|` operator can merge dictionaries in Python 3.9 and later. If keys overlap, the value from the right-hand dictionary takes precedence.

```python
a = {"name": "Bunny", "age": 21}
b = {"age": 22, "city": "Hyderabad"}

result = a | b

print(result)
```

Output:

```text
{'name': 'Bunny', 'age': 22, 'city': 'Hyderabad'}
```

## 6. Dictionary Functions and Methods

Python provides built-in functions and dictionary methods to inspect and manage key-value pairs.

### `len()`

Returns the number of key-value pairs.

```python
student = {"name": "Bunny", "age": 21, "course": "Python"}

print(len(student))
```

Output:

```text
3
```

### `keys()`

Returns a view of the dictionary's keys.

```python
student = {"name": "Bunny", "age": 21}

print(student.keys())
```

Output:

```text
dict_keys(['name', 'age'])
```

### `values()`

Returns a view of the dictionary's values.

```python
student = {"name": "Bunny", "age": 21}

print(student.values())
```

Output:

```text
dict_values(['Bunny', 21])
```

### `items()`

Returns a view of the key-value pairs.

```python
student = {"name": "Bunny", "age": 21}

print(student.items())
```

Output:

```text
dict_items([('name', 'Bunny'), ('age', 21)])
```

### `get()`

Returns the value for a key, or a default value if the key is missing.

```python
student = {"name": "Bunny"}

print(student.get("name"))
print(student.get("marks", 0))
```

Output:

```text
Bunny
0
```

### `setdefault()`

Returns the existing value for a key. If the key is missing, it inserts the key with the specified default value.

```python
student = {"name": "Bunny"}

result = student.setdefault("age", 21)

print(result)
print(student)
```

Output:

```text
21
{'name': 'Bunny', 'age': 21}
```

### `copy()`

Creates a shallow copy of the dictionary.

```python
original = {"name": "Bunny", "age": 21}
new_student = original.copy()

new_student["age"] = 22

print(original)
print(new_student)
```

Output:

```text
{'name': 'Bunny', 'age': 21}
{'name': 'Bunny', 'age': 22}
```

### `clear()`

Removes all key-value pairs.

```python
student = {"name": "Bunny", "age": 21}

student.clear()

print(student)
```

Output:

```text
{}
```

### `dict()`

The built-in `dict()` function creates a dictionary.

```python
student = dict(name="Bunny", age=21, course="Python")

print(student)
```

Output:

```text
{'name': 'Bunny', 'age': 21, 'course': 'Python'}
```

### `sorted()`

The `sorted()` function returns a list of sorted keys by default.

```python
student = {"zebra": 1, "apple": 2, "mango": 3}

print(sorted(student))
```

Output:

```text
['apple', 'mango', 'zebra']
```

### Common dictionary methods

| Method or function | Purpose |
|---|---|
| `len()` | Counts key-value pairs |
| `get()` | Retrieves a value safely |
| `keys()` | Returns dictionary keys |
| `values()` | Returns dictionary values |
| `items()` | Returns key-value pairs |
| `update()` | Adds or updates pairs |
| `pop()` | Removes a specified key and returns its value |
| `popitem()` | Removes and returns the last inserted pair |
| `setdefault()` | Retrieves a value or inserts a default |
| `copy()` | Creates a shallow copy |
| `clear()` | Removes all pairs |
| `dict()` | Creates a dictionary |
| `sorted()` | Returns a sorted list of keys by default |

## Sets vs Dictionaries – Quick Comparison

| Feature | Set | Dictionary |
|---|---|---|
| Stores | Unique elements | Key-value pairs |
| Syntax | `{1, 2, 3}` | `{"name": "Bunny"}` |
| Duplicates | Duplicate elements removed | Keys must be unique |
| Access by key | No | Yes |
| Mutable | Yes | Yes |
| Empty creation | `set()` | `{}` or `dict()` |
| Common use | Unique values and set operations | Structured data and lookups |

## What I Learned Today

- Sets store unique elements and automatically remove duplicates.
- Set operations include union, intersection, difference, and symmetric difference.
- Set methods help add, remove, copy, and compare elements.
- Dictionaries store data as key-value pairs.
- Dictionary operations help add, update, retrieve, and delete data.
- Dictionary methods such as `keys()`, `values()`, and `items()` help access stored information.
- Sets are useful for unique collections, while dictionaries are useful for structured information.
