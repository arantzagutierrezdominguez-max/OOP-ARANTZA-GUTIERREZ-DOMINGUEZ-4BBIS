from datetime import datetime

class User:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.posts = []
        self.sent_messages = []

    def login(self):
        print(f"El usuario {self.name} ha iniciado sesión.")

    def sign_up(self):
        print(f"El usuario {self.name} se ha registrado.")

    def create_post(self, post_type: str, description: str) -> "Post":
        new_post = Post(author=self, post_type=post_type, description=description)
        self.posts.append(new_post)
        print(f"{self.name} creó una nueva publicación: '{description}'")
        return new_post

    def send_message(self, receiver: "User", text: str) -> "DirectMessage":
        message = DirectMessage(sender=self, receiver=receiver, text=text)
        self.sent_messages.append(message)
        print(f"Mensaje enviado de {self.name} a {receiver.name}: '{text}'")
        return message


class Post:
    def __init__(self, author: User, post_type: str, description: str):
        self.author = author
        self.type = post_type  # 'photo', 'video', etc.
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.comments = []
        self.likes = 0

    def add_comment(self, user: User, text: str) -> "Comment":
        comment = Comment(author=user, text=text, post=self)
        self.comments.append(comment)
        print(f"{user.name} comentó en el post de {self.author.name}: '{text}'")
        return comment

    def delete(self):
        print(f"La publicación '{self.description}' ha sido eliminada.")


class Comment:
    def __init__(self, author: User, text: str, post: Post):
        self.author = author
        self.text = text
        self.post = post
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.likes = 0

    def delete(self):
        print(f"El comentario de {self.author.name} ha sido eliminado.")


class DirectMessage:
    def __init__(self, sender: User, receiver: User, text: str):
        self.sender = sender
        self.receiver = receiver
        self.text = text
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def edit(self, new_text: str):
        self.text = new_text
        print("El mensaje ha sido actualizado.")


# ---------------------------------------------------------
# EJEMPLO DE USO PRÁCTICO
# ---------------------------------------------------------

# 1. Crear usuarios
user1 = User("Dulce", "dulce@gmail.com", "618 1234567")
user2 = User("Arantza", "arantza@gmail.com", "618 7654321")

# 2. Iniciar sesión
user1.login()

# 3. Dulce crea un post
post1 = user1.create_post(post_type="photo", description="Cena de Navidad")

# 4. Arantza comenta el post de Dulce
post1.add_comment(user=user2, text="¡Qué rica cena! Feliz Navidad.")

# 5. Dulce le envía un mensaje privado a Arantza
user1.send_message(receiver=user2, text="¡Hola Arantza! ¿Cómo estás?")