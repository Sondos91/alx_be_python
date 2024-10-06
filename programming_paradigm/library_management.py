# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title, author, and checked-out status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing the library, which manages a collection of books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store book instances
    
    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book from the library by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                    return
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")
    
    def return_book(self, title):
        """Return a book to the library by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {title}")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in the library.")
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

