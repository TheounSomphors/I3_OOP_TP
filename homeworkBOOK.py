class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self._price = None      # protected attribute
        self.price = price      # goes through the setter for validation

    @property
    def price(self):
        """Getter: read access to the protected price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter: only allows valid (non-negative) prices."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def __str__(self):
        return f"'{self.title}' by {self.author} - ${self._price:.2f}"


class EBook(Book):
    def __init__(self, title, author, price, file_size_mb, file_format="PDF"):
        super().__init__(title, author, price)
        self.file_size_mb = file_size_mb
        self.file_format = file_format

    def __str__(self):
        return (f"{super().__str__()} "
                f"[{self.file_format}, {self.file_size_mb} MB]")


# Demonstration
book = Book("Clean Code", "Robert C. Martin", 35.50)
print(book)

book.price = 30          # valid update via setter
print(book.price)

try:
    book.price = -5      # rejected by setter
except ValueError as e:
    print("Error:", e)

ebook = EBook("Clean Code", "Robert C. Martin", 20.00, 4.2, "EPUB")
print(ebook)