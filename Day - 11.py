# Day 11 – Python While Loop and While with Else

## 1. WHILE Loop

### What is a While Loop?

A `while` loop is used to execute a block of code repeatedly as long as a given condition is `True`.

When the condition becomes `False`, the loop stops.

### Syntax

```python
while condition:
    # Code to execute
```

### Example 1: Print Numbers from 1 to 5

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

**Output:**
```text
1
2
3
4
5
```

**Explanation:**
- `i = 1` initializes the variable.
- `i <= 5` checks the condition.
- `print(i)` displays the current value.
- `i += 1` increases the value by 1.
- When `i` becomes 6, the condition is `False`, and the loop stops.

### Example 2: Print Even Numbers

```python
i = 2

while i <= 10:
    print(i)
    i += 2
```

**Output:**
```text
2
4
6
8
10
```

### Example 3: Calculate the Sum of Numbers from 1 to 5

```python
i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Total:", total)
```

**Output:**
```text
Total: 15
```

### Important Points
- A `while` loop checks its condition before every iteration.
- The loop runs only while the condition is `True`.
- Update the loop variable when necessary to avoid an infinite loop.
- The `break` statement can stop a loop immediately.

---

## 2. WHILE with ELSE

### What is While with Else?

In Python, a `while` loop can have an `else` block. The `else` block executes when the loop finishes normally because its condition becomes `False`.

If the loop stops using `break`, the `else` block is skipped.

### Syntax

```python
while condition:
    # Loop code
else:
    # Code executed after normal completion
```

### Example 1: While Loop Finishes Normally

```python
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed")
```

**Output:**
```text
1
2
3
Loop completed
```

**Explanation:**

The loop prints numbers from 1 to 3. When `i` becomes 4, the condition becomes `False`, so the `else` block executes.

### Example 2: While with Else and Break

```python
i = 1

while i <= 5:
    print(i)

    if i == 3:
        break

    i += 1
else:
    print("Loop completed")
```

**Output:**
```text
1
2
3
```

**Explanation:**

When `i` becomes 3, `break` immediately terminates the loop. Therefore, the `else` block does not execute.

### Example 3: Search for a Number

```python
numbers = [10, 20, 30, 40]
target = 30
i = 0

while i < len(numbers):
    if numbers[i] == target:
        print("Number found")
        break
    i += 1
else:
    print("Number not found")
```

**Output:**
```text
Number found
```

If `target = 50`, the loop finishes normally, and the output becomes:

```text
Number not found
```

### Difference Between While and While-Else

| While Loop | While-Else Loop |
|---|---|
| Repeats while the condition is `True`. | Repeats while the condition is `True` and supports an `else` block. |
| Stops when the condition becomes `False` or `break` executes. | The `else` block runs only if the loop finishes without `break`. |
| Useful for repetition and counting. | Useful for searching and handling normal loop completion. |

---

## Summary

- A `while` loop repeats code while a condition is `True`.
- Always update the condition-related variable when needed.
- A `while-else` loop executes its `else` block after normal completion.
- The `else` block does not execute when the loop terminates using `break`.
