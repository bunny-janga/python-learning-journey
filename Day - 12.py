# Day 12 – Python Nested Loops and Patterns

## 1. Nested Loops

### What is a Nested Loop?

A nested loop is a loop inside another loop. The outer loop controls the main repetitions, while the inner loop runs completely for each iteration of the outer loop.

Nested loops are useful for printing patterns, working with rows and columns, and solving programming problems.

### Syntax

```python
for variable1 in sequence:
    for variable2 in sequence:
        # Code to execute
```

### Example 1: Nested For Loop

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()
```

**Output:**

```text
1 2 3
1 2 3
1 2 3
```

**Explanation:**
- The outer loop runs 3 times.
- For every outer-loop iteration, the inner loop runs 3 times.
- `end=" "` prints values on the same line with spaces.
- `print()` moves to the next line.

### Example 2: Multiplication Table Using Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()
```

**Output:**

```text
1 2 3
2 4 6
3 6 9
```

### Example 3: Nested While Loop

```python
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(j, end=" ")
        j += 1

    print()
    i += 1
```

**Output:**

```text
1 2 3
1 2 3
1 2 3
```

### Important Points
- A loop inside another loop is called a nested loop.
- The inner loop completes all its iterations for each outer-loop iteration.
- Nested loops are commonly used in pattern programs and matrix operations.

---

## 2. Loop Problems

Loops help us solve problems by repeating instructions until a task is completed.

### Example 1: Sum of Numbers from 1 to 10

```python
total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)
```

**Output:**

```text
Sum: 55
```

### Example 2: Multiplication Table

```python
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
```

**Output:**

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

### Example 3: Factorial of a Number

The factorial of a positive integer is the product of all positive integers from 1 up to that number.

For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.

```python
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)
```

**Output:**

```text
Factorial: 120
```

### Example 4: Count Digits in a Number

```python
num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits:", count)
```

**Output:**

```text
Number of digits: 5
```

### Example 5: Reverse a Number

```python
num = 1234
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)
```

**Output:**

```text
Reversed number: 4321
```

### Example 6: Check Whether a Number Is Prime

A prime number is a number greater than 1 that has exactly two positive divisors: 1 and itself.

```python
num = 7
is_prime = num > 1

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
```

**Output:**

```text
Prime number
```

---

## 3. Star Patterns

Star patterns use loops to print stars in different shapes. Nested loops are commonly used to control the number of stars and rows.

### Example 1: Right-Angled Triangle

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

### Example 2: Inverted Triangle

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Output:**

```text
* * * * *
* * * *
* * *
* *
*
```

### Example 3: Square Pattern

```python
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
```

**Output:**

```text
* * * *
* * * *
* * * *
* * * *
```

### Example 4: Pyramid Pattern

```python
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
```

**Output:**

```text
    *
   * *
  * * *
 * * * *
* * * * *
```

### Example 5: Right-Aligned Triangle

```python
rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
```

**Output:**

```text
    *
   * *
  * * *
 * * * *
* * * * *
```

### Important Points
- The outer loop controls the number of rows.
- The inner loop controls the number of stars.
- Spaces help align patterns.
- Changing the loop range changes the shape of the pattern.

---

## 4. Number Patterns

Number patterns use loops to display numbers in different arrangements.

### Example 1: Increasing Number Triangle

```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**Output:**

```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

### Example 2: Repeated Number Triangle

```python
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
```

**Output:**

```text
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

### Example 3: Inverted Number Triangle

```python
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**Output:**

```text
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

### Example 4: Sequential Number Triangle

```python
num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

**Output:**

```text
1
2 3
4 5 6
7 8 9 10
```

### Example 5: Number Square

```python
for i in range(1, 5):
    for j in range(1, 5):
        print(i, end=" ")
    print()
```

**Output:**

```text
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

---

## Summary

- **Nested Loops:** A loop inside another loop.
- **Loop Problems:** Use loops to calculate sums, factorials, multiplication tables, and more.
- **Star Patterns:** Use loops and spaces to print different shapes with stars.
- **Number Patterns:** Use loops to display numbers in rows and columns.

Nested loops and pattern programs improve logical thinking and help build a strong foundation for problem-solving in Python.
