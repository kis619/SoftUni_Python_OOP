class User:

    def __init__(self, uid: int, u_name: str):
        self.user_id = uid
        self.username = u_name
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            if not library.rented_books.get(self.username):
                library.rented_books[self.username] = dict()
            library.rented_books[self.username][book_name] = days_to_return
            library.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        days = [book.get(book_name) for book in list(library.rented_books.values()) if book.get(book_name)][0]
        # for username, rented_books in library.rented_books.items():
        #     for book, days_to_return in rented_books.items():
        #         if book == book_name:
        #             return f"The book \"{book_name}\" is already rented and will be available in " \
        #                    f"{days_to_return} days!"

        return f"The book \"{book_name}\" is already rented and will be available in " \
               f"{days} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name in self.books:
            self.books.remove(book_name)
            del library.rented_books[self.username][book_name]

            if not library.books_available[author]:
                library.books_available[author] = []
            library.books_available[author].append(book_name)

        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
