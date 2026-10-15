from Controller.database_connection import Database_connection

class User:
    def __init__(self, username, passw):
        self.username = username
        self.passw = passw
        self.db = Database_connection()

    def auth(self):
        # Agregamos "login_system_db." antes de users para que Python sepa exactamente dónde buscar
        query = """
            SELECT id_user, username, nombre 
            FROM login_system_db.users 
            WHERE username = %s AND passw = %s
        """
        resultado = self.db.ejecutar_consulta(query, (self.username, self.passw))
        return resultado