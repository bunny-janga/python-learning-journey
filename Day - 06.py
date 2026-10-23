# Day 06 – Python Lists and Tuples

## 1. Introduction to Lists

A list is a Python data type used to store multiple items in a single variable. Lists are **ordered, mutable, and allow duplicate values**. They can contain different data types.

### Creating a list

```python
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40]
mixed = ["Bunny", 21, 85.5, True]

print(fruits)
print(numbers)
print(mixed)
```

Output:

```text
['apple', 'banana', 'mango']
[10, 20, 30, 40]
['Bunny', 21, 85.5, True]
```

### Accessing list elements

List indexing starts at `0`. Negative indexing starts at `-1` from the end.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
```

Output:

```text
apple
banana
mango
```

### List slicing

Slicing retrieves a portion of a list using `list[start:stop:step]`.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

Output:

```text
[20, 30, 40]
[10, 20, 30]
[30, 40, 50]
[50, 40, 30, 20, 10]
```

The `stop` index is not included.

### Lists are mutable

Mutable means we can change, add, or remove list elements after creating a list.

```python
colors = ["red", "green", "blue"]

colors[1] = "yellow"

print(colors)
```

Output:

```text
['red', 'yellow', 'blue']
```

### Lists allow duplicates

```python
numbers = [10, 20, 10, 30, 20]

print(numbers)
```

Output:

```text
[10, 20, 10, 30, 20]
```

**Remember:** Lists use square brackets `[]` and are useful when a collection of values may need to change.

## 2. List Operations

List operations help us combine lists, repeat elements, check membership, and update values.

### Concatenation (`+`)

The `+` operator combines two lists into a new list.

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = a + b

print(result)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

### Repetition (`*`)

The `*` operator repeats the elements of a list.

```python
numbers = [1, 2]

print(numbers * 3)
```

Output:

```text
[1, 2, 1, 2, 1, 2]
```

### Membership (`in` and `not in`)

These operators check whether an element exists in a list.

```python
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
print("grapes" not in fruits)
```

Output:

```text
True
True
```

### Updating elements

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

### Adding elements

Python provides several ways to add elements to a list.

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

- `append()` adds one item at the end.
- `insert()` adds an item at a specified index.

### Extending a list

The `extend()` method adds elements from another iterable.

```python
a = [1, 2]
b = [3, 4]

a.extend(b)

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

### Removing elements

```python
fruits = ["apple", "banana", "mango", "orange"]

fruits.remove("banana")
print(fruits)

fruits.pop()
print(fruits)

del fruits[0]
print(fruits)
```

Output:

```text
['apple', 'mango', 'orange']
['apple', 'mango']
['mango']
```

- `remove(value)` removes the first matching value.
- `pop(index)` removes and returns an item; without an index, it removes the last item.
- `del` removes an item or a selected portion of a list.

### List copying

Assigning one list to another variable does not create a separate list. Both variables refer to the same object.

```python
a = [10, 20, 30]
b = a

b[0] = 100

print(a)
print(b)
```

Output:

```text
[100, 20, 30]
[100, 20, 30]
```

To create a separate shallow copy, use `copy()`.

```python
a = [10, 20, 30]
b = a.copy()

b[0] = 100

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[100, 20, 30]
```

**Remember:** List operations make it easy to modify collections of data. Use `copy()` when you need a separate list rather than another reference to the same list.

## 3. List Functions and Methods

Python provides built-in functions and list methods to find the length, calculate values, sort items, and search for elements.

### `len()`

Returns the number of elements in a list.

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

Output:

```text
4
```

### `max()` and `min()`

Return the largest and smallest elements.

```python
numbers = [40, 10, 30, 20]

print(max(numbers))
print(min(numbers))
```

Output:

```text
40
10
```

### `sum()`

Returns the total of numeric elements.

```python
numbers = [10, 20, 30, 40]

print(sum(numbers))
```

Output:

```text
100
```

### `sorted()`

Returns a new sorted list without changing the original list.

```python
numbers = [40, 10, 30, 20]

result = sorted(numbers)

print(result)
print(numbers)
```

