import psycopg2
from Controller.config import DB_CONFIG

class Database_connection:
    def __init__(self):
        self.config = DB_CONFIG.copy()

    def obtener_conexion(self):
        try:
            conexion = psycopg2.connect(**self.config)
            return conexion
        except Exception as e:
            print(f"Error al conectar con PostgreSQL: {e}")
            return None