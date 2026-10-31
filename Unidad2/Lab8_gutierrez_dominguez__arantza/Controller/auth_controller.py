from Models.user_model import UserModel
from Views.register_view import RegisterView

class Authentication:
    def __init__(self, model, login_view):
        self.model = model
        self.login_view = login_view
        
        # Conectar los botones de la vista de login
        self.login_view.btn_login.config(command=self.intentar_login)
        self.login_view.btn_register.config(command=self.abrir_registro)

    def intentar_login(self):
        email, password = self.login_view.obtener_datos()
        
        if not email or not password:
            self.login_view.mostrar_mensaje("Error", "Por favor completa todos los campos", "error")
            return

        exito = self.model.verificar_usuario(email, password)
        if exito:
            self.login_view.mostrar_mensaje("Éxito", f"¡Bienvenido, {email}!")
            self.login_view.limpiar_campos()
        else:
            self.login_view.mostrar_mensaje("Error", "Correo o contraseña incorrectos", "error")

    def abrir_registro(self):
        self.register_window = RegisterView(self.login_view.root)
        # Conectar el botón de guardar de la ventana de registro
        self.register_window.btn_guardar.config(command=self.procesar_registro)

    def procesar_registro(self):
        nombre, email, password, confirmar = self.register_window.obtener_datos()

        if not nombre or not email or not password or not confirmar:
            self.register_window.mostrar_mensaje("Error", "Todos los campos son obligatorios", "error")
            return

        if password != confirmar:
            self.register_window.mostrar_mensaje("Error", "Las contraseñas no coinciden", "error")
            return

        try:
            exito, mensaje = self.model.registrar_usuario(nombre, email, password)
            if exito:
                self.register_window.mostrar_mensaje("Éxito", mensaje)
                self.register_window.cerrar()
            else:
                self.register_window.mostrar_mensaje("Error", mensaje, "error")
        except Exception as e:
            print(f"Error detallado en el controlador: {e}")
            self.register_window.mostrar_mensaje("Error", "No fue posible registrar el usuario. Revisa la terminal.", "error")