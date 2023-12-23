import sqlite3

class Modelo:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           nombre TEXT, 
                           edad INTEGER)''')
        self.conn.commit()

    def agregar_usuario(self, nombre, edad):
        self.c.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
        self.conn.commit()

    def obtener_usuarios(self):
        self.c.execute("SELECT * FROM usuarios")
        return self.c.fetchall()

    def eliminar_usuario(self, id):
        self.c.execute("DELETE FROM usuarios WHERE id=?", (id))
        self.conn.commit()

    def cerrar_conexion(self):
        self.conn.close()
