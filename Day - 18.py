# Day 18: Python Standard Library Modules

## 1. Introduction to Modules

A module is a file that contains Python code, such as functions, variables, and classes. Modules help us organize code and reuse existing functionality instead of writing everything from scratch.

Python provides many built-in modules that we can import whenever we need them.

### Why do we use modules?

- To reuse existing code.
- To make programs easier to organize.
- To reduce repeated code.
- To access useful built-in functions.

### Example

```python
import math

print(math.sqrt(25))
print(math.pi)
```

**Output:**
```text
5.0
3.141592653589793
```

We use `import` to access a module. The dot operator (`.`) lets us access its functions and variables.

---

## 2. Math Module

The `math` module provides mathematical functions and constants. It is useful for calculations involving square roots, powers, rounding, and trigonometry.

### Importing the math module

```python
import math
```

### Important functions

| Function | Purpose |
|---|---|
| `math.sqrt(x)` | Returns the square root |
| `math.ceil(x)` | Rounds upward to an integer |
| `math.floor(x)` | Rounds downward to an integer |
| `math.factorial(x)` | Returns the factorial of a non-negative integer |
| `math.pow(x, y)` | Returns x raised to the power y as a float |
| `math.fabs(x)` | Returns the absolute value as a float |
| `math.pi` | Provides the value of pi |
| `math.gcd(a, b)` | Returns the greatest common divisor |

### Example

```python
import math

print(math.sqrt(64))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.factorial(5))
print(math.pow(2, 3))
print(math.fabs(-15))
print(math.gcd(12, 18))
print(math.pi)
```

**Output:**
```text
8.0
5
4
120
8.0
15.0
6
3.141592653589793
```

### Using a specific function

We can import only the function we need.

```python
from math import sqrt

print(sqrt(81))
```

**Output:**
```text
9.0
```

**Remember:** Most `math` functions work with numbers. For factorials, use non-negative integers.

---

## 3. Random Module

The `random` module helps us generate pseudo-random numbers and select random items. It is useful for simple games, simulations, and practice programs.

### Importing the random module

```python
import random
```

### Important functions

| Function | Purpose |
|---|---|
| `random.random()` | Returns a float from 0.0 up to, but not including, 1.0 |
| `random.randint(a, b)` | Returns an integer between a and b, including both |
| `random.randrange(a, b)` | Selects an integer from the range, excluding b |
| `random.choice(items)` | Selects one item from a non-empty sequence |
| `random.shuffle(items)` | Shuffles a list in place |
| `random.uniform(a, b)` | Returns a random float between the given bounds |

### Example

```python
import random

print(random.randint(1, 10))
print(random.choice(["Apple", "Mango", "Orange"]))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
```

**Sample output:**
```text
7
Mango
[3, 1, 5, 2, 4]
```

Your output may be different each time because the results are random.

### Example: Dice simulator

```python
import random

dice = random.randint(1, 6)
print("Dice value:", dice)
```

**Sample output:**
```text
Dice value: 4
```

**Important:** The `random` module is not suitable for passwords, security tokens, or other security-sensitive purposes. Use Python's `secrets` module for those tasks.

---

## 4. Sys Module

The `sys` module provides information about the Python interpreter and allows us to interact with certain interpreter features.

### Importing the sys module

```python
import sys
```

### Important attributes and functions

| Attribute / Function | Purpose |
|---|---|
| `sys.version` | Shows the Python version |
| `sys.platform` | Identifies the operating-system platform |
| `sys.argv` | Contains command-line arguments |
| `sys.path` | Shows locations Python searches for modules |
| `sys.exit()` | Requests termination of the program |
| `sys.getsizeof()` | Returns the approximate size of an object in bytes |

### Example

```python
import sys

print(sys.version)
print(sys.platform)
print(sys.getsizeof(100))
```

**Sample output:**
```text
3.x.x (...)
win32
28
```

The exact version and object size can vary. On a typical 64-bit CPython installation, `sys.getsizeof(100)` is often 28 bytes.

### Example: Command-line arguments

Save this code in a file named `arguments.py`.

```python
import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])
```

Run it from the terminal:

```bash
python arguments.py Hello Python
```

**Output:**
```text
Script name: arguments.py
Arguments: ['Hello', 'Python']
```

