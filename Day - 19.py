# Day 19: Python Real-Time Examples and Mini Projects

## 1. Introduction to Real-Time Examples

Real-time examples help us understand how Python concepts are used in everyday applications. Instead of learning only individual functions, we can combine variables, conditions, loops, functions, and modules to build small projects.

In this lesson, we will create:

1. A real-time shopping bill calculator.
2. A random password generator.
3. An ATM simulation.

These projects help us practice Python programming in a practical way.

---

## 2. Real-Time Example: Shopping Bill Calculator

A shopping bill calculator adds item prices, calculates the total, applies a discount when applicable, and displays the final amount.

### Concepts used

- Variables and data types
- Lists and loops
- Conditional statements
- Arithmetic operators
- Functions

### Program

```python
def calculate_bill(prices):
    total = sum(prices)

    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print("Total amount:", total)
    print("Discount:", discount)
    print("Final amount:", final_amount)


prices = [250, 300, 500]

calculate_bill(prices)
```

### Output

```text
Total amount: 1050
Discount: 105.0
Final amount: 945.0
```

### Explanation

- The `prices` list stores the prices of purchased items.
- `sum()` calculates the total bill.
- If the total is at least ₹1,000, a 10% discount is applied.
- The final amount is calculated by subtracting the discount from the total.

This is a simple example of how Python can be used in billing systems.

---

## 3. Mini Project: Random Password Generator

A password generator creates a random password using letters, numbers, and special characters.

It is useful for learning how Python's `random` module works and how to combine strings, loops, and functions.

### Concepts used

- `random` module
- `string` module
- Functions
- Loops
- User input
- Exception handling

### Program

```python
import secrets
import string


def generate_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8.")

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    password.extend(
        secrets.choice(characters)
        for _ in range(length - len(password))
    )

    # Randomize the positions of the characters.
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


try:
    length = int(input("Enter password length (minimum 8): "))

    password = generate_password(length)

    print("Generated password:", password)

except ValueError as error:
    print("Error:", error)
```

### Sample output

```text
Enter password length (minimum 8): 12
Generated password: aB7@kP2!mQ9#
```

The generated password will be different each time.

### Explanation

**1. Import modules**

- `secrets` provides secure random choices suitable for password generation.
- `string` provides ready-made collections of letters, digits, and punctuation.

**2. Check the length**

The program requires a password of at least eight characters.

**3. Select characters**

The password includes at least one lowercase letter, uppercase letter, digit, and punctuation character.

**4. Shuffle the characters**

The characters are placed in a random order.

**5. Join the characters**

`"".join(password)` combines the individual characters into one string.

### Important note

For real accounts, prefer a password manager and use long, unique passwords. Eight characters is only the minimum used in this learning example; longer passwords are generally preferable.

---

## 4. Mini Project: ATM Simulation

An ATM simulation demonstrates how a simple banking menu might work. The user can check a balance, deposit money, withdraw money, or exit the program.

This is a learning simulation only. It does not connect to a real bank or perform real transactions.

### Concepts used

- Variables
- Functions
- `while` loops
- Conditional statements
- User input
- Exception handling

### Program

```python
def check_balance(balance):
    print(f"Available balance: ₹{balance:.2f}")


def deposit_money(balance):
    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            balance += amount
            print(f"₹{amount:.2f} deposited successfully.")

    except ValueError:
        print("Please enter a valid number.")

    return balance


def withdraw_money(balance):
    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    except ValueError:
        print("Please enter a valid number.")

    return balance


def atm():
    balance = 5000.00

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit_money(balance)

        elif choice == "3":
            balance = withdraw_money(balance)

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please select 1-4.")


atm()
```

### Sample output

```text
===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 1
Available balance: ₹5000.00

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 2
Enter deposit amount: ₹1000
₹1000.00 deposited successfully.

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 3
Enter withdrawal amount: ₹500
₹500.00 withdrawn successfully.

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 1
Available balance: ₹5500.00

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 4
Thank you for using the ATM.
```

### Explanation

**1. Initial balance**

The program starts with a sample balance of ₹5,000.

**2. Check balance**

The `check_balance()` function displays the current balance.

**3. Deposit money**

The `deposit_money()` function checks that the amount is positive and adds it to the balance.

**4. Withdraw money**

The `withdraw_money()` function checks that the amount is positive and that sufficient funds are available before subtracting it.

**5. Repeat the menu**

The `while True` loop keeps displaying the menu until the user chooses option 4.

**6. Handle invalid input**

The `try-except` blocks prevent invalid numeric input from crashing the program.

**Important:** This beginner example stores the balance only in memory. The balance resets to ₹5,000 when the program restarts. Real banking applications require secure authentication, persistent records, transaction validation, and proper security controls.

---

## 5. Quick Revision

| Project | Main Python concepts |
|---|---|
| Shopping Bill Calculator | Lists, functions, loops, conditions |
| Random Password Generator | Modules, strings, functions, secure randomness |
| ATM Simulation | Functions, loops, conditions, input validation |

## 6. What I Learned Today

- How to combine Python concepts to solve practical problems.
- How to calculate a shopping bill and apply a discount.
- How to generate random passwords using Python's `secrets` module.
- How to create a menu-driven ATM simulation.
- How to use functions to organize code.
- How to handle invalid input using `try-except`.
- How loops and conditions control program behavior.

**Day 19 completed: Python Real-Time Examples and Mini Projects.**
