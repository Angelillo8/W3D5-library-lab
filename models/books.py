from models.book import Book

book1 = Book("Ulysses", "James Joyce", "Fiction")
book2 = Book("Kidnapped", "Robert Louis Stevenson", "Adventure")
book3 = Book("The Aleph and Other Stories", "Jorge Luis Borges", "Fantasy")

books = [book1, book2, book3]

def get_book(book_title):
    book_to_get = None
    for book in books:
        if book.title == book_title:
            book_to_get = book
            break

    return book_to_get

def add_new_book(book):
    books.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)

# def delete_book(book_title):
#     for book in books:
#         if book.title == book_title:
#             books.remove(book)
#             break

