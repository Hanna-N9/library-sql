import unittest
from book import Book
from card import Card
from fees import Fees
from member import Member
from librarian import Librarian

class BookTest(unittest.TestCase):
    def setUp(self):
        self.book=Book('9781118531648', 'Jon', 'Duckett', '640')

    def test_getIsbn(self):
        self.assertEqual(self.book.getIsbn(), '9781118531648')

    def test_getAuthorfirstname(self):
        self.assertEqual(self.book.getAuthorfirstname(), 'Jon')

    def test_getAuthorlastname(self):
        self.assertEqual(self.book.getAuthorlastname(), 'Duckett')
    
    def test_getPages(self):
        self.assertEqual(self.book.getPages(), '640')

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card=Card('1000022230101', 'The Seattle Public Library', '5/31/20', '5/31/22')
    
    def test_getCardnumber(self):
        self.assertEqual(self.card.getCardnumber(), '1000022230101')

    def test_getTitle(self):
        self.assertEqual(self.card.getTitle(), 'The Seattle Public Library')

class FeesTest(self):
    def setUp(self):
        sefl.fees=Fees('20', '.25')

    def test_getAmount(self):
        self.assertEqual(self.fees.getAmount(), '20')
    
    def test_getWeeklyinterest(self):
        self.assertEqual(self.fees.getWeeklyinterest(), '.25')

class MemberTest(self):
    def setUp(self):
        member=Member('1000022230101', 'Library patron', 'username@gmail.com', 'A member')

    def test_getLibrarynumber(self):
        self.assertEqual(self.member.getLibrarynumber(), '1000022230101')
    
    def test_getRecord(self):
        self.assertEqual(self.member.getRecord(), 'Library patron')

class LibrarianTest(self):
    def setUp(self):
        librarian=Librarian('Smith', 'Amy', 'username@email.com', 'Assistant Librarian')
    
    def test_getLastName(self):
        self.assertEqual(self.librarian.getLastName(), 'Smith')

    def test_getEmail(self):
        self.assertEqual(self.librarian.getEmail(), 'username@email.com')

    def test_getPosition(self):
        self.assertEqual(self.librarian.getPosition(), 'Assistant Librarian')
        
        
        