Output:

```text
[10, 20, 30, 40]
[40, 10, 30, 20]
```

### `sort()`

Sorts the original list in place.

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

To sort in descending order:

```python
numbers = [10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

### `reverse()`

Reverses the order of elements in the original list.

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

### `index()`

Returns the index of the first matching element.

```python
fruits = ["apple", "banana", "mango"]

print(fruits.index("banana"))
```

Output:

```text
1
```

If the value is not found, `index()` raises a `ValueError`.

### `count()`

Counts how many times a value appears.

```python
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

Output:

```text
3
```

### `clear()`

Removes all elements from the list.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

### `copy()`

Creates a shallow copy of a list.

```python
original = [1, 2, 3]
new_list = original.copy()

print(new_list)
```

Output:

```text
[1, 2, 3]
```

### Common list methods at a glance

| Method | Purpose |
|---|---|
| `append()` | Adds one item at the end |
| `extend()` | Adds items from an iterable |
| `insert()` | Adds an item at a given index |
| `remove()` | Removes the first matching value |
| `pop()` | Removes and returns an item |
| `clear()` | Removes all items |
| `index()` | Finds the first matching index |
| `count()` | Counts matching values |
| `sort()` | Sorts the original list |
| `reverse()` | Reverses the original list |
| `copy()` | Creates a shallow copy |

**Remember:** Methods such as `sort()`, `reverse()`, and `append()` modify the list and usually return `None`. The built-in `sorted()` function returns a new sorted list.

## 4. Introduction to Tuples

A tuple is a collection used to store multiple values in one variable. Tuples are **ordered, immutable, and allow duplicate values**.

### Creating a tuple

```python
fruits = ("apple", "banana", "mango")
numbers = (10, 20, 30)
mixed = ("Bunny", 21, True)

print(fruits)
print(numbers)
print(mixed)
```

Output:

```text
('apple', 'banana', 'mango')
(10, 20, 30)
('Bunny', 21, True)
```

### Creating a single-element tuple

A comma is required when creating a tuple containing one item.

```python
value = (10,)

print(value)
print(type(value))
```

Output:

```text
(10,)
<class 'tuple'>
```

Without the comma, `(10)` is an integer inside parentheses, not a tuple.

### Accessing tuple elements

Tuples support positive and negative indexing.

```python
colors = ("red", "green", "blue")

print(colors[0])
print(colors[1])
print(colors[-1])
```

Output:

```text
red
green
blue
```

### Tuple slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[::-1])
```

Output:

```text
(20, 30, 40)
(10, 20, 30)
(50, 40, 30, 20, 10)
```

### Tuples are immutable

Tuple elements cannot be reassigned after the tuple is created.

```python
colors = ("red", "green", "blue")

# colors[0] = "yellow"  # This causes a TypeError

print(colors)
```

Output:

```text
('red', 'green', 'blue')
```

If you need to change the contents, you can create a new tuple or convert it to a list, modify the list, and convert it back.

```python
colors = ("red", "green", "blue")

temp = list(colors)
temp[0] = "yellow"
colors = tuple(temp)

print(colors)
```

Output:

```text
('yellow', 'green', 'blue')
```

### Tuple packing and unpacking

Packing means placing multiple values into a tuple. Unpacking means assigning tuple elements to separate variables.

```python
student = ("Bunny", 21, "Python")

name, age, course = student

print(name)
print(age)
print(course)
```

Output:

```text
Bunny
21
Python
```

The number of variables must match the number of elements unless extended unpacking is used.

**Remember:** Tuples use parentheses `()` by convention and are useful for collections that should not be structurally changed.

## 5. Tuple Operations

Tuples support operations such as concatenation, repetition, membership checking, indexing, and slicing.

### Concatenation (`+`)

The `+` operator combines tuples into a new tuple.

```python
a = (1, 2, 3)
b = (4, 5, 6)

result = a + b

print(result)
```

Output:

```text
(1, 2, 3, 4, 5, 6)
```

### Repetition (`*`)

The `*` operator repeats tuple elements.

```python
numbers = (1, 2)

