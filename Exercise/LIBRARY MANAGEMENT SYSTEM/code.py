
# ==========================================
# DAY 4 - LIBRARY MANAGEMENT SYSTEM
# ==========================================

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

    # ADD BOOK
    def add_book(self, book):
        if book.book_id in self.books:
            return "Book ID already exists"

        self.books[book.book_id] = book
        return f"Book '{book.title}' added successfully"

    # ADD MEMBER
    def add_member(self, member):
        if member.member_id in self.members:
            return "Member ID already exists"

        self.members[member.member_id] = member
        return f"Member '{member.name}' added successfully"

    # BORROW BOOK
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

    # RETURN BOOK
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

    # LIST AVAILABLE BOOKS
    def list_available_books(self):
        found = False

        for book_id, book in self.books.items():
            if book.is_available:
                print(f"Book ID: {book_id}, Title: {book.title}")
                found = True

        if not found:
            print("No books are currently available")


# ==========================================
# OBJECT CREATION
# ==========================================

library = Library()

# Book objects
book1 = Book(101, "Python Basics")
book2 = Book(102, "Machine Learning")
book3 = Book(103, "Data Structures")

# Member objects
member1 = Member(201, "Amol")
member2 = Member(202, "Rahul")
member3 = Member(203, "Priya")


# ==========================================
# ADD BOOKS AND MEMBERS
# ==========================================

print("\n=== ADDING BOOKS ===")

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

print("\n=== ADDING MEMBERS ===")

print(library.add_member(member1))
print(library.add_member(member2))
print(library.add_member(member3))


# ==========================================
# TEST 1 - AVAILABLE BOOKS
# ==========================================

print("\n=== AVAILABLE BOOKS ===")
library.list_available_books()


# ==========================================
# TEST 2 - BORROW BOOK
# ==========================================

print("\n=== BORROW BOOK ===")

print(library.borrow_book(201, 101))
print(library.borrow_book(202, 102))

print("\n=== AVAILABLE BOOKS AFTER BORROWING ===")
library.list_available_books()


# ==========================================
# TEST 3 - SECOND BORROWER
# ==========================================

print("\n=== SECOND BORROWER ===")
print(library.borrow_book(203, 101))


# ==========================================
# TEST 4 - WRONG MEMBER RETURN
# ==========================================

print("\n=== WRONG MEMBER RETURN ===")
print(library.return_book(203, 101))


# ==========================================
# TEST 5 - CORRECT MEMBER RETURN
# ==========================================

print("\n=== CORRECT MEMBER RETURN ===")
print(library.return_book(201, 101))


# ==========================================
# TEST 6 - RETURN AGAIN
# ==========================================

print("\n=== RETURN AGAIN ===")
print(library.return_book(201, 101))


# ==========================================
# TEST 7 - UNKNOWN BOOK AND MEMBER
# ==========================================

print("\n=== INVALID OPERATIONS ===")

print(library.borrow_book(201, 999))
print(library.borrow_book(999, 101))
print(library.return_book(201, 999))


# ==========================================
# TEST 8 - DUPLICATE IDS
# ==========================================

print("\n=== DUPLICATE ID CHECK ===")

print(library.add_book(Book(101, "Duplicate Python")))
print(library.add_member(Member(201, "Duplicate Member")))


# ==========================================
# TEST 9 - FINAL AVAILABLE BOOKS
# ==========================================

print("\n=== FINAL AVAILABLE BOOKS ===")
library.list_available_books()


# ==========================================
# TEST 10 - FINAL OBJECT STATUS
# ==========================================

print("\n=== FINAL BOOK STATUS ===")

for book_id, book in library.books.items():
    print(
        f"ID: {book_id}, "
        f"Title: {book.title}, "
        f"Available: {book.is_available}, "
        f"Borrowed By: {book.borrowed_by}"
    )
