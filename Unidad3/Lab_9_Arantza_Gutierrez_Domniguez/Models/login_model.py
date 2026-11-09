from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw
        self.db = Database_connection()

    def auth(self):
        # Buscamos directamente por el nombre y la contraseña en tu tabla actual
        query = """
            SELECT id, nombre, email 
            FROM users 
            WHERE nombre = %s AND password = %s
        """
        resultado = self.db.ejecutar_consulta(query, (self.username, self.password))
        return resultado