print(numbers * 3)
```

Output:

```text
(1, 2, 1, 2, 1, 2)
```

### Membership (`in` and `not in`)

```python
fruits = ("apple", "banana", "mango")

print("apple" in fruits)
print("grapes" not in fruits)
```

Output:

```text
True
True
```

### Finding the length

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

Output:

```text
4
```

### Comparing tuples

Tuples can be compared element by element when their corresponding values support comparison.

```python
a = (1, 2, 3)
b = (1, 2, 4)

print(a == b)
print(a < b)
```

Output:

```text
False
True
```

Python compares the first pair of unequal elements to determine the ordering.

### Iterating through a tuple

A `for` loop can access each element in sequence.

```python
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
mango
```

### Tuple immutability and nested values

A tuple cannot have its elements reassigned, but if it contains a mutable object such as a list, that inner object can still change.

```python
data = (10, [20, 30])

data[1].append(40)

print(data)
```

Output:

```text
(10, [20, 30, 40])
```

The tuple still references the same inner list; the list itself was modified.

**Remember:** Tuples support many of the same reading and combining operations as lists, but their elements cannot be reassigned.

## 6. Tuple Functions and Methods

Python provides built-in functions and two main tuple methods for working with tuple data.

### `len()`

Returns the number of elements.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))
```

Output:

```text
4
```

### `max()` and `min()`

Return the largest and smallest elements.

```python
numbers = (40, 10, 30, 20)

print(max(numbers))
print(min(numbers))
```

Output:

```text
40
10
```

### `sum()`

Returns the total of numeric tuple elements.

```python
numbers = (10, 20, 30, 40)

print(sum(numbers))
```

Output:

```text
100
```

### `sorted()`

Returns a sorted **list**, not a tuple.

```python
numbers = (40, 10, 30, 20)

result = sorted(numbers)

print(result)
print(type(result))
```

Output:

```text
[10, 20, 30, 40]
<class 'list'>
```

If a sorted tuple is needed, convert the result back:

```python
numbers = (40, 10, 30, 20)

result = tuple(sorted(numbers))

print(result)
```

Output:

```text
(10, 20, 30, 40)
```

### `count()`

Returns the number of occurrences of a value.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

Output:

```text
3
```

### `index()`

Returns the index of the first matching element.

```python
fruits = ("apple", "banana", "mango")

print(fruits.index("mango"))
```

Output:

```text
2
```

If the value is missing, `index()` raises a `ValueError`.

### Converting a tuple to a list

```python
numbers = (10, 20, 30)

result = list(numbers)

print(result)
print(type(result))
```

Output:

```text
[10, 20, 30]
<class 'list'>
```

### Converting a list to a tuple

```python
fruits = ["apple", "banana", "mango"]

result = tuple(fruits)

print(result)
print(type(result))
```

Output:

```text
('apple', 'banana', 'mango')
<class 'tuple'>
```

### Tuple methods at a glance

| Method | Purpose |
|---|---|
| `count()` | Counts occurrences of a value |
| `index()` | Finds the first matching index |

Tuples have fewer methods than lists because they cannot be modified after creation.

## Lists vs Tuples – Quick Comparison

| Feature | List | Tuple |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Ordered | Yes | Yes |
| Mutable | Yes | No |
| Duplicates allowed | Yes | Yes |
| Can access by index | Yes | Yes |
| Methods to add/remove elements | Yes | No |
| Common use | Data that changes | Data that should remain structurally fixed |

## What I Learned Today

- Lists store multiple values and can be changed after creation.
- List operations include concatenation, repetition, membership, indexing, and slicing.
- List functions and methods help count, sort, search, add, and remove elements.
- Tuples store ordered values but do not allow their elements to be reassigned.
- Tuple packing and unpacking help organize and retrieve multiple values.
- Tuples support indexing, slicing, concatenation, repetition, and membership checks.
- Tuple methods include `count()` and `index()`.
- `sorted()` returns a list even when its input is a tuple.
