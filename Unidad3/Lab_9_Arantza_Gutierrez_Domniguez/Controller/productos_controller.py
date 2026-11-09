from tkinter import filedialog, messagebox
from exportadores import ExportadorCSV, ExportadorTXT, ExportadorJSON, ExportadorPDF

class ProductosController:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def generar_reporte(self):
        # 1. Obtener el formato seleccionado en la Vista
        formato = self.vista.combo_formato.get()
        
        # 2. Obtener los productos desde el Modelo (Corregido a obtener_todos)
        datos_productos = self.modelo.obtener_todos()
        
        if not datos_productos:
            messagebox.showwarning("Aviso", "No hay productos para exportar.")
            return

        # 3. Cuadro de diálogo para elegir la ruta y nombre del archivo
        extensiones = {
            "CSV": "*.csv",
            "TXT": "*.txt",
            "JSON": "*.json",
            "PDF": "*.pdf"
        }
        
        ruta_archivo = filedialog.asksaveasfilename(
            defaultextension=f".{formato.lower()}",
            filetypes=[(f"Archivo {formato}", extensiones.get(formato, "*.*"))]
        )
        
        if not ruta_archivo:
            return

        # 4. Aplicar Polimorfismo según la opción elegida
        exportador = None
        if formato == "CSV":
            exportador = ExportadorCSV()
        elif formato == "TXT":
            exportador = ExportadorTXT()
        elif formato == "JSON":
            exportador = ExportadorJSON()
        elif formato == "PDF":
            exportador = ExportadorPDF()

        # 5. Llamada genérica al método .exportar()
        if exportador:
            exportador.exportar(datos_productos, ruta_archivo)
            messagebox.showinfo("Éxito", f"Reporte guardado correctamente en:\n{ruta_archivo}")