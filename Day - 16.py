# Day 16: List Comprehensions, Generators, Yield, and Next in Python

## 1. List Comprehensions

### What is a List Comprehension?

List comprehension is a short and convenient way to create a new list from an existing iterable, such as a list, range, or string.

It allows us to write a loop and an optional condition in a single line instead of using multiple lines of code.

### Syntax

```python
[expression for item in iterable]
```

With a condition:

```python
[expression for item in iterable if condition]
```

### Example 1: Create a List of Numbers

```python
numbers = [number for number in range(1, 6)]

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

### Example 2: Find Squares of Numbers

```python
squares = [number ** 2 for number in range(1, 6)]

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

The expression `number ** 2` calculates the square of each number.

### Example 3: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

**Output:**

```text
[2, 4, 6, 8]
```

Only numbers satisfying the condition are included in the new list.

### Example 4: Convert Words to Uppercase

```python
names = ["ravi", "anu", "krishna"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)
```

**Output:**

```text
['RAVI', 'ANU', 'KRISHNA']
```

### Example 5: Use an If-Else Expression

```python
numbers = [1, 2, 3, 4, 5]

results = ["Even" if number % 2 == 0 else "Odd"
           for number in numbers]

print(results)
```

**Output:**

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

**Remember:** The `if` at the end filters elements. An `if-else` expression before the `for` chooses what value to put into the list.

---

## 2. Nested Comprehensions

### What is a Nested Comprehension?

A nested comprehension is a comprehension that contains more than one `for` clause. It is useful when working with nested loops, such as lists of lists or combinations of values.

### Example 1: Nested Loops

Using regular loops:

```python
pairs = []

for i in range(1, 3):
    for j in range(1, 3):
        pairs.append((i, j))

print(pairs)
```

**Output:**

```text
[(1, 1), (1, 2), (2, 1), (2, 2)]
```

The same result using a nested list comprehension:

```python
pairs = [(i, j) for i in range(1, 3)
                 for j in range(1, 3)]

print(pairs)
```

**Output:**

```text
[(1, 1), (1, 2), (2, 1), (2, 2)]
```

The first `for` loop runs first. For each value of `i`, the second loop goes through all values of `j`.

### Example 2: Flatten a Nested List

```python
matrix = [[1, 2], [3, 4], [5, 6]]

numbers = [number for row in matrix for number in row]

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5, 6]
```

The nested list is converted into a single list.

### Example 3: Create a Multiplication Table

```python
table = [i * j for i in range(1, 4)
                for j in range(1, 4)]

print(table)
```

**Output:**

```text
[1, 2, 3, 2, 4, 6, 3, 6, 9]
```

This creates the multiplication results for numbers from 1 to 3.

**Note:** Nested comprehensions are useful, but if the logic becomes difficult to read, normal nested loops may be a better choice.

---

## 3. Generators

### What is a Generator?

A generator is a special type of iterator that produces values one at a time instead of storing all the results in memory at once.

Generators are useful when working with large amounts of data because values can be produced only when needed.

A generator can be created using:

- A generator function with the `yield` keyword.
- A generator expression using parentheses.

### Example 1: Generator Expression

```python
numbers = (number for number in range(1, 6))

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

**Output:**

```text
1
2
3
```

The generator produces one value each time `next()` is called.

### Example 2: Using a Generator in a Loop

```python
numbers = (number ** 2 for number in range(1, 6))

for number in numbers:
    print(number)
```

**Output:**

```text
1
4
9
16
25
```

The generator produces each square as the loop requests it.

### Example 3: Generator Function

```python
def count_numbers():
    for number in range(1, 6):
        yield number

for value in count_numbers():
    print(value)
```

**Output:**

```text
1
2
3
4
5
```

The `yield` keyword makes this function a generator function.

---

## 4. Yield Keyword

### What is `yield`?

The `yield` keyword returns a value from a generator function while preserving its execution state.

When the generator is requested to produce another value, execution continues from where it previously paused.

Unlike `return`, which ends a function call, `yield` pauses the generator temporarily.

### Example 1: Using Yield

```python
def numbers():
    yield 10
    yield 20
    yield 30

for number in numbers():
    print(number)
```

**Output:**

```text
10
20
30
```

Each `yield` produces one value.

### Example 2: Yield with a Loop

```python
def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number

