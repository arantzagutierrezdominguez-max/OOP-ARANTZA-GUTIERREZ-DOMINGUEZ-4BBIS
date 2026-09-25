class library:
    def __init__(self):
        self.users = []
        self.books = []

    # Requerimiento 1: Registrar libros
    def add_book(self, book):
        self.books.append(book)  

    # Requerimiento 2: Registrar usuarios
    def add_user(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_book_info())


    def add_users(self, user):
        self.users.append(user) #append es para agregar en el ultimo lugar
    def add_book(self, book):
        self.books.append(book)

# Requerimiento 3 y 4: Prestar un libro / no prestar si ya está prestado
    def borrow_book(self, id_book, user):
        for book in self.books:
            if book.id_book == id_book:
                if book.is_borrowed:
                    print(f"El libro '{book.title}' ya está prestado.")
                    return
                book.is_borrowed = True
                print(f"El libro '{book.title}' ha sido prestado con éxito a {user.name}.")
                return
        print("Libro no encontrado.")
    
# Requerimiento 5: Devolver un libro
    def return_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                if not book.is_borrowed:
                    print(f"El libro '{book.title}' no estaba prestado.")
                    return
                book.is_borrowed = False
                print(f"El libro '{book.title}' ha sido devuelto con éxito.")
                return
        print("Libro no encontrado.")