from models.book import Book, Periodical, StandardBook, Textbook
from models.user import User, Staff, Student, Faculty
from models.card import Card
from services.kiosk import Kiosk
from services.web import Web


faculty_member = Faculty("f001", "Dr. Smith", "smith@example.edu", "INE")
standard_book = Textbook("987654321", "Example Title", "Example Author", "nov7")
card1 = Card(1234, faculty_member)
kiosk1 = Kiosk()
# Simulate borrowing at a kiosk
kiosk_result = kiosk1.borrow_book(card1, standard_book, 1234, 15)
print(kiosk_result)
print(kiosk_result.return_loan())

books = [Book("123456789", "Example Title", "ben"), Book("987654321", "Another Title", "sen")]
user = User("23214aw", "timu", "user@example.com")

# Search for a book
search_query = "example"
search_results = [book for book in books if book.search(search_query)]
if search_results:
    # Reserve the first found book
    search_results[0].reserve(user)

# Simulate the passing of time and check reservation expiries
for book in books:
    book.check_reservation_expiry()
