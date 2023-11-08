from datetime import datetime, timedelta

# Base Book class
class Book:
    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.reserved_by = None
        self.reservation_expires = None

    def search(self, query: str) -> bool:
        return query.lower() in self.title.lower()

    def reserve(self, user):
        if not self.is_borrowed and self.reserved_by is None:
            self.reserved_by = user
            self.reservation_expires = datetime.now() + timedelta(days=2)
            user.notify(f"You have reserved the book '{self.title}'. Please pick it up within 2 days.")
        else:
            raise Exception(f"The book '{self.title}' is not available for reservation.")

    def check_reservation_expiry(self):
        if self.reserved_by and datetime.now() > self.reservation_expires:
            self.reserved_by.notify(f"Your reservation for '{self.title}' has been cancelled.")
            self.reserved_by = None
            self.reservation_expires = None

    def borrow(self) -> bool:
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

# Derived classes for different types of books
class Periodical(Book):
    def __init__(self, isbn: str, title: str, author: str, issue: str):
        super().__init__(isbn, title, author)
        self.issue = issue

class Textbook(Book):
    def __init__(self, isbn: str, title: str, author: str, subject: str):
        super().__init__(isbn, title, author)
        self.subject = subject

class StandardBook(Book):
    def __init__(self, isbn: str, title: str, author: str):
        super().__init__(isbn, title, author)