import sqlite3

class Modelo:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Usuario 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           Username TEXT, 
                           Password TEXT)''')
        self.conn.commit()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Rol 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           Nombre TEXT, 
                           Descripcion TEXT)''')
        self.conn.commit()

    def agregar_usuario(self, username, password):
        self.c.execute("INSERT INTO Usuario (Username, Password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def obtener_usuarios(self):
        self.c.execute("SELECT * FROM Usuario")
        return self.c.fetchall()

    def eliminar_usuario(self, id):
        self.c.execute("DELETE FROM Usuario WHERE ID_Usuario=?", (id))
        self.conn.commit()

    def actualizar_usuario(self, id_usuario, username, password):
        self.c.execute("UPDATE Usuario SET Username=?, Password=? WHERE ID_Usuario=?", (username, password, id_usuario))
        self.conn.commit()

    def agregar_rol(self, nombre, descripcion):
        self.c.execute("INSERT INTO Rol (Nombre, Descripcion) VALUES (?, ?)", (nombre, descripcion))
        self.conn.commit()

    def obtener_roles(self):
        self.c.execute("SELECT * FROM Rol")
        return self.c.fetchall()

    def eliminar_rol(self, id):
        self.c.execute("DELETE FROM Rol WHERE ID_Rol=?", (id))
        self.conn.commit()

    def actualizar_rol(self, id_rol, nombre, descripcion):
        self.c.execute("UPDATE Rol SET Nombre=?, Descripcion=? WHERE ID_Rol=?", (nombre, descripcion, id_rol))
        self.conn.commit()

    def cerrar_conexion(self):
        self.conn.close()
