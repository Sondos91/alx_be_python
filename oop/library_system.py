# Base Class - Book
class Book:
    """Represents a generic book with title and author."""
    
    def __init__(self, title, author):
        """Initialize the Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    """Represents an e-book, a type of Book with file size."""
    
    def __init__(self, title, author, file_size):
        """Initialize the EBook with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    """Represents a printed book, a type of Book with page count."""
    
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """Return string representation of the printed book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    """Represents a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
