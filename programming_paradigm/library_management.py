class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False
    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
            #return f"The book '{self.title}' has been checked out."
        return False
        #return f"The book '{self.title}' is already checked out."

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    def is_checked_out(self):
        return self.__is_checked_out     
class Library:
    def __init__(self):
        self._books = [] 
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
        #     return f"Book '{book.title}' by {book.author} added to the library."
        # else:
        #     raise ValueError("Only instances of Book can be added to the library.")
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"You have checked out '{title}'."
        return f"Sorry, '{title}' is not available."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"You have returned '{title}'."
        return f"Sorry, '{title}' was not checked out."

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            return [f"{book.title} by {book.author}" for book in available_books]
        return ["No books are currently available."]
