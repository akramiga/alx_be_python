class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)        
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books: list[Book] = []  # Initializes an empty list of books

    def add_book(self, book: Book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):  # Check if the object is an instance of Book or its subclasses
            self.books.append(book)
            print(f"'{book.title}' has been added to the library.")
        else:
            print("The object is not a valid book.")

    def list_books(self):
        """Prints details of each book in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)                