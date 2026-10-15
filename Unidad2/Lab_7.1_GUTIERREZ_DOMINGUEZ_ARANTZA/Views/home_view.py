import tkinter as tk
from tkinter import ttk, messagebox
from Models.products_model import Producto

class DashboardVentana:
    """Ventana principal con pestañas para Inicio e Inventario de Productos."""

    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title("Panel Principal - Sistema")
        self.root.geometry("850x520")
        self.root.config(bg="#F4F1F8")

        # 1. Encabezado de bienvenida superior
        lbl_bienvenida = tk.Label(
            self.root,
            text=f"Bienvenido/a, {nombre_usuario}",
            font=("Helvetica", 14, "bold"),
            bg="#F4F1F8",
            fg="#4A2E65"
        )
        lbl_bienvenida.pack(pady=10)

        # 2. Creación del sistema de pestañas (Notebook)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=10)

        # --- Pestaña 1: Inicio ---
        self.tab_inicio = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_inicio, text="Inicio")

        lbl_info = tk.Label(
            self.tab_inicio,
            text="Utiliza las pestañas superiores para navegar por el sistema.",
            font=("Helvetica", 12),
            fg="#555555"
        )
        lbl_info.pack(expand=True)

        # --- Pestaña 2: Inventario de Productos ---
        self.tab_inventario = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_inventario, text="Inventario de Productos")

        self.crear_seccion_inventario()

    def crear_seccion_inventario(self):
        # Frame izquierdo: Formulario para registrar productos
        frame_form = tk.LabelFrame(
            self.tab_inventario, 
            text="Registrar Producto", 
            font=("Helvetica", 10, "bold"), 
            padx=10, 
            pady=10
        )
        frame_form.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(frame_form, text="Nombre:", font=("Helvetica", 10)).pack(anchor="w", pady=5)
        self.entry_nombre = tk.Entry(frame_form, font=("Helvetica", 10), width=22)
        self.entry_nombre.pack(pady=5)

        tk.Label(frame_form, text="Precio ($):", font=("Helvetica", 10)).pack(anchor="w", pady=5)
        self.entry_precio = tk.Entry(frame_form, font=("Helvetica", 10), width=22)
        self.entry_precio.pack(pady=5)

        tk.Label(frame_form, text="Stock:", font=("Helvetica", 10)).pack(anchor="w", pady=5)
        self.entry_stock = tk.Entry(frame_form, font=("Helvetica", 10), width=22)
        self.entry_stock.pack(pady=5)

        btn_guardar = tk.Button(
            frame_form, 
            text="Guardar Producto", 
            bg="#6C3483", 
            fg="white", 
            font=("Helvetica", 10, "bold"),
            command=self.guardar_producto,
            cursor="hand2"
        )
        btn_guardar.pack(fill="x", pady=15)

        # Frame derecho: Tabla (Treeview) para mostrar los productos de la BD
        frame_tabla = tk.Frame(self.tab_inventario)
        frame_tabla.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        columns = ("id", "nombre", "precio", "stock")
        self.tabla = ttk.Treeview(frame_tabla, columns=columns, show="headings")

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio ($)")
        self.tabla.heading("stock", text="Stock")

        self.tabla.column("id", width=40, anchor="center")
        self.tabla.column("nombre", width=180, anchor="w")
        self.tabla.column("precio", width=90, anchor="center")
        self.tabla.column("stock", width=70, anchor="center")

        # Barra de desplazamiento para la tabla
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Cargar los datos desde PostgreSQL al iniciar la vista
        self.cargar_productos()

    def cargar_productos(self):
        # Limpiar registros actuales de la tabla en pantalla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Llamar al método del modelo que ya creaste (products_model.py)
        prod_model = Producto()
        productos = prod_model.obtener_todos()

        if productos:
            for p in productos:
                # Como usas RealDictCursor, puedes acceder por las llaves del diccionario[cite: 5, 8]
                self.tabla.insert("", "end", values=(p['id'], p['nombre'], p['precio'], p['stock']))

    def guardar_producto(self):
        nombre = self.entry_nombre.get().strip()
        precio = self.entry_precio.get().strip()
        stock = self.entry_stock.get().strip()

        if not nombre or not precio or not stock:
            messagebox.showerror("Error", "Por favor completa todos los campos.")
            return

        try:
            precio_float = float(precio)
            stock_int = int(stock)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número y el stock entero.")
            return

        # Instanciar el modelo con los datos y guardar
        nuevo_prod = Producto(nombre=nombre, precio=precio_float, stock=stock_int)
        if nuevo_prod.guardar():
            messagebox.showinfo("Éxito", "Producto guardado correctamente.")
            self.entry_nombre.delete(0, 'end')
            self.entry_precio.delete(0, 'end')
            self.entry_stock.delete(0, 'end')
            self.cargar_productos()  # Recargar la tabla automáticamente
        else:
            messagebox.showerror("Error", "No se pudo guardar el producto en la base de datos.")