# Day 29 – Regular Expressions (Regex) in Python

## 1. Introduction to Regular Expressions (Regex)

Regular Expression, commonly called Regex, is a sequence of characters used to search, match, and validate patterns in text.

In Python, we use the built-in `re` module to work with regular expressions.

Regex is useful when we want to:

- Validate email addresses.
- Check mobile numbers.
- Search for specific words in text.
- Find numbers inside a sentence.
- Validate passwords.
- Extract useful information from text.

### Import the Regex Module

```python
import re
```

### Simple Example

```python
import re

text = "I am learning Python programming"

result = re.search("Python", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")
```

**Output:**

```text
Pattern found
```

**Explanation:**

The `re.search()` function searches for the given pattern anywhere in the text. If it finds a match, it returns a match object; otherwise, it returns `None`.

## 2. Regex Meta Characters

Meta characters are special symbols used to define search patterns.

They help us create flexible patterns instead of searching for only exact words.

### Common Meta Characters

| Meta Character | Meaning | Example |
|---|---|---|
| `.` | Matches any character except newline | `a.c` |
| `^` | Matches the beginning of a string | `^Hello` |
| `$` | Matches the end of a string | `world$` |
| `*` | Matches zero or more repetitions | `ab*` |
| `+` | Matches one or more repetitions | `ab+` |
| `?` | Matches zero or one repetition | `colou?r` |
| `{n}` | Matches exactly n repetitions | `\d{4}` |
| `{n,m}` | Matches between n and m repetitions | `\d{2,4}` |
| `[]` | Matches any one character inside brackets | `[abc]` |
| `[^ ]` | Matches a character not inside brackets | `[^0-9]` |
| `\` | Gives special meaning to a character | `\d` |
| `|` | Matches either pattern | `cat|dog` |
| `()` | Groups patterns | `(ab)+` |

### Examples of Meta Characters

**Example 1: Dot (.)**

```python
import re

text = "cat cot cut"

result = re.findall("c.t", text)

print(result)
```

**Output:**

```text
['cat', 'cot', 'cut']
```

The dot matches any single character except a newline.

**Example 2: Caret (^)**

```python
import re

text = "Python is easy"

result = re.findall("^Python", text)

print(result)
```

**Output:**

```text
['Python']
```

The `^` symbol checks whether the text starts with the given pattern.

**Example 3: Dollar ($)**

```python
import re

text = "I love Python"

result = re.findall("Python$", text)

print(result)
```

**Output:**

```text
['Python']
```

The `$` symbol checks whether the text ends with the given pattern.

**Example 4: Plus (+)**

```python
import re

text = "ab abb abbb"

result = re.findall("ab+", text)

print(result)
```

**Output:**

```text
['ab', 'abb', 'abbb']
```

The `+` symbol matches one or more repetitions of the preceding character.

## 3. Pattern Matching in Python

Pattern matching means checking whether a particular pattern exists in a given string.

Python provides several useful functions through the `re` module.

### 1. re.match()

Checks for a pattern only at the beginning of a string.

```python
import re

text = "Python is powerful"

result = re.match("Python", text)

if result:
    print("Match found")
else:
    print("No match found")
```

**Output:**

```text
Match found
```

### 2. re.search()

Searches for a pattern anywhere in a string.

```python
import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")
```

**Output:**

```text
Pattern found
```

### 3. re.findall()

Returns all non-overlapping matches as a list.

```python
import re

text = "My numbers are 10, 20, 30 and 40"

result = re.findall(r"\d+", text)

print(result)
```

**Output:**

```text
['10', '20', '30', '40']
```

### 4. re.finditer()

Returns an iterator containing match objects for all matches.

```python
import re

text = "Python 10 Java 20 C++ 30"

result = re.finditer(r"\d+", text)

for match in result:
    print(match.group())
```

**Output:**

```text
10
20
30
```

### 5. re.sub()

Replaces matched patterns with another value.

```python
import re

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)
```

**Output:**

```text
I like Python
```

### 6. re.split()

Splits a string wherever the given pattern matches.

```python
import re

text = "Python,Java;C++"

result = re.split(r"[,;]", text)

print(result)
```

**Output:**

```text
['Python', 'Java', 'C++']
```

### Common Regex Character Classes

| Pattern | Meaning |
|---|---|
| `\d` | Matches any digit (0–9) |
| `\D` | Matches any non-digit |
| `\w` | Matches letters, digits, and underscore |
| `\W` | Matches characters other than word characters |
| `\s` | Matches whitespace |
| `\S` | Matches non-whitespace |
| `\b` | Matches a word boundary |
| `\B` | Matches a position that is not a word boundary |

### Example: Extract Numbers

```python
import re

