# Day 21: Sending Emails Using Python

## 1. Introduction to Sending Emails Using Python

Python allows us to send emails automatically using its built-in modules.

Email automation is useful in real-world applications such as:

- Sending welcome emails to new users.
- Sending job application updates.
- Sending invoices and reports.
- Sending notifications and reminders.
- Sending course completion certificates.

Python provides the `smtplib` module to communicate with an SMTP email server.

### What is SMTP?

SMTP stands for Simple Mail Transfer Protocol.

It is a communication protocol used to send emails from one email server to another.

### Important modules

| Module | Purpose |
|---|---|
| `smtplib` | Connects to an SMTP server and sends emails |
| `email` | Creates email messages |
| `email.message` | Provides the `EmailMessage` class |
| `ssl` | Provides secure connections |
| `mimetypes` | Helps identify file content types |

### Basic email workflow

1. Import the required modules.
2. Configure the sender and receiver email addresses.
3. Create the email message.
4. Connect to the SMTP server.
5. Log in securely.
6. Send the email.
7. Close the connection.

---

## 2. Sending Emails Using Python

We can use Python's `smtplib` module to send a simple text email.

### Example: Sending a simple email

```python
import smtplib
import ssl

sender_email = "your_email@gmail.com"
receiver_email = "receiver@example.com"

# Use an app password, not your normal email password.
app_password = "YOUR_APP_PASSWORD"

subject = "Hello from Python"
message = "Hello! This email was sent using Python."

email_content = f"Subject: {subject}\n\n{message}"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(
    "smtp.gmail.com", 465, context=context
) as server:

    server.login(sender_email, app_password)

    server.sendmail(
        sender_email,
        receiver_email,
        email_content
    )

print("Email sent successfully!")
```

### Explanation

- `smtplib` connects Python to an SMTP server.
- `ssl` helps create a secure connection.
- `SMTP_SSL()` connects securely to Gmail's SMTP server.
- `login()` authenticates the sender.
- `sendmail()` sends the email to the receiver.
- `with` automatically closes the connection.

### Gmail configuration

For Gmail, the commonly used settings are:

| Setting | Value |
|---|---|
| SMTP server | `smtp.gmail.com` |
| SSL port | `465` |
| TLS port | `587` |

**Important:** Gmail generally requires an App Password when using this SMTP login method. App Passwords require 2-Step Verification and may not be available for every Google account.

Never share your App Password or upload it to GitHub.

---

## 3. Email Subject and Attachments

An email usually contains a sender, receiver, subject, and message body.

Sometimes we also need to attach files such as PDFs, images, documents, or reports.

Python's `EmailMessage` class makes it easier to create emails with attachments.

### Important email fields

| Field | Purpose |
|---|---|
| `From` | Sender's email address |
| `To` | Receiver's email address |
| `Subject` | Email subject |
| `set_content()` | Adds the email body |
| `add_attachment()` | Adds a file attachment |

### Example: Sending an email with a subject

```python
from email.message import EmailMessage
import smtplib
import ssl

sender_email = "your_email@gmail.com"
receiver_email = "receiver@example.com"
app_password = "YOUR_APP_PASSWORD"

email = EmailMessage()

email["From"] = sender_email
email["To"] = receiver_email
email["Subject"] = "Python Course Update"

email.set_content("""
Hello,

I am learning Python programming.

This email was created using Python.

Thank you!
""")

context = ssl.create_default_context()

with smtplib.SMTP_SSL(
    "smtp.gmail.com", 465, context=context
) as server:

    server.login(sender_email, app_password)
    server.send_message(email)

print("Email sent successfully!")
```

### Explanation

- `EmailMessage()` creates an email message.
- `From` identifies the sender.
- `To` identifies the receiver.
- `Subject` sets the subject line.
- `set_content()` adds the email body.
- `send_message()` sends the prepared email.

### Example: Sending an email with an attachment

```python
from email.message import EmailMessage
import smtplib
import ssl
import mimetypes
from pathlib import Path

sender_email = "your_email@gmail.com"
receiver_email = "receiver@example.com"
app_password = "YOUR_APP_PASSWORD"

file_path = Path("report.pdf")

email = EmailMessage()

email["From"] = sender_email
email["To"] = receiver_email
email["Subject"] = "Python Project Report"

email.set_content("""
Hello,

Please find the attached project report.

Thank you!
""")

# Read the attachment
with open(file_path, "rb") as file:
    file_data = file.read()

# Identify the file type
content_type, encoding = mimetypes.guess_type(file_path)

if content_type is None or encoding is not None:
    content_type = "application/octet-stream"

main_type, sub_type = content_type.split("/", 1)

# Add the attachment
email.add_attachment(
    file_data,
    maintype=main_type,
    subtype=sub_type,
    filename=file_path.name
)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(
    "smtp.gmail.com", 465, context=context
) as server:

    server.login(sender_email, app_password)
    server.send_message(email)

print("Email with attachment sent successfully!")
```

