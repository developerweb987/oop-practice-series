class Book:
    # Class variable to track the total number of books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Each time a book is created, increment the book count
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        # Increment the total book count by 1
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        # Display the total number of books
        print(f"Total books: {cls.total_books}")

# Example usage
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Display the total number of books
Book.display_total_books()
