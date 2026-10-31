from Controller.database_connection import Database_connection

class UserModel:
    def __init__(self):
        self.db = Database_connection()
        self.crear_tabla_si_no_existe()

    def crear_tabla_si_no_existe(self):
        conexion = self.db.obtener_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL
                    );
                """)
                conexion.commit()
                cursor.close()
                conexion.close()
            except Exception as e:
                print(f"Error al crear la tabla automáticamente: {e}")

    def registrar_usuario(self, nombre, email, password):
        conexion = self.db.obtener_conexion()
        if not conexion:
            return False, "No se pudo conectar a la base de datos."
        
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO users (nombre, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, email, password))
            conexion.commit()
            cursor.close()
            conexion.close()
            return True, "¡Usuario registrado con éxito!"
        except Exception as e:
            print(f"Detalle del error en BD: {e}")
            return False, "El correo ya está registrado o hubo un error."

    def verificar_usuario(self, email, password):
        conexion = self.db.obtener_conexion()
        if not conexion:
            return False
        
        try:
            cursor = conexion.cursor()
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            usuario = cursor.fetchone()
            cursor.close()
            conexion.close()
            return usuario is not None
        except Exception as e:
            print(f"Detalle del error al iniciar sesión: {e}")
            return False