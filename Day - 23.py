# Day 23 – Python OOP (Object-Oriented Programming)

## 1. What is OOP?

OOP stands for **Object-Oriented Programming**.

It is a programming approach that organizes code using classes and objects.

In OOP, we combine data and functions into a single unit called an object.

### Why do we use OOP?

- Code reusability.
- Easy to understand and maintain.
- Better code organization.
- Reduces code duplication.
- Useful for developing large applications.

### Real-Time Example

Think about a car.

A car has:
- Brand
- Color
- Model
- Speed

A car can perform actions such as:
- Start
- Stop
- Accelerate
- Brake

In Python, we can represent a car using a class and objects.

---

## 2. Classes

A **class** is a blueprint or template used to create objects.

It defines the attributes and methods that its objects can have.

### Syntax

```python
class ClassName:
    # Attributes
    # Methods
    pass
```

### Example

```python
class Student:
    name = "Rahul"
    age = 21

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
```

**Output:**

```text
No output
```

Explanation: We created a class, but we did not create an object or call the method. Therefore, nothing is displayed.

---

## 3. Objects

An **object** is an instance of a class.

We create objects to access the attributes and methods defined inside a class.

### Syntax

```python
object_name = ClassName()
```

### Example

```python
class Student:
    name = "Rahul"
    age = 21

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student()

student1.display()
```

**Output:**

```text
Name: Rahul
Age: 21
```

### Creating Multiple Objects

```python
class Student:
    def display(self):
        print("Welcome to Python OOP")


student1 = Student()
student2 = Student()

student1.display()
student2.display()
```

**Output:**

```text
Welcome to Python OOP
Welcome to Python OOP
```

Explanation: We created two different objects using the same class.

---

## 4. Attributes

**Attributes** are variables that store the data or properties of an object.

For example, a student can have a name, age, roll number and course.

There are two common types of attributes:

### A. Instance Attributes

Instance attributes belong to individual objects.

They are usually created using `self` inside the `__init__()` method.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Rahul", 21)
student2 = Student("Priya", 22)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)
```

**Output:**

```text
Rahul
21
Priya
22
```

### B. Class Attributes

Class attributes are shared by all objects of a class unless an object overrides the attribute.

```python
class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Rahul")
student2 = Student("Priya")

print(student1.name)
print(student1.college)

print(student2.name)
print(student2.college)
```

**Output:**

```text
Rahul
ABC College
Priya
ABC College
```

### Difference Between Instance and Class Attributes

| Instance Attributes | Class Attributes |
|---|---|
| Belong to individual objects | Belong to the class |
| Usually created using `self` | Defined directly inside the class |
| Can have different values for each object | Shared by objects by default |

---

## 5. Methods

A **method** is a function defined inside a class.

Methods describe the actions that an object can perform.

### Example

```python
class Student:
    def display(self):
        print("Student details")

    def study(self):
        print("Student is studying Python")


student1 = Student()

student1.display()
student1.study()
```

**Output:**

```text
Student details
Student is studying Python
```

### What is self?

`self` represents the current object of the class.

It is used to access the attributes and methods belonging to that object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)


student1 = Student("Rahul")
student2 = Student("Priya")

student1.display()
student2.display()
```

**Output:**

```text
Student Name: Rahul
Student Name: Priya
```

### What is __init__()?

`__init__()` is a special method in Python that is automatically called when a new object is created.

It is commonly used to initialize object attributes.

Example:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("Arun", 25000)

emp1.display()
```

**Output:**

```text
Employee: Arun
Salary: 25000
```

---

## Complete Example – Student Management

```python
class Student:

    college = "ABC College"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("College:", Student.college)


student1 = Student("Rahul", 21, "Python")
student2 = Student("Priya", 22, "Java")

student1.display_details()

print("----------------")

student2.display_details()
```

**Output:**

```text
Student Name: Rahul
Age: 21
Course: Python
College: ABC College
----------------
Student Name: Priya
Age: 22
Course: Java
College: ABC College
```

---

## Quick Revision

| Topic | Meaning |
|---|---|
| OOP | Object-Oriented Programming |
| Class | Blueprint for creating objects |
| Object | Instance of a class |
| Attributes | Variables that store data |
| Methods | Functions defined inside a class |
| self | Refers to the current object |
| __init__() | Initializes an object's attributes |

## What I Learned Today

- Introduction to Object-Oriented Programming.
- How to create classes in Python.
- How to create and use objects.
- Difference between class and instance attributes.
- How to define and call methods.
- Understanding `self` and `__init__()`.

**Day 23 completed – Python OOP Basics.**
