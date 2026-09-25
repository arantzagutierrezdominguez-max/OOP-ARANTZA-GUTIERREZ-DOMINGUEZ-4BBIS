from books import book
from users import user
from library import library

# Instancias de prueba
book1 = book("001", "OOP Fundamentals", "John L", "BBC")
book2 = book("002", "Python for dummies", "Stef Maruzh", "For dummies")
user1 = user("001", "Arazntza Gutierrez", "1234")


library=library()

library.add_book(book1)
library.add_book(book2)
library.add_user(user1)

print("--- Libros iniciales ---")
library.show_books()

# 3. Prestar un libro a un usuario
print("\n--- Prestando libro 001 ---")
library.borrow_book("001", user1)

# 4. Intentar prestar el mismo libro otra vez (debe rechazarlo)
print("\n--- Intentando prestar libro 001 nuevamente ---")
library.borrow_book("001", user1)

# Ver el estado actualizado
print("\n--- Estado actual de libros ---")
library.show_books()

# 5. Devolver un libro
print("\n--- Devolviendo libro 001 ---")
library.return_book("001")

print("\n--- Estado final de libros ---")
library.show_books()

#Requeriments
#1.The system must allow register books
#2.The system must allow register users.
#3. The system must allow book to be borrowed by a user.
#4. A book that has already been borrowed cannot be borrowed again
#5. The system must allow a book to be return


