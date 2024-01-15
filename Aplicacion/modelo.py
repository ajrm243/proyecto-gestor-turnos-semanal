import sqlite3

class Modelo:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()

    #-----------------TABLAS-------------------------

        self.c.execute('''CREATE TABLE IF NOT EXISTS Usuario 
                          ("ID_Usuario"	INTEGER NOT NULL,
                            "Username"	TEXT(64) NOT NULL,
                            "Password"	TEXT(128) NOT NULL,
                            PRIMARY KEY("ID_Usuario" AUTOINCREMENT));''')
        self.conn.commit()

        self.c.execute('''CREATE TABLE IF NOT EXISTS Rol 
                          ("ID_Rol"	INTEGER NOT NULL,
                            "Nombre"	TEXT(64) NOT NULL,
                            "Descripcion"	TEXT(128),
                            PRIMARY KEY("ID_Rol" AUTOINCREMENT));''')
        self.conn.commit()

        self.c.execute('''CREATE TABLE IF NOT EXISTS Disponibilidad 
                          ("ID_Disponibilidad"	INTEGER NOT NULL,
                            "Nombre"	TEXT(64) NOT NULL,
                            "Descripcion"	TEXT(128),
                            PRIMARY KEY("ID_Disponibilidad" AUTOINCREMENT));''')
        self.conn.commit()

        self.c.execute('''CREATE TABLE IF NOT EXISTS Turno 
                          ("ID_Turno"	INTEGER NOT NULL,
                            "Nombre"	TEXT(64) NOT NULL,
                            "Lunes_Ingreso"	TEXT,
                            "Lunes_Salida"	TEXT,
                            "Martes_Ingreso"	TEXT,
                            "Martes_Salida"	TEXT,
                            "Miercoles_Ingreso"	TEXT,
                            "Miercoles_Salida"	TEXT,
                            "Jueves_Ingreso"	TEXT,
                            "Jueves_Salida"	TEXT,
                            "Viernes_Ingreso"	TEXT,
                            "Viernes_Salida"	TEXT,
                            "Sabado_Ingreso"	TEXT,
                            "Sabado_Salida"	TEXT,
                            "Domingo_Ingreso"	TEXT,
                            "Domingo_Salida"	TEXT,
                            PRIMARY KEY("ID_Turno" AUTOINCREMENT));''')
        self.conn.commit()
        
        self.c.execute('''CREATE TABLE IF NOT EXISTS Colaborador
                          ("ID_Colaborador"	INTEGER NOT NULL,
                            "Nombre"	TEXT(128) NOT NULL,
                            "Correo"	TEXT(128) NOT NULL,
                            "Telefono"	TEXT NOT NULL DEFAULT (2256 - 2222),
                            "ID_Rol"	INTEGER NOT NULL,
                            "ID_Turno"	INTEGER NOT NULL,
                            "ID_Disponibilidad"	INTEGER NOT NULL,
                            "Modalidad"	INTEGER NOT NULL DEFAULT (1),
                            PRIMARY KEY("ID_Colaborador" AUTOINCREMENT),
                            CONSTRAINT "Colaborador_FK_4" FOREIGN KEY("ID_Turno") REFERENCES "Turno"("ID_Turno"),
                            CONSTRAINT "Colaborador_FK_3" FOREIGN KEY("ID_Rol") REFERENCES "Rol"("ID_Rol"),
                            CONSTRAINT "Colaborador_FK_5" FOREIGN KEY("ID_Disponibilidad") REFERENCES "Disponibilidad"("ID_Disponibilidad"));''')
        self.conn.commit()

    #-------------------LOGIN--------------------------
    def inicio_usuario(self, username, password):
        self.c.execute("SELECT * FROM Usuario WHERE Username=? AND Password=?", (username, password))
        user = self.c.fetchone()
        return True if user else False

    #-----------------USUARIOS-------------------------

    def agregar_usuario(self, username, password):
        try:
            self.c.execute("INSERT INTO Usuario (Username, Password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True  
        except Exception as e:
            print(f"Error agregando usuario: {e}")
            return False  

    def eliminar_usuario(self, id):
        try:
            self.c.execute("DELETE FROM Usuario WHERE ID_Usuario=?", (id,))
            self.conn.commit()
            return True  
        except Exception as e:
            print(f"Error eliminando usuario: {e}")
            return False 

    def actualizar_usuario(self, id_usuario, username, password):
        try:
            self.c.execute("UPDATE Usuario SET Username=?, Password=? WHERE ID_Usuario=?", (username, password, id_usuario))
            self.conn.commit()
            return True  
        except Exception as e:
            print(f"Error actualizando usuario: {e}")
            return False

    def obtener_usuarios(self):
        self.c.execute("SELECT * FROM Usuario")
        return self.c.fetchall()

    #-----------------ROLES-------------------------

    def agregar_rol(self, nombre, descripcion):
        try:
            self.c.execute("INSERT INTO Rol (Nombre, Descripcion) VALUES (?, ?)", (nombre, descripcion))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error agregando rol: {e}")
            return False        

    def eliminar_rol(self, id):
        try:
            self.c.execute("DELETE FROM Rol WHERE ID_Rol=?", (id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error eliminando rol: {e}")
            return False      

    def actualizar_rol(self, id_rol, nombre, descripcion):
        try:
            self.c.execute("UPDATE Rol SET Nombre=?, Descripcion=? WHERE ID_Rol=?", (nombre, descripcion, id_rol))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error actualizando rol: {e}")
            return False  

    def obtener_roles(self):
        self.c.execute("SELECT * FROM Rol")
        return self.c.fetchall()
    
    def obtener_nombre_roles(self):
        self.c.execute("SELECT Nombre FROM Rol")
        return self.c.fetchall()
    
    def comprobar_nombre_rol(self, nombre):
        self.c.execute("SELECT 1 FROM Rol WHERE Nombre = ?", (nombre,))
        return self.c.fetchall()

    #-----------------DISPONIBILIDADES-------------------------

    def agregar_disponibilidad(self, nombre, descripcion):
        try:
            self.c.execute("INSERT INTO Disponibilidad (Nombre, Descripcion) VALUES (?, ?)", (nombre, descripcion))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error agregando disponibilidad: {e}")
            return False  

    def eliminar_disponibilidad(self, id):
        try:
            self.c.execute("DELETE FROM Disponibilidad WHERE ID_Disponibilidad=?", (id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error eliminadno disponibilidad: {e}")
            return False  

    def actualizar_disponibilidad(self, id_disponibilidad, nombre, descripcion):
        try:
            self.c.execute("UPDATE Disponibilidad SET Nombre=?, Descripcion=? WHERE ID_Disponibilidad=?", (nombre, descripcion, id_disponibilidad))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error aactualizando disponibilidad: {e}")
            return False  

    def obtener_disponibilidades(self):
        self.c.execute("SELECT * FROM Disponibilidad")
        return self.c.fetchall()
    
    def obtener_nombre_disponibilidades(self):
        self.c.execute("SELECT Nombre FROM Disponibilidad")
        return self.c.fetchall()
    
    def comprobar_nombre_disponibilidad(self, nombre):
        self.c.execute("SELECT 1 FROM Disponibilidad WHERE Nombre = ?", (nombre,))
        return self.c.fetchall()

    #-----------------TURNOS-------------------------
        
    def agregar_turno(self, nombre, lunes_ingreso, lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida):
        try:
            self.c.execute("INSERT INTO Turno (Nombre, Lunes_Ingreso, Lunes_Salida, Martes_Ingreso, Martes_Salida, Miercoles_Ingreso, Miercoles_Salida, Jueves_Ingreso, Jueves_Salida, Viernes_Ingreso, Viernes_Salida, Sabado_Ingreso, Sabado_Salida, Domingo_Ingreso, Domingo_Salida) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nombre, lunes_ingreso, lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error agregando turno: {e}")
            return False  
    
    def eliminar_turno(self, id):
        try:
            self.c.execute("DELETE FROM Turno WHERE ID_Turno=?", (id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error eliminando turno: {e}")
            return False  
    
    def actualizar_turno(self, nombre, lunes_ingreso, lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id_turno ):
        try:
            self.c.execute("UPDATE Turno SET Nombre=?, Lunes_Ingreso=?, Lunes_Salida=?, Martes_Ingreso=?, Martes_Salida=?, Miercoles_Ingreso=?, Miercoles_Salida=?, Jueves_Ingreso=?, Jueves_Salida=?, Viernes_Ingreso=?, Viernes_Salida=?, Sabado_Ingreso=?, Sabado_Salida=?, Domingo_Ingreso=?, Domingo_Salida=? WHERE ID_Turno=?", (nombre, lunes_ingreso, lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id_turno))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error actualizando turno: {e}")
            return False  

    def obtener_turnos(self):
        self.c.execute("SELECT * FROM Turno")
        return self.c.fetchall()
    
    def obtener_nombre_turnos(self):
        self.c.execute("SELECT Nombre FROM Turno")
        return self.c.fetchall()
    
    def comprobar_nombre_turno(self, nombre):
        self.c.execute("SELECT 1 FROM Turno WHERE Nombre = ?", (nombre,))
        return self.c.fetchall()
    
    #-----------------COLABORADORES-------------------------
    
    def agregar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad):
        try:
            self.c.execute("INSERT INTO Colaborador (Nombre, Correo, Telefono, ID_Rol, ID_Turno, ID_Disponibilidad, Modalidad) VALUES(?, ?, ?, ?, ?, ?, ?)", (nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error agregando colaborador: {e}")
            return False  
    
    def eliminar_colaborador(self, id):
        try:
            self.c.execute("DELETE FROM Colaborador WHERE ID_Colaborador=?", (id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error eliminando colaborador: {e}")
            return False  
    
    def actualizar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador):
        try:
            self.c.execute("UPDATE Colaborador SET Nombre=?, Correo=?, Telefono=?, ID_Rol=?, ID_Turno=?, ID_Disponibilidad=?, Modalidad=? WHERE ID_Colaborador=?", (nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error actualizando colaborador: {e}")
            return False  
    
    def obtener_colaboradores(self):
        self.c.execute("SELECT * FROM Colaborador")
        return self.c.fetchall()
    
    def obtener_colaboradores_nombre_id(self):
        self.c.execute("SELECT ID_Colaborador, Nombre FROM Colaborador")
        return self.c.fetchall()
    
    # Para comprobar si existe el correo en la BD
    def comprobar_correo_colaborador(self, correo):
        self.c.execute("SELECT 1 FROM Colaborador WHERE Correo = ?", (correo,))
        return self.c.fetchall()
    
    def obtener_filtros_colaborador(self):
        self.c.execute("""
                            SELECT 'Rol: ' || R.Nombre AS NombreDisplay, R.ID_Rol AS Valor
                            FROM Rol R
                            UNION
                            SELECT 'Turno: ' || T.Nombre AS NombreDisplay, T.ID_turno AS Valor
                            FROM Turno T
                            UNION
                            SELECT 'Disponibilidad: ' || D.Nombre AS NombreDisplay, D.ID_Disponibilidad AS Valor
                            FROM Disponibilidad D
                            UNION
                            SELECT CASE C.Modalidad
                                WHEN 1 THEN "Modalidad: Presencial"
                                WHEN 2 THEN "Modalidad: Virtual"
                            END AS NombreDisplay,
                                CASE C.Modalidad
                                WHEN 1 THEN 1
                                WHEN 2 THEN 2
                            END AS Valor
                            FROM Colaborador C
                       """)
        return self.c.fetchall()
    
    def filtrar_colaboradores(self, filtro, valor):
        self.c.execute(f"""
                            SELECT 
                                C.ID_Colaborador, C.Nombre, C.Correo, C.Telefono,
                                R.Nombre AS Rol,
                                T.Nombre AS Turno,
                                D.Nombre AS Disponibilidad,
                                CASE C.Modalidad
                                    WHEN 1 THEN "Presencial"
                                    WHEN 2 THEN "Virtual"
                                    ELSE "Desconocido"
                                END AS Modalidad
                                FROM Colaborador C
                                INNER JOIN Rol R ON R.ID_Rol = C.ID_Rol 
                                INNER JOIN Turno T ON T.ID_Turno = C.ID_Turno 
                                INNER JOIN Disponibilidad D ON D.ID_Disponibilidad = C.ID_Disponibilidad
                            WHERE {filtro} = ?
                       """, (valor,))
        return self.c.fetchall()
    
    def obtener_colaboradores_bonito(self):
        self.c.execute("""
                        SELECT 
                            C.ID_Colaborador, C.Nombre, C.Correo, C.Telefono,
                            R.Nombre AS Rol,
                            T.Nombre AS Turno,
                            D.Nombre AS Disponibilidad,
                            CASE C.Modalidad
                                WHEN 1 THEN "Presencial"
                                WHEN 2 THEN "Virtual"
                                ELSE "Desconocido"
                            END AS Modalidad
                            FROM Colaborador C
                            INNER JOIN Rol R ON R.ID_Rol = C.ID_Rol 
                            INNER JOIN Turno T ON T.ID_Turno = C.ID_Turno 
                            INNER JOIN Disponibilidad D ON D.ID_Disponibilidad = C.ID_Disponibilidad 
                       """)
        return self.c.fetchall()
    
    #-------------------HORARIO----------------------------

    def obtener_id_disponible(self):
        self.c.execute("SELECT ID_Disponibilidad FROM Disponibilidad WHERE Nombre = 'Disponible'")
        resultado = self.c.fetchone() 
        if resultado:
            return resultado[0]  
        else:
            return None 

    def obtener_colaboradores_disponibles(self, id_disponible):
        self.c.execute("SELECT * FROM Colaborador WHERE ID_Disponibilidad = ?",(id_disponible,))
        return self.c.fetchall()
    
    def agregar_horario(self,info_horario):
        try:
            
            self.c.execute("INSERT INTO Horario (ID_Colaborador, DiaSemana, Prof_1, Prof_2, Prof_3, Almuerzo, HorasExtr) VALUES(?, ?, ?, ?, ?, ?, ?)", (info_horario[0], info_horario[1], info_horario[2], info_horario[3], info_horario[4], info_horario[5], info_horario[6]))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error agregando horario: {e}")
            return False  
        
    def eliminar_horario(self):
        try:
            self.c.execute("DELETE FROM Horario")
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error agregando horario: {e}")
            return False  
    
    def obtener_horario_colaborador(self, id_colaborador):
        self.c.execute("SELECT DiaSemana, Prof_1, Prof_2, Prof_3, Almuerzo, HorasExtr FROM Horario WHERE ID_Colaborador = ?", (id_colaborador,))
        return self.c.fetchall()
    
    def obtener_horario_colaborador2(self, id_colaborador):
        self.c.execute("""
                        SELECT
                            H.DiaSemana,
                            CASE H.DiaSemana
                                WHEN 'Lunes' THEN T.Lunes_Ingreso
                                WHEN 'Martes' THEN T.Martes_Ingreso
                                WHEN 'Miercoles' THEN T.Miercoles_Ingreso
                                WHEN 'Jueves' THEN T.Jueves_Ingreso
                                WHEN 'Viernes' THEN T.Viernes_Ingreso
                                WHEN 'Sabado' THEN T.Sabado_Ingreso
                                WHEN 'Domingo' THEN T.Domingo_Ingreso
                                ELSE NULL
                            END AS Ingreso_Dia,
                            CASE H.DiaSemana
                                WHEN 'Lunes' THEN T.Lunes_Salida
                                WHEN 'Martes' THEN T.Martes_Salida
                                WHEN 'Miercoles' THEN T.Miercoles_Salida
                                WHEN 'Jueves' THEN T.Jueves_Salida
                                WHEN 'Viernes' THEN T.Viernes_Salida
                                WHEN 'Sabado' THEN T.Sabado_Salida
                                WHEN 'Domingo' THEN T.Domingo_Salida
                                ELSE NULL
                            END AS Salida_Dia,
                            H.Prof_1,
                            H.Prof_2,
                            H.Prof_3,
                            H.Almuerzo,
                            H.HorasExtr
                            FROM Horario H
                            INNER JOIN Colaborador C ON H.ID_Colaborador = C.ID_Colaborador
                            INNER JOIN Turno T ON C.ID_Turno = T.ID_Turno
                            WHERE C.ID_Colaborador=?
                       """, (id_colaborador,))
        return self.c.fetchall()
    
    def actualizar_horario(self, id_colaborador, dia_semana, prof1, prof2, prof3, almuerzo, horas_extra):
        try:
            self.c.execute("""
                            UPDATE Horario
                            SET
                                Prof_1 = ?,
                                Prof_2 = ?,
                                Prof_3 = ?,
                                Almuerzo = ?,
                                HorasExtr = ?
                            WHERE
                                ID_Colaborador = ? AND
                                DiaSemana = ?;
                            """, ( prof1, prof2, prof3, almuerzo, horas_extra,id_colaborador, dia_semana))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error actualizando colaborador: {e}")
            return False

    def obtener_horario_completo(self):
        self.c.execute('''SELECT
                            C.ID_Colaborador,
                            C.Nombre AS Nombre_Colaborador,
                            H.DiaSemana,
                            CASE H.DiaSemana
                                WHEN 'Lunes' THEN T.Lunes_Ingreso
                                WHEN 'Martes' THEN T.Martes_Ingreso
                                WHEN 'Miercoles' THEN T.Miercoles_Ingreso
                                WHEN 'Jueves' THEN T.Jueves_Ingreso
                                WHEN 'Viernes' THEN T.Viernes_Ingreso
                                WHEN 'Sabado' THEN T.Sabado_Ingreso
                                WHEN 'Domingo' THEN T.Domingo_Ingreso
                                ELSE NULL
                            END AS Ingreso_Dia,
                            CASE H.DiaSemana
                                WHEN 'Lunes' THEN T.Lunes_Salida
                                WHEN 'Martes' THEN T.Martes_Salida
                                WHEN 'Miercoles' THEN T.Miercoles_Salida
                                WHEN 'Jueves' THEN T.Jueves_Salida
                                WHEN 'Viernes' THEN T.Viernes_Salida
                                WHEN 'Sabado' THEN T.Sabado_Salida
                                WHEN 'Domingo' THEN T.Domingo_Salida
                                ELSE NULL
                            END AS Salida_Dia,
                            H.Prof_1,
                            H.Prof_2,
                            H.Prof_3,
                            H.Almuerzo,
                            H.HorasExtr
                        FROM Horario H
                        JOIN Colaborador C ON H.ID_Colaborador = C.ID_Colaborador
                        JOIN Turno T ON C.ID_Turno = T.ID_Turno;''')
        return self.c.fetchall()

    def obtener_horario_individual(self, id_colaborador):
        self.c.execute('''SELECT
                            C.ID_Colaborador,
                            C.Nombre AS Nombre_Colaborador,
                            H.DiaSemana,
                            CASE H.DiaSemana
                                WHEN 'Lunes' THEN T.Lunes_Ingreso
                                WHEN 'Martes' THEN T.Martes_Ingreso
                                WHEN 'Miercoles' THEN T.Miercoles_Ingreso
                                WHEN 'Jueves' THEN T.Jueves_Ingreso
                                WHEN 'Viernes' THEN T.Viernes_Ingreso
                                WHEN 'Sabado' THEN T.Sabado_Ingreso
                                WHEN 'Domingo' THEN T.Domingo_Ingreso
                                ELSE NULL
                            END AS Ingreso_Dia,
                            CASE H.DiaSemana
                                WHEN 'Lunes' THEN T.Lunes_Salida
                                WHEN 'Martes' THEN T.Martes_Salida
                                WHEN 'Miercoles' THEN T.Miercoles_Salida
                                WHEN 'Jueves' THEN T.Jueves_Salida
                                WHEN 'Viernes' THEN T.Viernes_Salida
                                WHEN 'Sabado' THEN T.Sabado_Salida
                                WHEN 'Domingo' THEN T.Domingo_Salida
                                ELSE NULL
                            END AS Salida_Dia,
                            H.Prof_1,
                            H.Prof_2,
                            H.Prof_3,
                            H.Almuerzo,
                            H.HorasExtr
                        FROM Horario H
                        JOIN Colaborador C ON H.ID_Colaborador = C.ID_Colaborador
                        JOIN Turno T ON C.ID_Turno = T.ID_Turno
                        WHERE C.ID_Colaborador = ?''',(id_colaborador,))
        return self.c.fetchall()  
    #-----------------OTROS-------------------------

    def cerrar_conexion(self):
        self.conn.close()
