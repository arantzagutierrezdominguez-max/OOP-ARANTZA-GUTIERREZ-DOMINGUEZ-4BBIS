import tkinter as tk
from tkinter import messagebox
from Models.login_model import User 
from Views.home_view import DashboardVentana 
from PIL import Image, ImageTk

class LoginVentana:
    """Ventana de inicio de sesión."""

    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("350x450")  # Espacio suficiente para el logo y los campos
        self.root.resizable(False, False)
        
        # Color de fondo aesthetic (morado pastel / lavanda suave)
        self.root.configure(bg="#EAD9F5")

        self._crear_interfaz()

    def crear_logo(self):
        try:
            ruta_imagen = r"C:\Users\Administrator\Documents\UTD 4B\PRACTICE\Lab_7_Gutierrez_Dominguez_Arantza\assets\Gemini_Generated_Image_3xti983xti983xti.jpg"
            imagen_pil = Image.open(ruta_imagen)
            imagen_pil = imagen_pil.resize((80, 80), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(imagen_pil)
            
            # El fondo del label del logo también lleva el color lavanda para que no desentone
            lbl_logo = tk.Label(self.root, image=self.logo_img, bg="#EAD9F5")
            lbl_logo.pack(pady=(15, 5))
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")
            lbl_logo = tk.Label(self.root, text="[ LOGO ]", font=("Helvetica", 12, "italic"), fg="gray", bg="#EAD9F5")
            lbl_logo.pack(pady=10)

    def _crear_interfaz(self):
        # 1. Cargar el logo en la parte superior
        self.crear_logo()

        # 2. Título con tono morado oscuro elegante
        lbl_titulo = tk.Label(
            self.root, 
            text="Iniciar Sesión", 
            font=("Helvetica", 16, "bold"),
            bg="#EAD9F5",
            fg="#4A2E65"
        )
        lbl_titulo.pack(pady=10)

        # 3. Campo Usuario
        lbl_usuario = tk.Label(
            self.root, 
            text="Usuario:", 
            font=("Helvetica", 10, "bold"),
            bg="#EAD9F5",
            fg="#4A2E65"
        )
        lbl_usuario.pack(anchor="w", padx=30, pady=(5, 2))
        
        self.entry_usuario = tk.Entry(
            self.root, 
            font=("Helvetica", 11),
            bg="#F9F6FC",
            fg="#333333",
            relief="flat",
            highlightbackground="#B39DDB",
            highlightcolor="#6C3483",
            highlightthickness=1
        )
        self.entry_usuario.pack(fill="x", padx=30, ipady=3)

        # 4. Campo Contraseña
        lbl_pass = tk.Label(
            self.root, 
            text="Contraseña:", 
            font=("Helvetica", 10, "bold"),
            bg="#EAD9F5",
            fg="#4A2E65"
        )
        lbl_pass.pack(anchor="w", padx=30, pady=(15, 2))
        
        self.entry_pass = tk.Entry(
            self.root, 
            font=("Helvetica", 11), 
            show="*",
            bg="#F9F6FC",
            fg="#333333",
            relief="flat",
            highlightbackground="#B39DDB",
            highlightcolor="#6C3483",
            highlightthickness=1
        )
        self.entry_pass.pack(fill="x", padx=30, ipady=3)

        # 5. Botón Ingresar (Morado aesthetic / uva)
        btn_ingresar = tk.Button(
            self.root, 
            text="Entrar", 
            font=("Helvetica", 11, "bold"),
            bg="#6C3483", 
            fg="white", 
            activebackground="#512E5F",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self._validar_login
        )
        btn_ingresar.pack(fill="x", padx=30, pady=25, ipady=4)

    def _validar_login(self):
        usuario_texto = self.entry_usuario.get().strip()
        pass_texto = self.entry_pass.get().strip()

        if not usuario_texto or not pass_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor ingresa usuario y contraseña.")
            return

        usuario_obj = User(usuario_texto, pass_texto)
        datos_usuario = usuario_obj.auth()

        if datos_usuario and len(datos_usuario) > 0:
            nombre = datos_usuario[0]['nombre']
            messagebox.showinfo("Bienvenido", f"¡Hola {nombre}! Acceso concedido.")
            self._abrir_dashboard(nombre)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")

    def _abrir_dashboard(self, nombre_completo):
        self.root.destroy()
        root_dashboard = tk.Tk()
        DashboardVentana(root_dashboard, nombre_completo)
        root_dashboard.mainloop()