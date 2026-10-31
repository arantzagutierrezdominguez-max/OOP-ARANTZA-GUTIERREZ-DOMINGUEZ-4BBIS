import tkinter as tk
from Models.user_model import UserModel
from Views.login_view import LoginView
from Controller.auth_controller import Authentication

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = Authentication(self.modelo, self.vista)

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.start()
    