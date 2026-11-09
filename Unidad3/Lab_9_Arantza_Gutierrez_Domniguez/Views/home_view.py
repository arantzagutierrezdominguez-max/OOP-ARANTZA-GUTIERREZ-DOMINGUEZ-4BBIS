from tkinter import ttk, messagebox
import tkinter as tk
from Models.products_model import Producto
from Controller.productos_controller import ProductosController

class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.root.title(f"Dashboard - Bienvenido {nombre_usuario}")
        self.root.geometry("700x500")

        # 1. Inicializar Modelo y conectar el Controlador
        self.modelo = Producto()
        self.controlador = ProductosController(self, self.modelo)

        # 2. Panel superior de Exportación (Laboratorio 9)
        frame_export = ttk.LabelFrame(self.root, text="Exportar Reportes")
        frame_export.pack(fill="x", padx=10, pady=10)

        self.combo_formato = ttk.Combobox(frame_export, values=["CSV", "TXT", "JSON", "PDF"], state="readonly")
        self.combo_formato.set("PDF")
        self.combo_formato.pack(side="left", padx=10, pady=5)

        # Se vincula directamente al método generar_reporte del controlador
        btn_exportar = ttk.Button(frame_export, text="Exportar Reporte", command=self.controlador.generar_reporte)
        btn_exportar.pack(side="left", padx=10, pady=5)

        # 3. Panel de la Tabla / Registro de Productos (Laboratorio 7)
        frame_tabla = ttk.LabelFrame(self.root, text="Inventario de Productos")
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.tabla = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Stock", text="Stock")
        self.tabla.pack(fill="both", expand=True, padx=5, pady=5)

        # Cargar los registros en la tabla al abrir la ventana
        self.cargar_productos_tabla()

    def cargar_productos_tabla(self):
        """Llena la tabla con los registros actuales de la base de datos"""
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        productos = self.modelo.obtener_todos()
        if productos:
            for p in productos:
                self.tabla.insert("", "end", values=(p['id'], p['nombre'], p['precio'], p['stock']))