### Explanation

1. `Path()` stores the attachment file path.
2. `open(..., "rb")` reads the file in binary mode.
3. `mimetypes.guess_type()` identifies the file type.
4. `add_attachment()` attaches the file to the email.
5. `send_message()` sends the complete email.

**Important:** Make sure `report.pdf` exists in the same folder as your Python program, or provide its correct file path.

---

## 4. Bulk Mail Sending

Bulk email sending means sending emails to multiple recipients automatically.

For example, a company may send announcements, course updates, or event invitations to a list of registered users.

Python can automate this process using a loop.

### Concepts used

- Lists
- Loops
- Functions
- EmailMessage
- SMTP
- Exception handling

### Example: Sending individual emails to multiple recipients

```python
from email.message import EmailMessage
import smtplib
import ssl

sender_email = "your_email@gmail.com"
app_password = "YOUR_APP_PASSWORD"

recipients = [
    "student1@example.com",
    "student2@example.com",
    "student3@example.com"
]

context = ssl.create_default_context()

with smtplib.SMTP_SSL(
    "smtp.gmail.com", 465, context=context
) as server:

    server.login(sender_email, app_password)

    for receiver in recipients:

        email = EmailMessage()

        email["From"] = sender_email
        email["To"] = receiver
        email["Subject"] = "Python Course Announcement"

        email.set_content(f"""
Hello,

This is an announcement about our Python course.

Thank you,
Python Learning Team
""")

        try:
            server.send_message(email)
            print(f"Email sent successfully to {receiver}")

        except smtplib.SMTPException as error:
            print(f"Failed to send email to {receiver}: {error}")

print("Bulk email process completed.")
```

### Sample output

```text
Email sent successfully to student1@example.com
Email sent successfully to student2@example.com
Email sent successfully to student3@example.com
Bulk email process completed.
```

The output above is an example. Actual success depends on your SMTP account, authentication, recipient addresses, and server limits.

### Explanation

- The `recipients` list stores multiple email addresses.
- The `for` loop processes one recipient at a time.
- A new `EmailMessage` is created for each recipient.
- Each recipient receives an individual email.
- The `try-except` block handles sending errors.

### Why send individual emails?

If we put all recipients in the `To` field, everyone may see the other recipients' addresses.

Sending separate emails helps protect recipient privacy.

### Important points for bulk emailing

- Send emails only to people who have agreed to receive them.
- Avoid sending unwanted or spam messages.
- Follow your email provider's sending limits.
- Handle failed deliveries properly.
- Include an unsubscribe option for promotional mailing lists.
- For large mailing campaigns, use a dedicated email service.

---

## 5. Protecting Email Credentials

Never write your real email password or App Password directly inside a Python program that you plan to upload to GitHub.

One simple option is to use environment variables.

### Example using environment variables

```python
import os

sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_APP_PASSWORD")

if not sender_email or not app_password:
    raise ValueError("Email credentials are not configured.")

print("Email credentials loaded successfully.")
```

On Windows PowerShell, set the variables for the current terminal session:

```powershell
$env:EMAIL_ADDRESS="your_email@gmail.com"
$env:EMAIL_APP_PASSWORD="your_app_password"
```

Then run your Python program in the same terminal.

Do not print the password or commit it to GitHub. Add any `.env` file containing secrets to `.gitignore`.

---

## 6. Quick Revision

| Topic | Main purpose |
|---|---|
| `smtplib` | Connects to SMTP servers |
| `SMTP_SSL()` | Creates an SSL-secured SMTP connection |
| `login()` | Authenticates the sender |
| `EmailMessage()` | Creates an email message |
| `From` | Sets sender address |
| `To` | Sets receiver address |
| `Subject` | Sets email subject |
| `set_content()` | Adds message body |
| `add_attachment()` | Attaches files |
| `send_message()` | Sends an email |
| `for` loop | Processes multiple recipients |
| `ssl` | Supports secure connections |

## 7. What I Learned Today

- What SMTP means and how it works.
- How to send emails using Python.
- How to connect to Gmail's SMTP server.
- How to create email subjects and message bodies.
- How to attach PDF and other files.
- How to send emails to multiple recipients.
- How to handle email-sending errors.
- Why email credentials must be protected.

**Day 21 completed: Sending Emails Using Python.**
