from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.password = passw
        # Anotación de tipo para habilitar el autocompletado en VS Code
        self.db: Database_connection = Database_connection()

    def auth(self):
        query = """
            SELECT id_user, username, nombre 
            FROM users 
            WHERE username = %s AND passw = %s
        """
        # Ahora al poner "self.db." te aparecerá "ejecutar_consulta"
        resultado = self.db.ejecutar_consulta(query, (self.username, self.password))
        return resultado

