import csv
import json
from fpdf import FPDF

class Exporter:
    def export(self, data, file_path):
        """Método base que debe ser sobrescrito por las clases hijas"""
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

class ExportadorTXT(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n")
            for producto in data:
                # Usamos claves de diccionario porque usamos RealDictCursor
                file.write(f"ID: {producto['id']} | Nombre: {producto['nombre']} | Precio: ${producto['precio']}\n")
        print(f"Archivo TXT generado en: {file_path}")

class ExportadorCSV(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nombre", "Precio", "Stock"])
            for producto in data:
                writer.writerow([producto['id'], producto['nombre'], producto['precio'], producto['stock']])
        print(f"Archivo CSV generado en: {file_path}")

class ExportadorJSON(Exporter):
    def export(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Archivo JSON generado en: {file_path}")

class ExportadorPDF(Exporter):
    def export(self, data, file_path):
        pdf = FPDF()
        pdf.add_page()
        
        # Título del reporte
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')
        pdf.ln(10)
        
        # Cuerpo del reporte
        pdf.set_font("Arial", size=12)
        for producto in data:
            texto_linea = f"ID: {producto['id']} | Producto: {producto['nombre']} - Precio: ${producto['precio']}"
            pdf.cell(200, 10, txt=texto_linea, ln=True)
            
        pdf.output(file_path)
        print(f"Archivo PDF generado en: {file_path}")