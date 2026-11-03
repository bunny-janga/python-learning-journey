# Day 24 – Python OOP Concepts

## 1. Constructors

A **constructor** is a special method in Python that is automatically called when an object is created.

In Python, we use the `__init__()` method as a constructor to initialize the attributes of an object.

### Why do we use constructors?

- To initialize object attributes.
- To assign values when an object is created.
- To avoid writing the same initialization code repeatedly.
- To make objects easier to create and manage.

### Syntax

```python
class ClassName:
    def __init__(self):
        # Initialization code
        pass
```

### Example 1: Default Constructor

A constructor that does not take any additional arguments apart from `self` is commonly called a default or no-argument constructor.

```python
class Student:

    def __init__(self):
        print("Student object created")


student1 = Student()
```

**Output:**

```text
Student object created
```

### Example 2: Parameterized Constructor

A parameterized constructor accepts values when an object is created.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Rahul", 21)

student1.display()
```

**Output:**

```text
Name: Rahul
Age: 21
```

### Example 3: Creating Multiple Objects

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("Arun", 25000)
emp2 = Employee("Priya", 30000)

emp1.display()

print("--------------")

emp2.display()
```

**Output:**

```text
Employee Name: Arun
Salary: 25000
--------------
Employee Name: Priya
Salary: 30000
```

**Remember:** Python's `__init__()` initializes an object after it has been created. The actual object creation is handled by `__new__()`.

---

## 2. Self Keyword

`self` is a reference to the current object of a class.

It helps us access the attributes and methods belonging to that particular object.

In Python, `self` is written as the first parameter of an instance method. It is passed automatically when the method is called through an object.

### Why do we use self?

- To access instance variables.
- To call other instance methods.
- To work with individual object data.
- To distinguish attributes of different objects.

### Example 1: Using self

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Rahul", 21)

student1.display()
```

**Output:**

```text
Name: Rahul
Age: 21
```

### Example 2: Understanding self with Multiple Objects

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Welcome", self.name)


student1 = Student("Rahul")
student2 = Student("Priya")

student1.display()
student2.display()
```

**Output:**

```text
Welcome Rahul
Welcome Priya
```

Here:
- `student1` refers to the first object.
- `student2` refers to the second object.
- `self.name` accesses the name belonging to the current object.

### Example 3: Calling a Method Using self

```python
class Calculator:

    def add(self, a, b):
        return a + b

    def display(self):
        result = self.add(10, 20)
        print("Addition:", result)


calc = Calculator()

calc.display()
```

**Output:**

```text
Addition: 30
```

**Remember:** `self` is not a Python keyword. It is a naming convention, but using `self` is the standard practice.

---

## 3. Encapsulation

**Encapsulation** is one of the main concepts of Object-Oriented Programming.

It means combining data (attributes) and methods into a single class and controlling how the data is accessed or modified.

In simple words, encapsulation helps protect an object's data from being changed directly in an uncontrolled way.

### Why do we use encapsulation?

- To protect data.
- To control access to attributes.
- To improve code security and organization.
- To validate values before updating them.
- To make code easier to maintain.

### Access Conventions in Python

Python uses naming conventions to indicate how attributes should be accessed.

**A. Public Members**

Public attributes can be accessed from anywhere.

```python
class Student:

    def __init__(self):
        self.name = "Rahul"


student1 = Student()

print(student1.name)
```

**Output:**

```text
Rahul
```

**B. Protected Members**

A single underscore (`_`) indicates that an attribute is intended for internal use or use by subclasses.

It is a convention, not strict access protection.

```python
class Student:

    def __init__(self):
        self._age = 21


student1 = Student()

print(student1._age)
```

**Output:**

```text
21
```

**C. Private Members**

A double underscore (`__`) triggers name mangling. It makes direct access using the original attribute name difficult, but it does not provide absolute privacy.

```python
class Student:

    def __init__(self):
        self.__marks = 90


student1 = Student()

print(student1._Student__marks)
```

**Output:**

```text
90
```

The example demonstrates Python's name mangling. Normally, we should access private data through methods or properties instead.

### Example: Encapsulation Using Getter and Setter Methods

A getter is used to read a value, and a setter is used to update a value with validation.

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")


account = BankAccount(5000)

print("Current Balance:", account.get_balance())

account.set_balance(8000)

print("Updated Balance:", account.get_balance())

account.set_balance(-1000)
```

**Output:**

```text
Current Balance: 5000
Updated Balance: 8000
Balance cannot be negative
```

Here:
- `__balance` is a private-style attribute.
- `get_balance()` reads the balance.
- `set_balance()` updates the balance only if the amount is valid.

### Encapsulation Using @property

Python also provides `@property` to access and update attributes in a clean way.

```python
class Employee:

    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Salary must be positive")


emp1 = Employee(25000)

print("Salary:", emp1.salary)

emp1.salary = 30000

print("Updated Salary:", emp1.salary)
```

**Output:**

```text
Salary: 25000
Updated Salary: 30000
```

---

## Difference Between Constructors, self and Encapsulation

| Concept | Meaning |
|---|---|
| Constructor | Initializes an object's attributes |
| `__init__()` | Python initialization method |
| `self` | Refers to the current object |
| Encapsulation | Combines data and methods and controls access |
| Getter | Reads an attribute value |
| Setter | Updates an attribute value |

## Quick Revision

1. A constructor initializes an object when it is created.
2. `__init__()` is commonly used as the constructor in Python.
3. `self` refers to the current object.
4. Encapsulation combines data and methods inside a class.
5. A single underscore indicates an internal-use convention.
6. A double underscore triggers name mangling.
7. Getter and setter methods help control access to data.

## What I Learned Today

- Understanding constructors in Python.
- Difference between default and parameterized constructors.
- How to use the `self` reference.
- How `self` works with multiple objects.
- Understanding encapsulation.
- Public, protected and private naming conventions.
- Using getter and setter methods.
- Implementing encapsulation with `@property`.

**Day 24 Completed – Python OOP Concepts.**
