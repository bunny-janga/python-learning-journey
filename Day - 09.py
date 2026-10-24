# Day 9: Problem Solving and Logical Thinking in Python

## 1. Problem Solving

Problem solving is the process of understanding a problem, finding a solution, and implementing that solution using programming.

In Python, problem solving helps us break complex tasks into smaller steps and write code that produces the expected result.

### Steps in Problem Solving

1. **Understand the problem:** Identify what needs to be solved.
2. **Identify the inputs:** Determine what information is required.
3. **Plan the logic:** Decide the steps needed to solve the problem.
4. **Write the code:** Convert the logic into Python statements.
5. **Test the solution:** Run the program with different inputs.
6. **Debug the code:** Find and correct errors if the output is incorrect.

### Example 1: Adding Two Numbers

**Problem:** Write a program to add two numbers.

**Logic:**
- Store two numbers.
- Add them together.
- Display the result.

```python
num1 = 10
num2 = 20

result = num1 + num2

print("Sum:", result)
```

**Output**

```text
Sum: 30
```

**Explanation:** The program stores two numbers, adds them using the `+` operator, and displays their sum.

### Example 2: Finding the Square of a Number

**Problem:** Calculate the square of a number.

```python
number = 5

square = number * number

print("Square:", square)
```

**Output**

```text
Square: 25
```

**Explanation:** Multiplying a number by itself gives its square. Here, \(5 \times 5 = 25\).

### Example 3: Checking Even or Odd

**Problem:** Determine whether a number is even or odd.

**Logic:** If a number is divisible by 2 without a remainder, it is even. Otherwise, it is odd.

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

**Output**

```text
Odd number
```

**Explanation:** The modulo operator (`%`) returns the remainder after division. Since 7 divided by 2 leaves a remainder of 1, the number is odd.

### Example 4: Finding the Greater Number

**Problem:** Find the greater of two numbers.

```python
a = 25
b = 40

if a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Both numbers are equal")
```

**Output**

```text
B is greater
```

**Explanation:** The program compares both numbers and displays the appropriate result. It also handles the case in which both numbers are equal.

### Example 5: Calculating Simple Interest

**Problem:** Calculate simple interest using the principal amount, annual interest rate, and time.

**Formula:**

Simple Interest = (Principal × Rate × Time) / 100

```python
principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
```

**Output**

```text
Simple Interest: 1000.0
```

**Explanation:** The program applies the simple-interest formula. For a principal of 10,000 at 5% per year for 2 years, the interest is 1,000.

---

## 2. Logical Thinking Exercises

Logical thinking means using reasoning and step-by-step decisions to solve problems. It helps programmers understand how a program should behave before writing the code.

Logical thinking is important because programming is not only about knowing syntax; it is also about developing the correct solution.

### Example 1: Check Positive, Negative, or Zero

**Problem:** Identify whether a number is positive, negative, or zero.

```python
number = -10

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

**Output**

```text
Negative number
```

**Logic:** A number greater than zero is positive, a number less than zero is negative, and a number equal to zero is neither positive nor negative.

### Example 2: Find the Largest of Three Numbers

**Problem:** Find the largest number among three values.

```python
a = 15
b = 30
c = 20

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)
```

**Output**

```text
Largest number: 30
```

**Explanation:** The program compares each number with the other two. The `and` operator ensures that both comparisons must be true for a number to be the largest.

### Example 3: Check Leap Year

**Problem:** Determine whether a year is a leap year.

**Logic:**
- A year divisible by 400 is a leap year.
- Otherwise, a year divisible by 100 is not a leap year.
- Otherwise, a year divisible by 4 is a leap year.
- All other years are not leap years.

```python
year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
```

**Output**

```text
Leap year
```

**Explanation:** The year 2024 is divisible by 4 and is not a century year, so it is a leap year.

### Example 4: Calculate the Sum of Digits

**Problem:** Find the sum of the digits in a number.

```python
number = 1234
total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum of digits:", total)
```

**Output**

```text
Sum of digits: 10
```

**Explanation:** The modulo operator extracts the last digit, and integer division (`//`) removes that digit. The process continues until no digits remain.

Calculation: 1 + 2 + 3 + 4 = 10.

### Example 5: Reverse a Number

**Problem:** Reverse the digits of a number.

```python
number = 1234
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number:", reverse)
```

**Output**

```text
Reversed number: 4321
```

**Explanation:** The program extracts each last digit and adds it to the reversed number. Repeating this process builds the number in reverse order.

### Example 6: Check Whether a Number Is a Palindrome

**Problem:** Determine whether a number reads the same forward and backward.

```python
number = 121
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
```

**Output**

```text
Palindrome number
```

**Explanation:** The program reverses the number and compares it with the original. Since both values are 121, the number is a palindrome.

### Example 7: Calculate a Factorial

**Problem:** Find the factorial of a non-negative integer.

The factorial of a number is the product of all positive integers up to that number. The factorial of zero is 1.

```python
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)
```

**Output**

```text
Factorial: 120
```

**Explanation:** The loop multiplies the values from 1 through 5.

Calculation: 5 × 4 × 3 × 2 × 1 = 120.

---

## Important Concepts to Remember

- Problem solving begins with understanding the problem and identifying the required output.
- Logical thinking helps develop a clear sequence of steps before writing code.
- The modulo operator (`%`) is useful for checking divisibility and extracting digits.
- Integer division (`//`) removes the last digit when working with positive integers.
- Conditional statements help make decisions.
- Loops repeat a set of instructions until the required condition is met or the sequence ends.
- Testing a program with different values helps identify logical errors.
- Clear variable names and simple logic make programs easier to understand and maintain.

## Day 9 Summary

Problem solving and logical thinking are essential skills for every Python programmer. By learning to break problems into smaller steps, use conditions and loops, and test solutions carefully, we can build a strong foundation for more advanced programming topics.
