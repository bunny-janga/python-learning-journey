# Day 1 – Python Basics & Practice

## 1. Ice Breaker & Introduction

Today we started with a simple introduction. I introduced myself and talked about my interest in programming and technology.

The main purpose was to get comfortable with everyone and start the learning journey.

---

## 2. What is Programming?

Programming means giving instructions to a computer to perform a task.

We use programming languages to write these instructions.

### Example Program

```python
print("Hello, World!")
print("My name is Bunny")
print("I am learning Python")
```

### Output

```text
Hello, World!
My name is Bunny
I am learning Python
```

---

## 3. Procedural Programming

Procedural programming means writing a program step by step using functions and procedures.

The focus is mainly on **what steps need to be performed**.

### Example Program

```python
def add_numbers(a, b):
    return a + b

num1 = 10
num2 = 20

result = add_numbers(num1, num2)

print("Result:", result)
```

### Output

```text
Result: 30
```

Here, the program follows a sequence of steps:

1. Take two numbers
2. Pass them to the function
3. Add them
4. Display the result

---

## 4. Object-Oriented Programming

OOP is a programming approach based on **classes and objects**.

A class is like a blueprint, and an object is created from that class.

### Example Program

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Bunny", 20)

student1.display()
```

### Output

```text
Name: Bunny
Age: 20
```

Here:

* `Student` → Class
* `student1` → Object
* `name` and `age` → Data
* `display()` → Method

---

## 5. What is Python?

Python is a high-level programming language.

I found Python easy to read because its syntax is simple.

### My First Python Program

```python
message = "I am learning Python"

print(message)
```

### Output

```text
I am learning Python
```

---

## 6. Why Python?

Python is popular because:

* It has simple syntax.
* It is beginner-friendly.
* It has many libraries.
* It has a large community.
* It is used in many different fields.

### Small Example

```python
name = "Bunny"
age = 20

print("Name:", name)
print("Age:", age)
```

This shows how easily we can create variables and display their values in Python.

---

## 7. History and Applications of Python

Python was created by **Guido van Rossum** and was first released in **1991**.

Python is now used in many areas.

### Where Python is Used

* Web Development
* Artificial Intelligence
* Machine Learning
* Data Science
* Automation
* Backend Development
* Scripting

### Simple Automation Example

```python
for i in range(1, 6):
    print("Learning Python - Day", i)
```

### Output

```text
Learning Python - Day 1
Learning Python - Day 2
Learning Python - Day 3
Learning Python - Day 4
Learning Python - Day 5
```

---

## 8. Procedural vs OOP

### Procedural Programming

The program is mainly organized around functions and a sequence of steps.

### OOP

The program is organized around classes and objects.

| Procedural                              | OOP                                   |
| --------------------------------------- | ------------------------------------- |
| Focuses on functions                    | Focuses on objects                    |
| Step-by-step approach                   | Object-based approach                 |
| Functions and data are usually separate | Data and methods are grouped together |
| Example: C                              | Examples: Python, Java, C++           |

### Simple Comparison Example

**Procedural style:**

```python
name = "Bunny"

def greet(name):
    print("Hello", name)

greet(name)
```

**OOP style:**

```python
class Student:
    def greet(self):
        print("Hello Bunny")

student = Student()
student.greet()
```

Both programs produce a similar result, but they organize the code differently.

---

## 9. Memory Allocation – Basic Idea

Memory allocation means giving memory space to variables, data, and objects while a program is running.

In procedural programming, we commonly work with variables and function calls.

In OOP, objects are created from classes and memory is used for those objects.

The exact way memory is allocated depends on the programming language and its runtime.

---

# Practice Programs

I also practiced a few simple Python programs today.

### Program 1 – Add Two Numbers

```python
a = 10
b = 20

sum = a + b

print("Sum:", sum)
```

### Program 2 – Find Even or Odd

```python
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### Program 3 – Simple Calculator

```python
a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

### Program 4 – Print Numbers

```python
for number in range(1, 6):
    print(number)
```

### Output

```text
1
2
3
4
5
```

---

# Day 1 Takeaway

Today I understood the basic idea of programming, procedural programming, OOP, and Python.

I also started writing simple Python programs instead of only reading the concepts.

**Next step:** Practice more Python programs and understand the basics by writing code myself.
