# Day 04 – Python Operators

Operators are symbols or keywords used to perform operations on values and variables. Python has different types of operators for calculations, comparisons, logical conditions, and more.

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulus (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333333333333335
3
1
1000
```

**Important:** `/` performs regular division, while `//` performs floor division. For positive numbers, floor division removes the fractional part. For negative numbers, it rounds down toward negative infinity.

```python
print(7 // 2)
print(-7 // 2)
```

Output:

```text
3
-4
```

## 2. Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `10 == 10` | `True` |
| `!=` | Not equal to | `10 != 5` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal to | `10 >= 10` | `True` |
| `<=` | Less than or equal to | `5 <= 10` | `True` |

### Example

```python
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= 10)
print(b <= 5)
```

Output:

```text
False
True
True
False
True
True
```

### Real-world example

Suppose a student needs at least 35 marks to pass an exam.

```python
marks = 40

print(marks >= 35)
```

Output:

```text
True
```

**Remember:** `=` assigns a value, but `==` checks whether two values are equal.

## 3. Assignment Operators

Assignment operators assign values to variables or update their existing values.

| Operator | Example | Equivalent expression |
|---|---|---|
| `=` | `x = 10` | Assign `10` to `x` |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 2` | `x = x * 2` |
| `/=` | `x /= 2` | `x = x / 2` |
| `//=` | `x //= 2` | `x = x // 2` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 2` | `x = x ** 2` |

### Example

```python
x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x //= 4
print(x)
```

Output:

```text
15
12
24
6
```

### Multiple assignment

Python also supports assigning values to multiple variables in one statement.

```python
a, b = 10, 20

print(a)
print(b)
```

Output:

```text
10
20
```

**Remember:** Assignment operators make it easier to update a variable without repeating its name in a longer expression.

## 4. Logical Operators

Logical operators combine conditions or reverse a condition. They are commonly used in `if` statements.

Python has three logical operators: `and`, `or`, and `not`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | Both conditions must be true | `True and False` | `False` |
| `or` | At least one condition must be true | `True or False` | `True` |
| `not` | Reverses the truth value | `not True` | `False` |

### Example using `and`

Both conditions must be true.

```python
age = 21
has_id = True

print(age >= 18 and has_id)
```

Output:

```text
True
```

### Example using `or`

Only one condition needs to be true.

```python
is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)
```

Output:

```text
True
```

### Example using `not`

The `not` operator reverses a Boolean value.

```python
is_logged_in = False

print(not is_logged_in)
```

Output:

```text
True
```

**Remember:** `and` requires both conditions to be true, `or` requires at least one, and `not` reverses the result. Logical operators can also short-circuit, meaning they may skip evaluating the second condition.

## 5. Membership Operators

Membership operators check whether a value exists inside a sequence or collection, such as a string, list, tuple, or set.

The two membership operators are `in` and `not in`.

### Using `in`

Returns `True` if the value is found.

```python
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
print("grapes" in fruits)
```

Output:

```text
True
False
```

### Using `not in`

Returns `True` if the value is not found.

```python
fruits = ["apple", "banana", "mango"]

print("grapes" not in fruits)
print("apple" not in fruits)
```

Output:

```text
True
False
```

### Membership in a string

```python
message = "Welcome to Python"

print("Python" in message)
print("Java" in message)
```

Output:

```text
True
False
```

**Remember:** Membership operators check for the presence of a value. When used with dictionaries, `in` checks keys by default, not values.

## 6. Identity Operators

Identity operators check whether two variables refer to the same object in memory.

Python has two identity operators: `is` and `is not`.

- `is` returns `True` when both references point to the same object.
- `is not` returns `True` when they point to different objects.

### Example

```python
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a == c)
print(a is not c)
```

Output:

```text
True
False
True
True
```

Here, `b = a` makes `b` refer to the same list as `a`. The variable `c` refers to a separate list containing the same values.

### Difference between `is` and `==`

- `==` checks whether two objects have equal values.
- `is` checks whether they are the same object.

For example:

```python
x = [1, 2]
y = [1, 2]

print(x == y)
print(x is y)
```

Output:

```text
True
False
```

### Common use of `is`

Identity checks are especially useful when checking for `None`.

```python
result = None

print(result is None)
```

Output:

```text
True
```

**Remember:** Use `==` to compare values and `is` to compare object identity. Avoid using `is` as a replacement for `==` when comparing ordinary numbers or strings.

## 7. Bitwise Operators

Bitwise operators work on the binary representation of integers (their bits).

For example, the binary representation of `5` is `0101`, and the binary representation of `3` is `0011` when shown using four bits.

| Operator | Name | Meaning |
|---|---|---|
| `&` | Bitwise AND | A bit is `1` if both bits are `1` |
| `\|` | Bitwise OR | A bit is `1` if either bit is `1` |
| `^` | Bitwise XOR | A bit is `1` if the bits are different |
| `~` | Bitwise NOT | Inverts the bits |
| `<<` | Left shift | Shifts bits to the left |
| `>>` | Right shift | Shifts bits to the right |

### Bitwise AND (`&`)

```python
a = 5
b = 3

print(a & b)
```

Binary calculation:

```text
  0101
& 0011
------
  0001
```

Output:

```text
1
```

### Bitwise OR (`|`)

```python
a = 5
b = 3

print(a | b)
```

Binary calculation:

```text
  0101
| 0011
------
  0111
```

Output:

```text
7
```

### Bitwise XOR (`^`)

XOR produces `1` when the corresponding bits are different.

```python
print(5 ^ 3)
```

Output:

```text
6
```

### Bitwise NOT (`~`)

```python
print(~5)
```

Output:

```text
-6
```

In Python, `~x` is equivalent to `-x - 1` for integers.

### Left shift (`<<`)

```python
print(5 << 1)
```

Output:

```text
10
```

The bits are shifted one position to the left. For non-negative integers, shifting left by one position is equivalent to multiplying by two.

### Right shift (`>>`)

```python
print(5 >> 1)
```

Output:

```text
2
```

The bits are shifted one position to the right. For non-negative integers, shifting right by one position is equivalent to floor-dividing by two.

**Remember:** Bitwise operators are useful when working with binary data, flags, permissions, and low-level operations.

## Quick Revision

| Operator type | Operators | Purpose |
|---|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Mathematical calculations |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` | Compare values |
| Assignment | `=`, `+=`, `-=`, `*=`, etc. | Assign or update values |
| Logical | `and`, `or`, `not` | Combine or reverse conditions |
| Membership | `in`, `not in` | Check whether a value exists |
| Identity | `is`, `is not` | Check object identity |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` | Operate on integer bits |

## What I Learned Today

- Arithmetic operators help perform mathematical calculations.
- Comparison operators return `True` or `False`.
- Assignment operators make updating variables easier.
- Logical operators help combine conditions.
- Membership operators check whether a value exists in a collection.
- Identity operators check whether variables refer to the same object.
- Bitwise operators perform operations on the binary representation of integers.
