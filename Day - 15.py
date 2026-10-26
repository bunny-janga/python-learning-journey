# Day 15: Lambda Functions, Filter, Map, and Reduce in Python

## 1. Anonymous Functions

### What is an Anonymous Function?

An anonymous function is a function without a regular name. In Python, anonymous functions are created using the `lambda` keyword.

Unlike normal functions defined with `def`, lambda functions are generally used for short operations that can be written in a single expression.

### Example

```python
square = lambda number: number * number

print(square(5))
print(square(8))
```

**Output:**

```text
25
64
```

In this example, the lambda function takes a number and returns its square.

### Anonymous Function vs Normal Function

**Normal function:**

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

**Lambda function:**

```python
add = lambda a, b: a + b

print(add(10, 20))
```

**Output:**

```text
30
```

Both examples produce the same result. Lambda is useful when a short function is needed.

---

## 2. Lambda Syntax

### Syntax

```python
lambda arguments: expression
```

The syntax contains three parts:

- `lambda`: Keyword used to create a lambda function.
- `arguments`: Values received by the function.
- `expression`: A single expression whose result is returned automatically.

Lambda functions do not require an explicit `return` statement.

### Example 1: No Arguments

```python
message = lambda: "Welcome to Python"

print(message())
```

**Output:**

```text
Welcome to Python
```

### Example 2: One Argument

```python
double = lambda number: number * 2

print(double(10))
```

**Output:**

```text
20
```

### Example 3: Multiple Arguments

```python
multiply = lambda a, b: a * b

print(multiply(4, 5))
```

**Output:**

```text
20
```

### Example 4: Conditional Expression

```python
check_number = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check_number(8))
print(check_number(7))
```

**Output:**

```text
Even
Odd
```

**Remember:** A lambda function contains only one expression. That expression can include calculations, comparisons, and conditional expressions, but it cannot contain ordinary multi-statement function logic.

---

## 3. Lambda Examples

Lambda functions are especially useful when a small function is needed temporarily or passed to another function.

### Example 1: Find the Square

```python
square = lambda n: n ** 2

print(square(6))
```

**Output:**

```text
36
```

### Example 2: Find the Largest Number

```python
maximum = lambda a, b: a if a > b else b

print(maximum(25, 40))
```

**Output:**

```text
40
```

### Example 3: Sort Numbers by Their Last Digit

```python
numbers = [23, 11, 35, 42, 18]

numbers.sort(key=lambda number: number % 10)

print(numbers)
```

**Output:**

```text
[11, 42, 23, 35, 18]
```

The `key` argument tells Python to sort the numbers using their last digit instead of their complete values.

### Example 4: Sort Names by Length

```python
names = ["Ravi", "Anusha", "Sai", "Krishna"]

names.sort(key=lambda name: len(name))

print(names)
```

**Output:**

```text
['Sai', 'Ravi', 'Anusha', 'Krishna']
```

Here, `len(name)` determines the sorting order.

---

## 4. Filter Function

### What is `filter()`?

The `filter()` function selects elements from an iterable based on a condition.

It keeps only the elements for which the supplied function returns a truthy value.

### Syntax

```python
filter(function, iterable)
```

- `function`: A function that checks each element.
- `iterable`: A collection such as a list or tuple.
- `filter()` returns a filter iterator, so we often convert it into a list to see the results.

### Example 1: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print(even_numbers)
```

**Output:**

```text
[2, 4, 6, 8]
```

The lambda expression returns `True` for even numbers, so `filter()` keeps those numbers.

### Example 2: Filter Numbers Greater Than 10

```python
numbers = [5, 12, 8, 20, 15, 3]

result = list(filter(lambda n: n > 10, numbers))

print(result)
```

**Output:**

```text
[12, 20, 15]
```

### Example 3: Filter Names Starting with A

```python
names = ["Anu", "Ravi", "Arjun", "Kiran", "Akhil"]

result = list(filter(lambda name: name.startswith("A"), names))

print(result)
```

**Output:**

```text
['Anu', 'Arjun', 'Akhil']
```

### When to Use `filter()`

Use `filter()` when you want to keep only the elements that satisfy a condition.

---

## 5. Map Function

### What is `map()`?

The `map()` function applies a function to every element in an iterable and produces the transformed results.

Unlike `filter()`, which selects elements, `map()` transforms elements.

### Syntax

```python
map(function, iterable)
```

The result is a map iterator. Convert it to a list when you want to display all the results at once.

### Example 1: Square Every Number

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n ** 2, numbers))

print(squares)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

### Example 2: Convert Numbers to Strings

```python
numbers = [10, 20, 30, 40]

result = list(map(str, numbers))

print(result)
```

**Output:**

```text
['10', '20', '30', '40']
```

### Example 3: Convert Temperatures from Celsius to Fahrenheit

Formula:

`Fahrenheit = (Celsius × 9 / 5) + 32`

```python
celsius = [0, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celsius))

print(fahrenheit)
```

**Output:**

```text
[32.0, 68.0, 86.0, 104.0]
```

### When to Use `map()`

Use `map()` when you want to apply the same operation to every element in a collection.

---

## 6. Reduce Function

### What is `reduce()`?

The `reduce()` function repeatedly combines elements of an iterable to produce a single final result.

Unlike `filter()` and `map()`, `reduce()` is available through the `functools` module, so it must be imported before use.

### Syntax

```python
from functools import reduce

reduce(function, iterable)
```

You can also supply an optional initial value:

```python
reduce(function, iterable, initial_value)
```

### Example 1: Find the Sum of Numbers

```python
from functools import reduce

numbers = [10, 20, 30, 40]

total = reduce(lambda a, b: a + b, numbers)

print(total)
```

**Output:**

```text
100
```

### How It Works

```text
10 + 20 = 30
30 + 30 = 60
60 + 40 = 100
```

The final result is `100`.

### Example 2: Find the Product of Numbers

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print(product)
```

**Output:**

```text
120
```

### Example 3: Find the Largest Number

```python
from functools import reduce

numbers = [12, 45, 7, 89, 32]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print(largest)
```

**Output:**

```text
89
```

### Example 4: Reduce with an Initial Value

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers, 10)

print(total)
```

**Output:**

```text
20
```

The initial value `10` is added to the sum of the list elements.

### When to Use `reduce()`

Use `reduce()` when you need to combine a sequence into one result, such as a total or product. For simple sums, Python's built-in `sum()` is usually clearer.

---

## Difference Between `filter()`, `map()`, and `reduce()`

| Function | Purpose | Result |
|---|---|---|
| `filter()` | Selects elements based on a condition | Iterator of selected elements |
| `map()` | Transforms each element | Iterator of transformed elements |
| `reduce()` | Combines elements repeatedly | One final value |

### Quick Comparison

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Filter: Keep even numbers
even = list(filter(lambda n: n % 2 == 0, numbers))

# Map: Double every number
doubled = list(map(lambda n: n * 2, numbers))

# Reduce: Add all numbers
total = reduce(lambda a, b: a + b, numbers)

print(even)
print(doubled)
print(total)
```

**Output:**

```text
[2, 4, 6]
[2, 4, 6, 8, 10, 12]
21
```

## Day 15 Summary

- Anonymous functions are functions without a regular declared name.
- The `lambda` keyword creates a short function containing one expression.
- `filter()` selects elements that satisfy a condition.
- `map()` transforms every element in an iterable.
- `reduce()` combines elements into a single result.
- `filter()` and `map()` are built into Python.
- `reduce()` must be imported from `functools`.
- Use lambda functions for short, simple operations; use `def` for more complex logic.
