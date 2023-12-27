import sqlite3

class Modelo:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()

    #-----------------TABLAS-------------------------

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

        self.c.execute('''CREATE TABLE IF NOT EXISTS Disponibilidad 
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                           Nombre TEXT, 
                           Descripcion TEXT)''')
        self.conn.commit()
        
        self.c.execute('''CREATE TABLE IF NOT EXISTS Colaborador
                          (ID_Colaborador INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                          Nombre TEXT(128) NOT NULL,
                          Correo TEXT(128) NOT NULL,
                          Telefono TEXT DEFAULT (2256-2222) NOT NULL,
                          ID_Rol INTEGER NOT NULL,
                          ID_Turno INTEGER NOT NULL,
                          ID_Disponibilidad INTEGER NOT NULL,
                          Modalidad INTEGER DEFAULT (1) NOT NULL,
                          CONSTRAINT Colaborador_FK_3 FOREIGN KEY (ID_Rol) REFERENCES Rol(ID_Rol),
                          CONSTRAINT Colaborador_FK_4 FOREIGN KEY (ID_Turno) REFERENCES Turno(ID_Turno),
                          CONSTRAINT Colaborador_FK_5 FOREIGN KEY (ID_Disponibilidad) REFERENCES Disponibilidad(ID_Disponibilidad))''')
        self.conn.commit()

    #-----------------USUARIOS-------------------------

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

    #-----------------ROLES-------------------------

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

    #-----------------DISPONIBILIDADES-------------------------

    def agregar_disponibilidad(self, nombre, descripcion):
        self.c.execute("INSERT INTO Disponibilidad (Nombre, Descripcion) VALUES (?, ?)", (nombre, descripcion))
        self.conn.commit()

    def obtener_disponibilidades(self):
        self.c.execute("SELECT * FROM Disponibilidad")
        return self.c.fetchall()

    def eliminar_disponibilidad(self, id):
        self.c.execute("DELETE FROM Disponibilidad WHERE ID_Disponibilidad=?", (id))
        self.conn.commit()

    def actualizar_disponibilidad(self, id_disponibilidad, nombre, descripcion):
        self.c.execute("UPDATE Disponibilidad SET Nombre=?, Descripcion=? WHERE ID_Disponibilidad=?", (nombre, descripcion, id_disponibilidad))
        self.conn.commit()

    #-----------------COLABORADORES-------------------------
    
    def agregar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad):
        self.c.execute("INSERT INTO Colaborador (Nombre, Correo, Telefono, ID_Rol, ID_Turno, ID_Disponibilidad, Modalidad) VALUES(?, ?, ?, ?, ?, ?, ?)", (nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad))
        self.conn.commit()
    
    def obtener_colaboradores(self):
        self.c.execute("SELECT * FROM Colaborador")
        return self.c.fetchall()
    
    def eliminar_colaborador(self, id):
        self.c.execute("DELETE FROM Colaborador WHERE ID_Colaborador=?", (id))
        self.conn.commit()
    
    def actualizar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador):
        self.c.execute("UPDATE Colaborador SET Nombre=?, Correo=?, Telefono=?, ID_Rol=?, ID_Turno=?, ID_Disponibilidad=?, Modalidad=? WHERE ID_Colaborador=?", (nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador))
        self.conn.commit()
    
    #-----------------OTROS-------------------------

    def cerrar_conexion(self):
        self.conn.close()
