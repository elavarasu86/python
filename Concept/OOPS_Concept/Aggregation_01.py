# Aggregation = Represents a relationship where one object (the whole)
#                           Contains references to one or more INDEPENDENT objects (the parts)

# Library class is independent class but it hold Book class.
# Library class has reference to Book class.
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def print_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

# Book class is independent class.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("Madurai Central Library")

book1 = Book("Ponniyin Selvan", "Kalki")
book2 = Book("Sivagamiyin Sapatham", "Kalki")
book3 = Book("Kadal Pura", "Sandilyan")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

print(library.print_books())


