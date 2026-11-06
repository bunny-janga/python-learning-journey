# Day 27 – Python Data Abstraction

## 1. What is Data Abstraction?

**Data Abstraction** is one of the important concepts of Object-Oriented Programming (OOP).

Abstraction means hiding the internal implementation details and showing only the essential features to the user.

In simple words, we focus on **what an object does rather than how it works internally**.

### Real-Time Example

Think about using an ATM machine.

When you use an ATM, you can:
- Check your account balance.
- Withdraw money.
- Deposit money.
- Change your PIN.

You do not need to know how the ATM communicates with the bank server or processes the transaction internally.

This is an example of abstraction.

### Why do we use Data Abstraction?

- Hides unnecessary implementation details.
- Makes programs easier to understand.
- Reduces complexity.
- Improves code organization.
- Provides a clear structure for large applications.

---

## 2. How to Achieve Abstraction in Python?

Python supports abstraction using the `abc` module.

`abc` stands for **Abstract Base Classes**.

We mainly use:

- `ABC` – Used as a base class for creating abstract classes.
- `abstractmethod` – Used to declare abstract methods.

### Syntax

```python
from abc import ABC, abstractmethod

class ClassName(ABC):

    @abstractmethod
    def method_name(self):
        pass
```

### Important Terms

**Abstract Class:**

An abstract class is a class that contains one or more abstract methods. It cannot be instantiated directly.

**Abstract Method:**

An abstract method is a method declared using the `@abstractmethod` decorator. Its implementation is provided by concrete child classes.

---

## 3. Simple Example of Data Abstraction

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog1 = Dog()

dog1.sound()
```

**Output:**

```text
Dog barks
```

### Explanation

- `ABC` is imported from the `abc` module.
- `Animal` is an abstract class.
- `sound()` is an abstract method.
- `Dog` inherits from `Animal`.
- `Dog` provides the implementation of `sound()`.
- We create an object of `Dog` and call its method.

**Note:** We cannot directly create an object of `Animal` because it contains an abstract method that has not been implemented.

---

## 4. Example: Abstract Class with Multiple Methods

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


car1 = Car()

car1.start()
car1.stop()
```

**Output:**

```text
Car started
Car stopped
```

### Explanation

- `Vehicle` is an abstract class.
- It contains two abstract methods: `start()` and `stop()`.
- `Car` inherits from `Vehicle`.
- The `Car` class implements both methods.
- Now we can create a `Car` object.

**Remember:** A concrete child class must implement all inherited abstract methods before it can be instantiated.

---

## 5. Example: Real-Time Banking Application

```python
from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
            print("Remaining Balance:", self.balance)

        else:
            print("Insufficient balance")


account = SavingsAccount(10000)

account.withdraw(2000)
```

**Output:**

```text
Withdrawal successful
Remaining Balance: 8000
```

### Explanation

- `BankAccount` is an abstract class.
- `withdraw()` is an abstract method.
- `SavingsAccount` provides the actual withdrawal implementation.
- The user can call the withdrawal operation without needing to know the internal implementation.

---

## 6. Difference Between Abstract Class and Concrete Class

| Abstract Class | Concrete Class |
|---|---|
| Cannot be instantiated directly | Can be instantiated |
| Can contain abstract methods | Provides implementations for required abstract methods |
| Defines a common structure | Implements actual functionality |
| Often used as a base class | Often used to create objects |

---

## 7. Difference Between Encapsulation and Abstraction

| Encapsulation | Abstraction |
|---|---|
| Combines data and methods into a class | Hides implementation details |
| Controls access to data | Shows essential features |
| Focuses on data protection and access | Focuses on simplicity and essential behavior |
| Uses access conventions and properties | Uses abstract classes and methods |

---

## Quick Revision

1. Abstraction hides internal implementation details.
2. It shows only essential features to the user.
3. Python supports abstraction through the `abc` module.
4. `ABC` is used to create abstract base classes.
5. `@abstractmethod` is used to declare abstract methods.
6. Abstract classes cannot be instantiated directly.
7. Child classes provide implementations of abstract methods.
8. A concrete child class must implement all inherited abstract methods.

## What I Learned Today

- Introduction to Data Abstraction.
- Understanding real-world abstraction examples.
- Difference between abstract classes and abstract methods.
- Using the `abc` module.
- Working with `ABC` and `@abstractmethod`.
- Implementing abstraction using inheritance.
- Difference between encapsulation and abstraction.

**Day 27 Completed – Python Data Abstraction.**