Command-line arguments are useful when we want to pass values to a program without asking for interactive input.

---

## 5. Platform Module

The `platform` module provides information about the operating system, computer architecture, and Python environment.

It is different from `sys`: the `platform` module focuses on describing the system, while `sys` provides interpreter-related information and functionality.

### Importing the platform module

```python
import platform
```

### Important functions

| Function | Purpose |
|---|---|
| `platform.system()` | Returns the operating-system name |
| `platform.release()` | Returns the operating-system release |
| `platform.version()` | Returns operating-system version details |
| `platform.machine()` | Returns machine architecture information |
| `platform.processor()` | Returns processor information when available |
| `platform.python_version()` | Returns the Python version |

### Example

```python
import platform

print("Operating system:", platform.system())
print("OS release:", platform.release())
print("Machine:", platform.machine())
print("Python version:", platform.python_version())
```

**Sample output on Windows:**
```text
Operating system: Windows
OS release: 11
Machine: AMD64
Python version: 3.x.x
```

The actual output depends on your computer and installed Python version.

### Practical use

We can use the `platform` module when a program needs to display system information or adjust its behavior for different operating systems.

---

## 6. Collections Module

The `collections` module provides specialized container data types that make certain programming tasks easier.

### Important classes

| Class | Purpose |
|---|---|
| `Counter` | Counts how many times items occur |
| `defaultdict` | Provides a default value for missing keys |
| `deque` | Supports efficient additions and removals at both ends |
| `namedtuple` | Creates tuple-like objects with named fields |
| `OrderedDict` | Dictionary with additional order-related methods; regular dictionaries also preserve insertion order in modern Python |

### 6.1 Counter

`Counter` counts the occurrences of elements in an iterable.

```python
from collections import Counter

fruits = ["apple", "mango", "apple", "orange", "mango", "apple"]

result = Counter(fruits)
print(result)
print(result["apple"])
```

**Output:**
```text
Counter({'apple': 3, 'mango': 2, 'orange': 1})
3
```

### 6.2 defaultdict

`defaultdict` automatically provides a default value when we access a missing key.

```python
from collections import defaultdict

marks = defaultdict(int)

marks["Python"] += 10
marks["MySQL"] += 20

print(dict(marks))
print(marks["Java"])
```

**Output:**
```text
{'Python': 10, 'MySQL': 20}
0
```

Here, `int` provides the default value `0`.

### 6.3 deque

A `deque` allows efficient additions and removals at both ends.

```python
from collections import deque

numbers = deque([10, 20, 30])

numbers.append(40)
numbers.appendleft(5)

print(numbers)

numbers.pop()
numbers.popleft()

print(numbers)
```

**Output:**
```text
deque([5, 10, 20, 30, 40])
deque([10, 20, 30])
```

### 6.4 namedtuple

`namedtuple` lets us access tuple values using meaningful field names.

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])

student1 = Student("Rahul", 21)

print(student1.name)
print(student1.age)
```

**Output:**
```text
Rahul
21
```

**Remember:** Use `Counter` for counting, `defaultdict` for convenient default values, `deque` for operations at both ends, and `namedtuple` for simple records with named fields.

---

## 7. Itertools Module

The `itertools` module provides tools for working efficiently with iterators. It is especially useful for looping, combining sequences, and generating combinations or permutations.

### Importing the itertools module

```python
import itertools
```

### Important functions

| Function | Purpose |
|---|---|
| `itertools.count()` | Generates numbers continuously |
| `itertools.cycle()` | Repeats items from an iterable |
| `itertools.repeat()` | Repeats a value |
| `itertools.chain()` | Joins iterables into one sequence of items |
| `itertools.combinations()` | Generates combinations without considering order |
| `itertools.permutations()` | Generates arrangements where order matters |
| `itertools.product()` | Generates a Cartesian product |

### 7.1 count()

`count()` generates numbers continuously. Use a limit when displaying its values.

```python
import itertools

for number in itertools.islice(itertools.count(1), 5):
    print(number)
```

**Output:**
```text
1
2
3
4
5
```

### 7.2 repeat()

```python
import itertools

for item in itertools.repeat("Python", 3):
    print(item)
```

**Output:**
```text
Python
Python
Python
```

### 7.3 chain()

```python
import itertools

