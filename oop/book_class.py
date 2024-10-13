class Book:
    """A class to represent a book with title, author, and year."""

    def __init__(self, title, author, year):
        """Constructor to initialize the Book object."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation method (used by print())."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation method (used by repr())."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
