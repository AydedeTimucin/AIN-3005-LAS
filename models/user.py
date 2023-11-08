from models.book import Book, Periodical, Textbook
from models.loan import Loan
from typing import List, Optional

# Base User class
class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.loans: List[Loan] = []

    def notify(self, message: str):
        print(f"Sending email to {self.email}: {message}")

    def get_max_loan_duration(self) -> int:
        return 15  # Default max duration for students and staff

    def borrow_book(self, book: Book, loan_period: int) -> Optional[Loan]:
        if loan_period < 1 or loan_period > self.loan_duration:
            raise ValueError(f"Loan period must be between 1 and {self.loan_duration} days.")
        
        if isinstance(book, Periodical):
            raise ValueError("Periodicals cannot be borrowed.")
        
        if isinstance(book, Textbook) and not isinstance(self, Faculty):
            raise ValueError("Textbooks can only be borrowed by faculty members.")

        if len(self.loans) < self.get_book_limit() and not book.is_borrowed:
            loan = Loan(self, book, loan_period)
            self.loans.append(loan)
            book.borrow()
            return loan
        return None

    def get_book_limit(self) -> int:
        # Default book limit, overriden by child classes
        return 3

# Derived classes for different types of users
class Faculty(User):
    def __init__(self, user_id: str, name: str, email: str, department: str):
        super().__init__(user_id, name, email)
        self.department = department
        self.book_limit = 5
        self.loan_duration = 30  # 30 days

class Student(User):
    def __init__(self, user_id: str, name: str, email: str, major: str):
        super().__init__(user_id, name, email)
        self.major = major
        self.book_limit = 3
        self.loan_duration = 15  # 15 days

class Staff(User):
    def __init__(self, user_id: str, name: str, email: str, position: str):
        super().__init__(user_id, name, email)
        self.position = position
        self.book_limit = 3
        self.loan_duration = 15  # 15 days

class Alumni(User):
    def __init__(self, user_id: str, name: str, email: str, subscription: False):
        super().__init__(user_id, name, email)
        self.book_limit = 3
        self.loan_duration = 15  # 15 days
        self.subscription = subscription