a = [1, 2, 3]
b = [4, 5, 6]

result = itertools.chain(a, b)
print(list(result))
```

**Output:**
```text
[1, 2, 3, 4, 5, 6]
```

### 7.4 combinations()

Combinations select items where order does not matter.

```python
import itertools

items = ["A", "B", "C"]

result = itertools.combinations(items, 2)
print(list(result))
```

**Output:**
```text
[('A', 'B'), ('A', 'C'), ('B', 'C')]
```

### 7.5 permutations()

Permutations generate arrangements where order matters.

```python
import itertools

items = ["A", "B", "C"]

result = itertools.permutations(items, 2)
print(list(result))
```

**Output:**
```text
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

### 7.6 product()

```python
import itertools

numbers = [1, 2]
letters = ["A", "B"]

result = itertools.product(numbers, letters)
print(list(result))
```

**Output:**
```text
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

**Important:** Many `itertools` functions return iterators rather than lists. Use `list()` when you want to display or store all results, but remember that large results can consume a lot of memory.

---

## 8. Datetime Module

The `datetime` module is used to work with dates, times, and differences between dates.

It is useful for attendance systems, expense trackers, reports, reminders, and applications that record when something happened.

### Importing the datetime module

```python
import datetime
```

### Important classes

| Class | Purpose |
|---|---|
| `date` | Represents a calendar date |
| `time` | Represents a time of day |
| `datetime` | Represents both date and time |
| `timedelta` | Represents a duration or difference between dates and times |

### 8.1 Get the current date

```python
from datetime import date

today = date.today()
print(today)
```

**Sample output:**
```text
2026-10-28
```

The output changes according to the current date.

### 8.2 Get the current date and time

```python
from datetime import datetime

now = datetime.now()
print(now)
```

**Sample output:**
```text
2026-10-28 21:57:30.123456
```

The time shown here is only an example; your output will depend on when you run the program.

### 8.3 Create a specific date

```python
from datetime import date

birthday = date(2005, 5, 15)

print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.day)
```

**Output:**
```text
2005-05-15
2005
5
15
```

### 8.4 Format a date using strftime()

`strftime()` converts a date or time into a formatted string.

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%A"))
```

**Sample output:**
```text
28-10-2026
21:57:30
Wednesday
```

Useful format codes:

| Code | Meaning |
|---|---|
| `%d` | Day of the month |
| `%m` | Month number |
| `%Y` | Four-digit year |
| `%H` | Hour in 24-hour format |
| `%M` | Minutes |
| `%S` | Seconds |
| `%A` | Full weekday name |
| `%B` | Full month name |

### 8.5 Convert a string into a date using strptime()

`strptime()` parses a string into a date/time object using the specified format.

```python
from datetime import datetime

date_text = "28-10-2026"

result = datetime.strptime(date_text, "%d-%m-%Y")

print(result)
print(result.year)
```

**Output:**
```text
2026-10-28 00:00:00
2026
```

### 8.6 Calculate the difference between dates

```python
from datetime import date

date1 = date(2026, 10, 28)
date2 = date(2026, 11, 10)

difference = date2 - date1

print(difference.days)
```

**Output:**
```text
13
```

### 8.7 Use timedelta to add days

```python
from datetime import date, timedelta

today = date.today()
future_date = today + timedelta(days=7)

print("Today:", today)
print("After 7 days:", future_date)
```

**Sample output:**
```text
Today: 2026-10-28
After 7 days: 2026-11-04
```

---

## 9. Quick Revision

| Module | Main use |
|---|---|
| `math` | Mathematical calculations |
| `random` | Random numbers and selections |
| `sys` | Python interpreter and command-line information |
| `platform` | Operating-system and machine information |
| `collections` | Specialized data containers |
| `itertools` | Efficient iterator operations |
| `datetime` | Dates, times, and durations |

## 10. Final Notes

- A module is a reusable Python file or collection of functionality.
- Use `import module_name` to import a module.
- Use `from module_name import function_name` to import a specific function.
- Use `as` to give an imported module or function an alias.
- Python's standard library contains many useful modules that do not require separate installation.
- Choose the module that matches the task instead of writing everything from scratch.

**Day 18 completed: Python Standard Library Modules.**
