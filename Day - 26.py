# Day 26 – Python OOP Concepts

## 1. Method Overloading

**Method Overloading** means defining methods with the same name but different parameters.

In languages like Java and C++, method overloading is directly supported. Python does not support traditional method overloading using multiple definitions with the same name. If we define a method again, the latest definition replaces the earlier one.

However, we can achieve similar behavior using:
- Default arguments.
- Variable-length arguments (`*args`).
- Conditional statements.

### Example 1: Using Default Arguments

```python
class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
```

**Output:**

```text
30
60
```

### Example 2: Using *args

`*args` allows a method to accept any number of positional arguments.

```python
class Calculator:

    def add(self, *numbers):
        total = 0

        for num in numbers:
            total += num

        return total


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10, 20, 30, 40))
```

**Output:**

```text
30
60
100
```

### Explanation

- `*numbers` accepts multiple values.
- The `for` loop adds all the numbers.
- We can call the same method with different numbers of arguments.

**Remember:** Python does not have traditional method overloading, but default arguments and `*args` help us achieve similar functionality.

---

## 2. Method Overriding

**Method Overriding** happens when a child class provides its own implementation of a method that already exists in its parent class.

In simple words, the child class changes the behavior of an inherited method.

### Why do we use method overriding?

- To customize parent class behavior.
- To provide different implementations.
- To achieve runtime polymorphism.
- To make programs more flexible.

### Example

```python
class Animal:

    def sound(self):
        print("Animals make sounds")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog1 = Dog()
cat1 = Cat()

dog1.sound()
cat1.sound()
```

**Output:**

```text
Dog barks
Cat meows
```

### Explanation

- `Animal` is the parent class.
- `Dog` and `Cat` are child classes.
- Both child classes override the `sound()` method.
- Each child class provides its own implementation.

### Another Example

```python
class Employee:

    def work(self):
        print("Employee is working")


class Developer(Employee):

    def work(self):
        print("Developer is writing Python code")


emp1 = Employee()
dev1 = Developer()

emp1.work()
dev1.work()
```

**Output:**

```text
Employee is working
Developer is writing Python code
```

---

## 3. Operator Overloading

**Operator Overloading** means giving special behavior to operators when they are used with objects of a class.

For example:
- `+` performs addition with numbers.
- `-` performs subtraction.
- `*` performs multiplication.

In Python, we can customize operators for our own classes using special methods, also called magic methods or dunder methods.

### Common Operator Overloading Methods

| Operator | Special Method |
|---|---|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `==` | `__eq__()` |
| `<` | `__lt__()` |
| `>` | `__gt__()` |

### Example 1: Overloading the + Operator

```python
class Addition:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


obj1 = Addition(10)
obj2 = Addition(20)

result = obj1 + obj2

print("Addition:", result)
```

**Output:**

```text
Addition: 30
```

### Explanation

- `obj1` contains the value 10.
- `obj2` contains the value 20.
- The `+` operator calls the `__add__()` method.
- The method adds both object values and returns 30.

### Example 2: Overloading the * Operator

```python
class Multiply:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


obj1 = Multiply(5)
obj2 = Multiply(4)

print("Multiplication:", obj1 * obj2)
```

**Output:**

```text
Multiplication: 20
```

**Remember:** Operator overloading allows operators to work with user-defined objects in a meaningful way.

---

## 4. super() Method

`super()` is a built-in Python function used to access methods from a parent class.

It is commonly used inside a child class to call the parent class constructor or other parent class methods.

### Why do we use super()?

- To call the parent class constructor.
- To reuse parent class methods.
- To avoid repeating parent class code.
- To extend existing functionality.

### Example 1: Using super() to Call a Parent Constructor

```python
class Parent:

    def __init__(self):
        print("Parent constructor called")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("Child constructor called")


obj = Child()
```

**Output:**

```text
Parent constructor called
Child constructor called
```

### Explanation

- `Parent` contains a constructor.
- `Child` inherits from `Parent`.
- `super().__init__()` calls the parent constructor.
- Then the child constructor continues executing.

### Example 2: Using super() with Attributes

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student("Rahul", "Python")

student1.display()
```

**Output:**

```text
Name: Rahul
Course: Python
```

### Example 3: Using super() to Call a Parent Method

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog1 = Dog()

dog1.sound()
```

**Output:**

```text
Animal makes a sound
Dog barks
```

**Remember:** `super()` is especially useful when working with inheritance. It follows Python's Method Resolution Order (MRO) to find the next class in the inheritance chain.

---

## Difference Between All Four Concepts

| Concept | Meaning |
|---|---|
| Method Overloading | Similar method behavior with different arguments |
| Method Overriding | Child class changes an inherited method |
| Operator Overloading | Customizes operators for objects |
| `super()` | Accesses the next class in the MRO |

## Quick Revision

1. Method overloading can be achieved using default arguments and `*args` in Python.
2. Method overriding allows a child class to redefine a parent method.
3. Operator overloading customizes operators for user-defined objects.
4. `__add__()` is used to customize the `+` operator.
5. `__sub__()` is used to customize the `-` operator.
6. `super()` helps access parent class functionality.
7. `super().__init__()` calls the parent class constructor.
8. Python uses MRO to determine the method lookup order.

## What I Learned Today

- Understanding method overloading.
- Using default arguments and `*args`.
- Understanding method overriding.
- Implementing operator overloading.
- Learning special methods such as `__add__()` and `__mul__()`.
- Understanding the `super()` function.
- Calling parent class constructors and methods.

**Day 26 Completed – Python OOP Concepts.**
