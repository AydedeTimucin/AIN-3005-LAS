from datetime import datetime, timedelta
from models.book import Book

# Transaction class
class Loan:
    def __init__(self, user, book: Book, loan_period: int):
        self.user = user
        self.book = book
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=loan_period)
        self.is_active = True

    def __str__(self):
        return (f"Loan of book '{self.book.title}' to {self.user.name} "
                f"from {self.issue_date.strftime('%Y-%m-%d')} to {self.due_date.strftime('%Y-%m-%d')}")


    def extend_loan(self, extension_days: int) -> bool:
        if self.is_active and datetime.now() <= self.due_date:
            self.due_date += timedelta(days=extension_days)
            return True
        return False

    def return_loan(self):
        today = datetime.now()
        self.is_active = False
        self.book.return_book()
        if today > self.due_date:
            return f"Overdue book fine is: {self.calculate_fine()}."  # Calculate fine if overdue
        else:
            return f"Your return has been processed. Thank you!"

    def calculate_fine(self) -> int:
        if self.returned:
            return 0  # No fine if the book is already returned

        today = datetime.now()
        if today <= self.due_date:
            return 0  # No fine if the book is not overdue

        # Calculate the number of full weeks overdue
        overdue_days = (today - self.due_date).days
        full_weeks_overdue = overdue_days // 7

        # For the first week, the fine is 10 Turkish Lira
        fine = 10

        # For subsequent weeks, the fine is 20 Turkish Lira per week
        if full_weeks_overdue > 0:
            fine += (full_weeks_overdue * 20)

        return fine
