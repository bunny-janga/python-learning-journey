# Day 8: Python Conditional Statements

## 1. IF Statement

The `if` statement is used to execute a block of code only when a given condition is true. It helps a program make decisions based on specific conditions.

### Syntax

```python
if condition:
    # Code executes when the condition is True
```

### Example

```python
age = 21

if age >= 18:
    print("You are eligible to vote.")
```

### Output

```text
You are eligible to vote.
```

### Explanation

The condition checks whether the age is greater than or equal to 18. Since the age is 21, the condition is true, and the message is displayed.

---

## 2. IF-ELSE Statement

The `if-else` statement is used when a program needs to choose between two outcomes. If the condition is true, the `if` block executes. Otherwise, the `else` block executes.

### Syntax

```python
if condition:
    # Executes when the condition is True
else:
    # Executes when the condition is False
```

### Example

```python
marks = 28

if marks >= 35:
    print("You passed the exam.")
else:
    print("You failed the exam.")
```

### Output

```text
You failed the exam.
```

### Explanation

The student's marks are 28, which is less than 35. Therefore, the condition is false, and Python executes the `else` block.

---

## 3. ELIF Statement

The `elif` statement means "else if." It is used to check multiple conditions in a program. Python checks the conditions from top to bottom and executes the first matching block.

### Syntax

```python
if condition1:
    # First condition
elif condition2:
    # Second condition
elif condition3:
    # Third condition
else:
    # Executes when no condition is True
```

### Example: Student Grade Calculator

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
```

### Output

```text
Grade B
```

### Explanation

The first condition is false because the marks are below 90. The second condition is true because the marks are at least 75. Therefore, Python displays `Grade B`.

---

## 4. Nested Conditions

A nested condition means writing one `if` statement inside another `if` statement. It is useful when a decision depends on another condition being satisfied first.

### Example: Login System

```python
username = "student"
password = "python123"

if username == "student":
    if password == "python123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")
```

### Output

```text
Login successful!
```

### Explanation

First, Python checks whether the username is correct. If it is correct, Python checks the password. If both match, the login is successful. Otherwise, an appropriate error message is displayed.

Nested conditions are commonly used in login systems, eligibility checks, and other applications that require multiple decisions.

---

## 5. Real-Time Examples

### Example 1: ATM Withdrawal

```python
balance = 5000
withdrawal = 2000

if withdrawal > 0:
    if withdrawal <= balance:
        balance = balance - withdrawal
        print("Withdrawal successful.")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance.")
else:
    print("Enter a valid amount.")
```

### Output

```text
Withdrawal successful.
Remaining balance: 3000
```

### Explanation

The program checks whether the withdrawal amount is valid and whether sufficient balance is available. If both conditions are satisfied, the balance is updated.

### Example 2: Voting Eligibility

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### Output

```text
You are eligible to vote.
```

### Explanation

The program checks the person's age. If the age is 18 or above, the person meets the age requirement for voting in this example.

### Example 3: Electricity Bill Discount

```python
bill_amount = 2500

if bill_amount >= 5000:
    discount = 500
elif bill_amount >= 2000:
    discount = 200
else:
    discount = 0

final_amount = bill_amount - discount

print("Discount:", discount)
print("Final bill:", final_amount)
```

### Output

```text
Discount: 200
Final bill: 2300
```

### Explanation

The program checks the bill amount and applies a discount based on the conditions. Since the bill is 2500, the discount is 200.

### Example 4: Number Checker

```python
number = -5

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
```

### Output

```text
Negative number
```

### Explanation

The program checks whether the number is positive, negative, or zero and displays the appropriate message.

### Example 5: Online Shopping Delivery

```python
order_amount = 1200
membership = "premium"

if order_amount >= 1000:
    if membership == "premium":
        print("Free express delivery.")
    else:
        print("Free standard delivery.")
else:
    print("Delivery charges apply.")
```

### Output

```text
Free express delivery.
```

### Explanation

The program checks the order amount first. If the amount is at least 1000, it checks the membership type to determine the delivery option.

---

## Important Points to Remember

- The `if` statement executes code when a condition is true.
- The `else` statement handles the alternative when the condition is false.
- The `elif` statement checks additional conditions.
- Nested conditions allow one decision to be placed inside another.
- Always use a colon (`:`) after `if`, `elif`, and `else`.
- Correct indentation is important in Python.
- Comparison operators such as `==`, `!=`, `>`, `<`, `>=`, and `<=` are commonly used in conditions.
- In an `if-elif-else` structure, only the first matching block executes.

## Day 8 Summary

Conditional statements help Python programs make decisions and respond differently depending on the data they receive. The `if`, `if-else`, `elif`, and nested `if` statements are fundamental concepts used in real-world applications such as login systems, banking software, shopping websites, and student grading systems.