text = "My age is 21 and my marks are 95"

result = re.findall(r"\d+", text)

print(result)
```

**Output:**

```text
['21', '95']
```

**Note:** The `r` before a pattern creates a raw string. It is useful when writing Regex patterns containing backslashes.

## 4. Form Validation Project Using Regex

Now let's apply our Regex knowledge in a small real-world project.

A Form Validation System checks whether the information entered by a user follows the required format.

For example:

- Name should contain valid characters.
- Email should follow a valid email format.
- Mobile number should contain 10 digits.
- Password should meet basic security requirements.

### Project Requirements

| Field | Validation Rule |
|---|---|
| Name | Letters and spaces only |
| Email | Valid email format |
| Mobile | Exactly 10 digits |
| Password | At least 8 characters, including uppercase, lowercase, digit, and special character |

### Complete Python Program

```python
import re

def validate_name(name):
    pattern = r"^[A-Za-z ]+$"

    if re.fullmatch(pattern, name):
        return True
    return False


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(pattern, email):
        return True
    return False


def validate_mobile(mobile):
    pattern = r"^[6-9]\d{9}$"

    if re.fullmatch(pattern, mobile):
        return True
    return False


def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%*?&])[A-Za-z\d@#$!%*?&]{8,}$"

    if re.fullmatch(pattern, password):
        return True
    return False


print("===== FORM VALIDATION SYSTEM =====")

name = input("Enter your name: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
password = input("Enter your password: ")

print("\n===== VALIDATION RESULTS =====")

if validate_name(name):
    print("Name: Valid")
else:
    print("Name: Invalid")

if validate_email(email):
    print("Email: Valid")
else:
    print("Email: Invalid")

if validate_mobile(mobile):
    print("Mobile: Valid")
else:
    print("Mobile: Invalid")

if validate_password(password):
    print("Password: Valid")
else:
    print("Password: Invalid")

if (validate_name(name) and
    validate_email(email) and
    validate_mobile(mobile) and
    validate_password(password)):

    print("\nForm submitted successfully!")
else:
    print("\nPlease enter valid information.")
```

### Sample Output

```text
===== FORM VALIDATION SYSTEM =====

Enter your name: Rahul Kumar
Enter your email: rahul@gmail.com
Enter your mobile number: 9876543210
Enter your password: Rahul@123

===== VALIDATION RESULTS =====

Name: Valid
Email: Valid
Mobile: Valid
Password: Valid

Form submitted successfully!
```

### Understanding the Password Regex

Let's understand this pattern:

```python
r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!%*?&])[A-Za-z\d@#$!%*?&]{8,}$"
```

| Pattern | Meaning |
|---|---|
| `^` | Starts checking from the beginning |
| `(?=.*[a-z])` | At least one lowercase letter |
| `(?=.*[A-Z])` | At least one uppercase letter |
| `(?=.*\d)` | At least one digit |
| `(?=.*[@#$!%*?&])` | At least one allowed special character |
| `[A-Za-z\d@#$!%*?&]{8,}` | At least 8 allowed characters |
| `$` | Ends the pattern |

**Important:** This is a basic learning project. Regex validation checks the format, but it does not prove that an email address or mobile number actually exists. Real applications should also verify contact details and use secure password storage.

## 5. How to Run the Project

1. Open Visual Studio Code.
2. Create a file named `form_validation.py`.
3. Copy the complete Form Validation program into the file.
4. Save the file.
5. Open the terminal.
6. Run the following command:

```bash
python form_validation.py
```

## 6. What I Learned Today

After completing Day 29, I understood:

- What Regular Expressions are.
- How to import and use the `re` module.
- How Regex meta characters work.
- How to use character classes such as `\d`, `\w`, and `\s`.
- How to use `match()`, `search()`, and `findall()`.
- How to replace and split text using Regex.
- How to validate names, emails, mobile numbers, and passwords.
- How to build a simple Form Validation Project.

## 7. Day 29 – Quick Revision

| Function | Purpose |
|---|---|
| `re.match()` | Checks the beginning of a string |
| `re.search()` | Searches anywhere in a string |
| `re.findall()` | Returns all matches in a list |
| `re.finditer()` | Returns match objects through an iterator |
| `re.sub()` | Replaces matched text |
| `re.split()` | Splits text based on a pattern |
| `re.fullmatch()` | Checks whether the entire string matches |

**Day 29 completed: Regular Expressions and Form Validation Project using Python.**
