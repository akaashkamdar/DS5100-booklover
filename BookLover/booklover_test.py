import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        person = BookLover("Akaash Kamdar", "ak2znr@virginia.edu", "mystery")
        person.add_book("Encyclopedia Brown", 4)
        
        self.assertTrue("Encyclopedia Brown" in list(person.book_list.book_name))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        person = BookLover("Akaash Kamdar", "ak2znr@virginia.edu", "mystery")
        person.add_book("Encyclopedia Brown", 4)
        person.add_book("Encyclopedia Brown", 4)
        
        self.assertTrue(len(person.book_list[person.book_list.book_name == "Encyclopedia Brown"]) == 1)
     
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        person = BookLover("Akaash Kamdar", "ak2znr@virginia.edu", "mystery")
        person.add_book("Encyclopedia Brown", 4)
        
        self.assertTrue(person.has_read("Encyclopedia Brown"))

    def test_4_has_read(self): 
        person = BookLover("Akaash Kamdar", "ak2znr@virginia.edu", "mystery")
        person.add_book("Encyclopedia Brown", 4)
        
        self.assertFalse(person.has_read("Python Textbook"))

    def test_5_num_books_read(self): 
        person = BookLover("Akaash Kamdar", "ak2znr@virginia.edu", "mystery")
        person.add_book("Encyclopedia Brown", 4)
        person.add_book("The Kite Runner", 5)
        person.add_book("Frankenstein", 4)
        person.add_book("Picture of Dorian Gray", 4)
        person.add_book("Don Quixote", 4)
        expected_count = 5
        
        self.assertEqual(person.num_books_read(), expected_count)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        person = BookLover("Akaash Kamdar", "ak2znr@virginia.edu", "mystery")
        person.add_book("Encyclopedia Brown", 4)
        person.add_book("The Kite Runner", 5)
        person.add_book("Frankenstein", 2)
        person.add_book("Picture of Dorian Gray", 4)
        person.add_book("Don Quixote", 2)

        expected_count = 0
        
        self.assertEqual(len(person.fav_books()[person.fav_books().book_rating<= 3]), expected_count)


if __name__ == '__main__':
    
    unittest.main(verbosity=3)
