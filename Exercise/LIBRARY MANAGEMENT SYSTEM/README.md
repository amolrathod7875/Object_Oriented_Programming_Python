# Library Management System

## Overview

This exercise demonstrates **composition** and **encapsulation** in Python through `Book`, `Member`, and `Library` classes. The library tracks books and members, supports borrowing and returning books, records which member holds each borrowed book, and lists available books. Invalid operations are rejected safely with descriptive messages.

## Tasks

- [x] Create `Book`, `Member`, and `Library` classes.
- [x] Give each book a unique ID, title, and availability status.
- [x] Give each member a unique ID and name.
- [x] Add books and members to the library.
- [x] Implement `borrow_book(member_id, book_id)`.
- [x] Implement `return_book(member_id, book_id)`.
- [x] Track which member currently holds each borrowed book.
- [x] Add a method to list available books.
- [x] Reject borrowing an unavailable/nonexistent book.
- [x] Reject returning a book by the wrong member.

## Pass Checks

- [x] Borrowing an available book marks it unavailable.
- [x] A second borrower cannot borrow the same book simultaneously.
- [x] Returning by the correct member restores availability.
- [x] Wrong-member and unknown-book actions are rejected safely.

## Code

```python
class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.is_available = True
        self.borrowed_by = None

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if book.book_id in self.books:
            return "Book ID already exists"
        self.books[book.book_id] = book
        return f"Book '{book.title}' added successfully"

    def add_member(self, member):
        if member.member_id in self.members:
            return "Member ID already exists"
        self.members[member.member_id] = member
        return f"Member '{member.name}' added successfully"

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            return "Member not found"
        if book_id not in self.books:
            return "Book not found"
        book = self.books[book_id]
        if not book.is_available:
            return "Book is already borrowed"
        book.is_available = False
        book.borrowed_by = member_id
        return f"Book '{book.title}' borrowed successfully"

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            return "Member not found"
        if book_id not in self.books:
            return "Book not found"
        book = self.books[book_id]
        if book.is_available:
            return "Book is not currently borrowed"
        if book.borrowed_by != member_id:
            return "Wrong member! Cannot return this book"
        book.is_available = True
        book.borrowed_by = None
        return f"Book '{book.title}' returned successfully"

    def list_available_books(self):
        found = False
        for book_id, book in self.books.items():
            if book.is_available:
                print(f"Book ID: {book_id}, Title: {book.title}")
                found = True
        if not found:
            print("No books are currently available")
```

## How the Code Satisfies the Tasks

- **Classes**: `Book`, `Member`, and `Library` model the domain with composition (Library holds books/members).
- **Book attributes**: `book_id`, `title`, `is_available`, and `borrowed_by` track state and holder.
- **Member attributes**: `member_id` and `name`.
- **Add operations**: `add_book`/`add_member` reject duplicate IDs.
- **Borrowing**: Validates member and book existence, rejects unavailable books, marks unavailable and records borrower.
- **Returning**: Validates existence, rejects if not borrowed or wrong member, restores availability and clears borrower.
- **Listing**: `list_available_books` prints only available books (or a message if none).

## Sample Behavior

```python
library = Library()
library.add_book(Book(101, "Python Basics"))
library.add_member(Member(201, "Amol"))

print(library.borrow_book(201, 101))   # Book 'Python Basics' borrowed successfully
print(library.borrow_book(202, 101))   # Member not found (or already borrowed)
print(library.return_book(201, 101))   # Book 'Python Basics' returned successfully
```

## Running the example

```bash
cd "Exercise/LIBRARY MANAGEMENT SYSTEM"
python code.py
```
