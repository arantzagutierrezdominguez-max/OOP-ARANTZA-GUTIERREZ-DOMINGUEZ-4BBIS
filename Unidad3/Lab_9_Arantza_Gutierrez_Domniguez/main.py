import tkinter as tk
# Como login_view está dentro de la carpeta Views, se importa así:
from Views.login_view import LoginVentana 

def main():
    # 1. Crear la ventana principal de Tkinter
    root = tk.Tk()
    
    # 2. Instanciar la interfaz de inicio de sesión
    app = LoginVentana(root)
    
    # 3. Iniciar el bucle principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
