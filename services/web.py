from models.card import Card
from models.book import Book
from models.loan import Loan
from typing import Optional

class Web:
    def borrow_book(self, card: Card, book: Book, pin_code: str, loan_period: int) -> Optional[Loan]:
        # Verify the PIN code
        if not card.verify_pin(pin_code):
            raise ValueError("Invalid PIN code.")
        
        # Get the user from the card
        user = card.owner

        # Attempt to borrow the book
        try:
            loan = user.borrow_book(book, loan_period)
            if loan:
                return loan

            else:
                print(f"{book.title} is not available for borrowing.")
                return None

        except ValueError as error:
            print(error)
            return None