for value in even_numbers(10):
    print(value)
```

**Output:**

```text
2
4
6
8
10
```

This generator produces even numbers up to the given limit.

### Example 3: Compare Return and Yield

Using `return`:

```python
def get_number():
    return 10

print(get_number())
```

**Output:**

```text
10
```

Using `yield`:

```python
def get_numbers():
    yield 10
    yield 20

for number in get_numbers():
    print(number)
```

**Output:**

```text
10
20
```

The first function returns a single value and finishes. The second produces values one at a time.

**Remember:** A generator does not automatically save every generated value in a list. If you need all values together, you can convert it using `list(generator)`.

---

## 5. Next Keyword

### What is `next()`?

The built-in `next()` function retrieves the next value from an iterator or generator.

Each call advances the iterator by one item. When no values remain, `next()` raises `StopIteration`, unless a default value is provided.

### Syntax

```python
next(iterator)
```

With a default value:

```python
next(iterator, default_value)
```

### Example 1: Using Next with a Generator

```python
def numbers():
    yield 100
    yield 200
    yield 300

values = numbers()

print(next(values))
print(next(values))
print(next(values))
```

**Output:**

```text
100
200
300
```

Each call returns the next available value.

### Example 2: Next with a Default Value

```python
numbers = iter([10, 20])

print(next(numbers))
print(next(numbers))
print(next(numbers, "No more values"))
```

**Output:**

```text
10
20
No more values
```

After the two numbers have been consumed, the third call returns the supplied default instead of raising `StopIteration`.

### Example 3: Exhausted Iterator

```python
numbers = iter([1])

print(next(numbers))

# This would raise StopIteration:
# print(next(numbers))
```

**Output:**

```text
1
```

The iterator has only one value. Calling `next()` again without a default would raise `StopIteration`.

**Remember:** `next()` works with iterators. If you have a list, use `iter()` first when you want to retrieve its values one by one with `next()`.

---

## 6. Difference Between Functions and Generators

Both functions and generators help us organize code, but they handle results differently.

| Feature | Normal Function | Generator Function |
|---|---|---|
| Keyword | Usually uses `def` and `return` | Uses `def` and `yield` |
| Result | Returns a value or object | Returns a generator object |
| Execution | Runs until it returns or raises an exception | Pauses at each `yield` and resumes later |
| Values | Can return one result, including a collection | Can produce multiple values one at a time |
| Memory | May store a complete result in memory | Can avoid storing all generated values |
| Access | Call the function to obtain its result | Iterate over it or use `next()` |
| Best use | Calculations and returning results | Processing sequences of values as needed |

### Example: Normal Function

```python
def get_numbers():
    return [1, 2, 3, 4, 5]

numbers = get_numbers()

print(numbers)
```

**Output:**

```text
[1, 2, 3, 4, 5]
```

The function returns a list containing all five numbers.

### Example: Generator Function

```python
def generate_numbers():
    for number in range(1, 6):
        yield number

numbers = generate_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

**Output:**

```text
1
2
3
```

The generator produces values as they are requested, rather than creating a complete list first.

### When Should You Use Each?

Use a normal function when you need to calculate and return a result, such as the total price of items.

Use a generator when you need to process a sequence one value at a time, such as reading a large file line by line.

**Important:** Generators can reduce memory usage when values are consumed one at a time, but they are not automatically faster or better for every situation.

---

## Day 16 Summary

| Concept | Meaning |
|---|---|
| List Comprehension | Creates a list in a concise way |
| Nested Comprehension | Uses multiple `for` clauses in a comprehension |
| Generator | Produces values one at a time |
| `yield` | Produces a value and pauses generator execution |
| `next()` | Retrieves the next value from an iterator |
| Normal Function | Runs and returns a result |
| Generator Function | Produces a generator that can yield multiple values |

### Key Takeaways

- List comprehensions are useful for creating and filtering lists.
- Nested comprehensions can simplify nested loops.
- Generators produce values as they are needed.
- The `yield` keyword pauses and resumes generator execution.
- The `next()` function retrieves one value at a time.
- An exhausted iterator raises `StopIteration` unless a default is supplied.
- Choose comprehensions and generators when they make the code clearer, not simply to make it shorter.
