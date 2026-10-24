# Day 10: Python Loops and Control Statements

## 1. FOR Loop

A `for` loop is used to execute a block of code repeatedly for each item in a sequence. A sequence can be a list, tuple, string, or a range of numbers.

The `for` loop helps reduce repeated code and makes programs easier to read.

### Syntax

```python
for variable in sequence:
    # Code to execute
```

### Example 1: Printing Numbers

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

### Explanation

The `range(1, 6)` function generates numbers from 1 to 5. The ending value, 6, is excluded. The loop executes once for each number.

### Example 2: Iterating Through a String

```python
name = "Python"

for letter in name:
    print(letter)
```

### Output

```text
P
y
t
h
o
n
```

### Explanation

The loop accesses each character in the string and prints it on a separate line.

### Example 3: Calculating the Sum of Numbers

```python
total = 0

for i in range(1, 6):
    total = total + i

print("Total:", total)
```

### Output

```text
Total: 15
```

### Explanation

The loop adds the numbers from 1 to 5. The final sum is 15.

---

## 2. FOR with ELSE

Python allows an `else` block to be used with a `for` loop. The `else` block executes when the loop finishes normally without being terminated by a `break` statement.

### Syntax

```python
for variable in sequence:
    # Loop statements
else:
    # Executes after normal loop completion
```

### Example 1: Loop with ELSE

```python
for i in range(1, 4):
    print(i)
else:
    print("Loop completed.")
```

### Output

```text
1
2
3
Loop completed.
```

### Explanation

The loop prints the numbers 1, 2, and 3. Since the loop finishes normally, the `else` block also executes.

### Example 2: Searching for a Number

```python
numbers = [10, 20, 30, 40]
target = 25

for number in numbers:
    if number == target:
        print("Number found.")
        break
else:
    print("Number not found.")
```

### Output

```text
Number not found.
```

### Explanation

The loop checks each item in the list. Since 25 is not present, the loop finishes without a `break`, and the `else` block executes.

**Important:** The `else` block associated with a loop does not execute if that loop is terminated by `break`.

---

## 3. BREAK Statement

The `break` statement is used to stop a loop immediately when a specified condition is satisfied.

It is useful when the required result has been found and there is no need to continue looping.

### Example 1: Stop at a Specific Number

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

### Output

```text
1
2
3
4
```

### Explanation

When `i` becomes 5, the `break` statement terminates the loop. Therefore, 5 and the remaining numbers are not printed.

### Example 2: Searching for an Item

```python
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    if fruit == "mango":
        print("Mango found.")
        break
    print(fruit)
```

### Output

```text
apple
banana
Mango found.
```

### Explanation

The loop stops as soon as it finds `"mango"`. The remaining items are not processed.

---

## 4. CONTINUE Statement

The `continue` statement skips the remaining statements in the current loop iteration and moves to the next iteration.

Unlike `break`, it does not terminate the entire loop.

### Example 1: Skip a Number

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Output

```text
1
2
4
5
```

### Explanation

When the value of `i` becomes 3, the `continue` statement skips the `print()` statement for that iteration. The loop then continues with 4 and 5.

### Example 2: Print Only Odd Numbers

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

### Output

```text
1
3
5
7
9
```

### Explanation

The condition checks whether each number is even. If the remainder after division by 2 is zero, `continue` skips that number. Only odd numbers are printed.

---

## 5. PASS Statement

The `pass` statement is a placeholder that does nothing when executed. It allows you to create an empty block where Python syntax requires a statement.

It is useful when planning a program and intending to add the actual logic later.

### Example 1: PASS in a FOR Loop

```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```

### Output

```text
1
2
3
4
5
```

### Explanation

The `pass` statement does not skip the number 3 or stop the loop. It simply does nothing, so the `print()` statement executes normally.

### Example 2: PASS in a Function

```python
def calculate_total():
    pass

print("Program started.")
```

### Output

```text
Program started.
```

### Explanation

The function is defined with `pass` as a placeholder. It does not perform any calculation yet, but the program can continue running.

**Important:** `pass` is different from `break` and `continue`. It does not terminate the loop or skip an iteration.

---

## 6. ASSERT Keyword

The `assert` statement is used to check whether a condition is true. If the condition is false, Python raises an `AssertionError`.

It is commonly used during development to identify unexpected values and verify assumptions about a program.

### Syntax

```python
assert condition, "Optional error message"
```

### Example 1: Checking a Condition

```python
age = 21

assert age >= 18, "Age must be at least 18"

print("Age requirement satisfied.")
```

### Output

```text
Age requirement satisfied.
```

### Explanation

The condition `age >= 18` is true, so the program continues without raising an error.

### Example 2: Assertion Error

```python
balance = -100

assert balance >= 0, "Balance cannot be negative"

print("Valid balance.")
```

### Output

```text
AssertionError: Balance cannot be negative
```

### Explanation

The balance is negative, so the assertion condition is false. Python raises an `AssertionError`, and the next `print()` statement is not executed.

**Important:** Assertions are useful for debugging and checking internal assumptions. Do not use them as the only validation for user input or security checks, because Python can disable assertions when run with optimization enabled.

---

## Difference Between BREAK, CONTINUE, and PASS

| Statement | Purpose | Effect |
|---|---|---|
| `break` | Stop the loop | Exits the nearest enclosing loop |
| `continue` | Skip the current iteration | Moves to the next iteration |
| `pass` | Do nothing | Execution continues normally |

## Important Points to Remember

- A `for` loop iterates over items in a sequence or other iterable.
- `range(start, stop)` includes the start value but excludes the stop value.
- A loop's `else` block executes when the loop finishes normally without `break`.
- `break` immediately terminates the nearest enclosing loop.
- `continue` skips the remaining statements in the current iteration.
- `pass` is a placeholder that performs no operation.
- `assert` checks a condition and raises `AssertionError` if the condition is false.
- Correct indentation is essential in Python.

## Day 10 Summary

Python provides loops and control statements to manage repetition and control the flow of a program. The `for` loop processes sequences, `for-else` handles normal loop completion, `break` stops a loop, `continue` skips an iteration, `pass` acts as a placeholder, and `assert` checks assumptions during development. Understanding these concepts helps you write clearer and more efficient Python programs.
