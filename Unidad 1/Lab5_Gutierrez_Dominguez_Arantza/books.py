class book:
    def __init__(self, id_book, title, author, editorial):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.editorial = editorial
        self.is_borrowed = False  # Estado del libro (no prestado por defecto)

    def show_book_info(self):
        status = "Prestado" if self.is_borrowed else "Disponible"
        return f"{self.id_book} - {self.title} - {self.author} [{status}]"
