# Day 28 – Library Management System Using Python

## 1. Introduction

A Library Management System is a simple real-world Python project used to manage books in a library.

Instead of maintaining book details manually, we can use Python to perform tasks such as:

- Add new books
- Display all available books
- Search for a book
- Issue a book
- Return a book
- Delete a book

This project helps us understand how Python concepts work together in a practical application.

## 2. Project Objectives

The main objective is to create a basic library system where users can manage books easily.

**Features:**

1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

## 3. Concepts Used in This Project

Before writing the program, let's understand the Python concepts used.

| Python Concept | Purpose |
|---|---|
| Classes and Objects | Organize the library system |
| Constructors | Initialize book details |
| Lists | Store book records |
| Dictionaries | Store individual book information |
| Functions | Perform different operations |
| Conditional Statements | Check book availability |
| Loops | Display the menu repeatedly |
| Exception Handling | Handle invalid inputs |

## 4. Create a Book Class

A book contains information such as its ID, title, author, and availability.

We can use a class to represent a book.

```python
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display_book(self):
        status = "Available" if self.available else "Issued"

        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)
```

**Explanation:**

- `class Book`: Creates a Book class.
- `__init__()`: Initializes book details.
- `self`: Refers to the current object.
- `available`: Tracks whether the book is available.
- `display_book()`: Displays book information.

## 5. Create a Library Class

The Library class manages all the books.

```python
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            book.display_book()
            print("------------------")
```

**Explanation:**

- `self.books = []` creates an empty list.
- `add_book()` adds a new book.
- `view_books()` displays all books.
- A `for` loop is used to access each book.

## 6. Search for a Book

Searching helps us find a particular book using its ID.

```python
def search_book(self, book_id):
    for book in self.books:
        if book.book_id == book_id:
            book.display_book()
            return

    print("Book not found.")
```

**Explanation:**

The method checks every book in the list. If the entered ID matches, it displays the book details.

## 7. Issue a Book

When a user wants to borrow a book, the system checks whether it is available.

```python
def issue_book(self, book_id):
    for book in self.books:
        if book.book_id == book_id:
            if book.available:
                book.available = False
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")
```

**Explanation:**

- If the book is available, its status becomes `False`.
- If it is already issued, the system displays a message.
- If the book ID does not exist, it displays "Book not found."

## 8. Return a Book

When a user returns a book, its availability changes back to `True`.

```python
def return_book(self, book_id):
    for book in self.books:
        if book.book_id == book_id:
            if not book.available:
                book.available = True
                print("Book returned successfully!")
            else:
                print("This book was not issued.")
            return

    print("Book not found.")
```

## 9. Delete a Book

We can remove a book from the library using its ID.

```python
def delete_book(self, book_id):
    for book in self.books:
        if book.book_id == book_id:
            if not book.available:
                print("Cannot delete an issued book.")
                return

            self.books.remove(book)
            print("Book deleted successfully!")
            return

    print("Book not found.")
```

**Explanation:**

The method searches for the given book ID and removes the matching book if it is not currently issued.

## 10. Complete Library Management System

Now let's combine all the concepts into one complete program.

```python
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display_book(self):
        status = "Available" if self.available else "Issued"

        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.book_id == book.book_id:
                print("Book ID already exists.")
                return

        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            book.display_book()
            print("------------------")

    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.display_book()
                return

        print("Book not found.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
                return

        print("Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")
                return

        print("Book not found.")

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    print("Cannot delete an issued book.")
                    return

                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found.")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            book_id = int(input("Enter Book ID to search: "))
            library.search_book(book_id)

        elif choice == 4:
            book_id = int(input("Enter Book ID to issue: "))
            library.issue_book(book_id)

        elif choice == 5:
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(book_id)

        elif choice == 6:
            book_id = int(input("Enter Book ID to delete: "))
            library.delete_book(book_id)

        elif choice == 7:
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please select from 1 to 7.")

    except ValueError:
        print("Please enter a valid number.")
```

## 11. Sample Output

```text
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit

Enter your choice: 1

Enter Book ID: 101
Enter Book Title: Python Programming
Enter Author Name: John Smith

Book added successfully!
```

**Issuing a book:**

```text
Enter your choice: 4
Enter Book ID to issue: 101

Book issued successfully!
```

**Returning a book:**

```text
Enter your choice: 5
Enter Book ID to return: 101

Book returned successfully!
```

**Exiting the application:**

```text
Enter your choice: 7

Thank you for using the Library Management System!
```

## 12. How to Run the Project

1. Open Visual Studio Code.
2. Create a folder named `Library-Management-System`.
3. Create a Python file named `library_management.py`.
4. Copy the complete program into the file.
5. Save the file.
6. Open the VS Code terminal.
7. Run the following command:

```bash
python library_management.py
```

## 13. Project Limitations and Future Improvements

This is a beginner-level project. Currently, book details are stored in a Python list, so the records disappear when the program closes.

We can improve this project in the future by adding:

- File handling to save book records permanently.
- MySQL database connectivity.
- Student or member registration.
- Due dates and fine calculation.
- Login system for librarians.
- A graphical user interface using Tkinter.

## 14. What I Learned Today

After completing this project, I understood how to:

- Create classes and objects.
- Use constructors and instance attributes.
- Work with lists and objects.
- Create methods for different operations.
- Use loops and conditional statements.
- Handle invalid user input with `try-except`.
- Build a real-world application using Python.

## 15. Day 28 – Quick Revision

| Topic | Purpose |
|---|---|
| Class | Defines the structure of an object |
| Object | Represents an individual book |
| Constructor | Initializes book details |
| List | Stores multiple books |
| Method | Performs a specific operation |
| Loop | Iterates through book records |
| Condition | Checks book availability |
| Exception Handling | Handles invalid input |

**Day 28 completed: Library Management System using Python.**

