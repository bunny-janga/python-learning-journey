# Day 14: Python Scope, Argument Passing, and Recursion

## 1. Local Scope

### What is Local Scope?

A local variable is a variable created inside a function. It can normally be accessed only within that function.

When the function finishes executing, its local variables are no longer available for use outside the function.

### Example

```python
def greet():
    message = "Hello, Python!"
    print(message)

greet()
```

**Output:**
```text
Hello, Python!
```

In this example, `message` is a local variable because it is created inside the `greet()` function.

### Example: Local Variable Cannot Be Accessed Outside

```python
def display():
    number = 100
    print(number)

display()

# print(number)  # NameError
```

**Output:**
```text
100
```

The last line is commented out because `number` is a local variable and cannot be accessed directly outside the function.

---

## 2. Global Scope

### What is Global Scope?

A global variable is a variable declared outside all functions. It can be accessed from different parts of the program, including inside functions.

### Example

```python
name = "Python"

def display():
    print(name)

display()
print(name)
```

**Output:**
```text
Python
Python
```

Here, `name` is a global variable because it is declared outside the function.

### Using the `global` Keyword

The `global` keyword allows a function to modify a global variable.

```python
count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)
```

**Output:**
```text
20
```

Without the `global` keyword, assigning to `count` inside the function would create a local variable instead.

**Note:** Use global variables carefully. Passing values through function parameters and returning results is often easier to maintain.

---

## 3. Pass by Value

### What Does Pass by Value Mean?

Pass by value generally means that a function receives a copy of a value. Changes made to that copy do not change the original variable.

Python does not use traditional pass-by-value in the strict sense. It passes object references to functions. However, the following example demonstrates the behavior beginners often associate with pass by value.

### Example

```python
def change_number(number):
    number = 100
    print("Inside function:", number)

value = 50

change_number(value)

print("Outside function:", value)
```

**Output:**
```text
Inside function: 100
Outside function: 50
```

The original variable `value` remains `50`. The parameter `number` is reassigned to a different integer object inside the function.

---

## 4. Pass by Reference

### What Does Pass by Reference Mean?

In traditional pass-by-reference, a function can directly modify the caller's variable through a reference to it.

Python does not use traditional pass-by-reference. Instead, it passes object references. When a mutable object, such as a list, is passed to a function, the function can modify that same object.

### Example Using a List

```python
def add_item(items):
    items.append("Mango")

fruits = ["Apple", "Banana"]

add_item(fruits)

print(fruits)
```

**Output:**
```text
['Apple', 'Banana', 'Mango']
```

The original list changes because `items` and `fruits` refer to the same list object.

### Example: Reassigning the Parameter

```python
def change_list(items):
    items = ["Orange", "Grapes"]

fruits = ["Apple", "Banana"]

change_list(fruits)

print(fruits)
```

**Output:**
```text
['Apple', 'Banana']
```

Here, the original list remains unchanged because the function reassigns its local parameter to a new list.

**Remember:** Python's argument-passing behavior is best described as *object-reference passing* (often called *call by sharing*). Whether the original object changes depends on whether the function mutates the object or simply reassigns its parameter.

---

## 5. Recursive Functions

### What is Recursion?

Recursion is a programming technique in which a function calls itself to solve a smaller version of the same problem.

A recursive function needs two important parts:

1. **Base case:** Stops the recursion.
2. **Recursive case:** Calls the function again with a smaller or simpler problem.

Without a proper base case, recursion may continue until Python raises a `RecursionError`.

### Example: Countdown

```python
def countdown(number):
    if number == 0:
        print("Finished!")
        return

    print(number)
    countdown(number - 1)

countdown(5)
```

**Output:**
```text
5
4
3
2
1
Finished!
```

The function prints a number and calls itself with a number one smaller. When the number reaches zero, the base case stops the recursion.

### Example: Factorial Using Recursion

The factorial of a positive integer is the product of all positive integers up to that number.

For example:

`5! = 5 × 4 × 3 × 2 × 1 = 120`

```python
def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))
```

**Output:**
```text
120
```

### How It Works

```text
factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 = 120
```

The base case is reached at `factorial(1)`, which returns `1`. The results are then multiplied as the recursive calls return.

**Note:** This example assumes a non-negative integer input. For larger problems, an iterative solution may be more efficient because recursive calls use additional stack space.

---

## Day 14 Summary

| Concept | Meaning |
|---|---|
| Local Scope | A variable defined inside a function |
| Global Scope | A variable defined outside functions |
| Pass by Value | A general term for passing a copy of a value |
| Pass by Reference | A general term for allowing a function to modify a caller's variable through a reference |
| Python Argument Passing | Object references are passed to functions |
| Recursion | A function calls itself to solve a smaller problem |
| Base Case | The condition that stops recursion |

### Key Takeaways

- Local variables are normally accessible only inside their function.
- Global variables are declared outside functions.
- Python passes object references to functions.
- Mutating a list inside a function can change the original list.
- Reassigning a function parameter does not, by itself, replace the caller's variable.
- Recursive functions need a base case to stop.
- Factorial and countdown are common beginner examples of recursion.
