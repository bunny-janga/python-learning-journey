# Day 25 – Python Inheritance

## Introduction to Inheritance

**Inheritance** is one of the important concepts of Object-Oriented Programming (OOP).

Inheritance allows one class to use the attributes and methods of another class.

The class whose properties are inherited is called the **Parent Class (Base Class)**.

The class that inherits those properties is called the **Child Class (Derived Class)**.

### Why do we use inheritance?

- Code reusability.
- Avoids writing the same code again.
- Makes programs easier to maintain.
- Helps organize related classes.
- Supports extending existing functionality.

### Basic Syntax

```python
class Parent:
    # Parent class properties
    pass


class Child(Parent):
    # Child class properties
    pass
```

Python supports five common types of inheritance:

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

---

## 1. Single Inheritance

**Single Inheritance** means one child class inherits from one parent class.

In simple words, one parent class passes its properties and methods to one child class.

### Structure

```text
Parent Class
     |
     v
Child Class
```

### Example

```python
class Animal:

    def eat(self):
        print("Animals can eat")


class Dog(Animal):

    def bark(self):
        print("Dog can bark")


dog1 = Dog()

dog1.eat()
dog1.bark()
```

**Output:**

```text
Animals can eat
Dog can bark
```

### Explanation

- `Animal` is the parent class.
- `Dog` is the child class.
- `Dog` inherits the `eat()` method from `Animal`.
- The `Dog` class also has its own `bark()` method.

---

## 2. Multiple Inheritance

**Multiple Inheritance** means one child class inherits from two or more parent classes.

In simple words, one child class can use the methods and attributes of multiple parent classes.

### Structure

```text
Parent 1       Parent 2
    \             /
     \           /
      \         /
       Child Class
```

### Example

```python
class Father:

    def father_property(self):
        print("Father owns a house")


class Mother:

    def mother_property(self):
        print("Mother owns gold")


class Child(Father, Mother):

    def child_info(self):
        print("This is the child")


child1 = Child()

child1.father_property()
child1.mother_property()
child1.child_info()
```

**Output:**

```text
Father owns a house
Mother owns gold
This is the child
```

### Explanation

- `Father` is the first parent class.
- `Mother` is the second parent class.
- `Child` inherits from both classes.
- The child can access methods from both parents.

**Note:** Python uses Method Resolution Order (MRO) to decide which method to use when multiple parent classes contain methods with the same name.

---

## 3. Multilevel Inheritance

**Multilevel Inheritance** means a class inherits from another child class, creating a chain of inheritance.

In simple words, one class inherits from a parent, and another class inherits from that child.

### Structure

```text
Grandparent Class
       |
       v
 Parent Class
       |
       v
  Child Class
```

### Example

```python
class Grandfather:

    def grandfather_info(self):
        print("Grandfather is the oldest generation")


class Father(Grandfather):

    def father_info(self):
        print("Father is the middle generation")


class Son(Father):

    def son_info(self):
        print("Son is the youngest generation")


son1 = Son()

son1.grandfather_info()
son1.father_info()
son1.son_info()
```

**Output:**

```text
Grandfather is the oldest generation
Father is the middle generation
Son is the youngest generation
```

### Explanation

- `Grandfather` is the first parent class.
- `Father` inherits from `Grandfather`.
- `Son` inherits from `Father`.
- The `Son` object can access methods from all three classes.

---

## 4. Hierarchical Inheritance

**Hierarchical Inheritance** means multiple child classes inherit from one common parent class.

In simple words, one parent class has two or more child classes.

### Structure

```text
          Parent Class
          /          \
         /            \
        v              v
    Child 1          Child 2
```

### Example

```python
class Animal:

    def eat(self):
        print("Animals can eat")


class Dog(Animal):

    def bark(self):
        print("Dog can bark")


class Cat(Animal):

    def meow(self):
        print("Cat can meow")


dog1 = Dog()
cat1 = Cat()

dog1.eat()
dog1.bark()

cat1.eat()
cat1.meow()
```

**Output:**

```text
Animals can eat
Dog can bark
Animals can eat
Cat can meow
```

### Explanation

- `Animal` is the common parent class.
- `Dog` and `Cat` are child classes.
- Both child classes inherit the `eat()` method.
- Each child class has its own separate method.

---

## 5. Hybrid Inheritance

**Hybrid Inheritance** is a combination of two or more types of inheritance.

It combines inheritance structures such as multiple, multilevel and hierarchical inheritance.

### Structure

```text
          A
         / \
        B   C
         \ /
          D
```

This example combines hierarchical inheritance and multiple inheritance.

### Example

```python
class A:

    def display_a(self):
        print("Class A")


class B(A):

    def display_b(self):
        print("Class B")


class C(A):

    def display_c(self):
        print("Class C")


class D(B, C):

    def display_d(self):
        print("Class D")


obj = D()

obj.display_a()
obj.display_b()
obj.display_c()
obj.display_d()
```

**Output:**

```text
Class A
Class B
Class C
Class D
```

### Explanation

- `A` is the common parent class.
- `B` and `C` inherit from `A`.
- `D` inherits from both `B` and `C`.
- The object of `D` can access methods from all four classes.

Python uses Method Resolution Order (MRO) to handle the inheritance order.

You can check the order using:

```python
print(D.mro())
```

**Output:**

```text
[<class '__main__.D'>, <class '__main__.B'>,
 <class '__main__.C'>, <class '__main__.A'>,
 <class 'object'>]
```

---

## Difference Between the Five Types of Inheritance

| Type | Meaning |
|---|---|
| Single | One child inherits from one parent |
| Multiple | One child inherits from multiple parents |
| Multilevel | Inheritance happens in a chain |
| Hierarchical | Multiple children inherit from one parent |
| Hybrid | Combination of two or more inheritance types |

## Real-World Examples

| Inheritance Type | Example |
|---|---|
| Single | Animal → Dog |
| Multiple | Child inherits from Father and Mother |
| Multilevel | Grandfather → Father → Son |
| Hierarchical | Animal → Dog and Cat |
| Hybrid | Combination of multiple inheritance structures |

## Quick Revision

1. Inheritance allows code reusability.
2. A parent class provides attributes and methods.
3. A child class inherits from a parent class.
4. Python supports five common types of inheritance.
5. Multiple inheritance allows a child to inherit from multiple parents.
6. Multilevel inheritance creates a chain of classes.
7. Hierarchical inheritance allows multiple children to share one parent.
8. Hybrid inheritance combines different inheritance structures.
9. MRO stands for Method Resolution Order.

## What I Learned Today

- Introduction to inheritance.
- Parent and child classes.
- Single inheritance.
- Multiple inheritance.
- Multilevel inheritance.
- Hierarchical inheritance.
- Hybrid inheritance.
- Method Resolution Order (MRO).

**Day 25 Completed – Python Inheritance.**
