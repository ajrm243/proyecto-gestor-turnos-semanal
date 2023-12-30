from modelo import Modelo
from vista import Vista
# Es para la carga de colaboradores
import pandas as pd

class Controlador:
    def __init__(self):
        self.modelo = Modelo("proyecto_verano.db")
        self.vista = Vista(self)
        self.vista.iniciar_aplicacion()

    #----------LOGIN-------------
    def inicio_usuario(self, username, password):
        resultado = self.modelo.inicio_usuario(username, password)
        self.vista.procesar_inicio_usuario(resultado)
            
    def inicio_admin(self, username, password):
        autenticado = username == "admin" and password == "admin"
        self.vista.procesar_inicio_admin(autenticado)
    #--------USUARIOS------------
    def agregar_usuario(self, username, password):
        self.modelo.agregar_usuario(username, password)
        self.vista.actualizar_lista_usuarios()

    def actualizar_usuario(self, id, username, password):
        self.modelo.actualizar_usuario(id, username, password)
        self.vista.actualizar_lista_usuarios()    
    
    def eliminar_usuario(self, id):
        self.modelo.eliminar_usuario(id)
        self.vista.actualizar_lista_usuarios()

    def obtener_usuarios(self):
        return self.modelo.obtener_usuarios()
    
    #--------ROLES-----------
    def agregar_rol(self, nombre, descripcion):
        self.modelo.agregar_rol(nombre, descripcion)
        self.vista.actualizar_lista_roles()

    def actualizar_rol(self, id, nombre, descripcion):
        self.modelo.actualizar_rol(id, nombre, descripcion)
        self.vista.actualizar_lista_roles()    
    
    def eliminar_rol(self, id):
        self.modelo.eliminar_rol(id)
        self.vista.actualizar_lista_roles()

    def obtener_roles(self):
        return self.modelo.obtener_roles()
    
    def obtener_id_roles(self):
        return self.modelo.obtener_id_roles()
    
    #--------DISPONIBILIDADES-----------

    def agregar_disponibilidad(self, nombre, descripcion):
        self.modelo.agregar_disponibilidad(nombre, descripcion)
        self.vista.actualizar_lista_disponibilidades()

    def actualizar_disponibilidad(self, id, nombre, descripcion):
        self.modelo.actualizar_disponibilidad(id, nombre, descripcion)
        self.vista.actualizar_lista_disponibilidades()    
    
    def eliminar_disponibilidad(self, id):
        self.modelo.eliminar_disponibilidad(id)
        self.vista.actualizar_lista_disponibilidades()

    def obtener_disponibilidades(self):
        return self.modelo.obtener_disponibilidades()
    
    def obtener_id_disponibilidades(self):
        return self.modelo.obtener_id_disponibilidades()
    
    #--------TURNOS-----------
    
    def agregar_turno(self, nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida):
        self.modelo.agregar_turno(nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida)
        self.vista.actualizar_lista_turnos()
    
    def actualizar_turno(self, nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id):
        self.modelo.actualizar_turno(nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id)
        self.vista.actualizar_lista_colaboradores()
    
    def eliminar_turno(self, id):
        self.modelo.eliminar_turno(id)
        self.vista.actualizar_lista_turnos()
    
    def obtener_turnos(self):
        return self.modelo.obtener_turnos()
        #self.vista.actualizar_lista_colaboradores()
    
    def obtener_id_turnos(self):
        return self.modelo.obtener_id_turnos()


    #--------COLABORADORES-----------
    
    def agregar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad):
        self.modelo.agregar_colaborador(nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad)
        self.vista.actualizar_lista_colaboradores()
    
    def actualizar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador):
        self.modelo.actualizar_colaborador(nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador)
        self.vista.actualizar_lista_colaboradores()
    
    def eliminar_colaborador(self, id):
        self.modelo.eliminar_colaborador(id)
        self.vista.actualizar_lista_colaboradores()
    
    def obtener_colaboradores(self):
        return self.modelo.obtener_colaboradores()
        #self.vista.actualizar_lista_colaboradores()
    
    def cargar_lista_colaboradores(self, ruta):
        file = pd.ExcelFile(ruta)
        df = pd.read_excel(file, converters={'Telefono':str, 'Rol':int, 'Turno':int, 'Disponibilidad':int, 'Modalidad':int})
        for row in df.to_records(index=False):
            #print(row["Nombre"], type(row["Nombre"]))
            self.modelo.agregar_colaborador(row["Nombre"], row["Correo"], row["Telefono"]
                                            , row["Rol"].item(), row["Turno"].item(), row["Disponibilidad"].item()
                                            , row["Modalidad"].item())
        

#--------MAIN----------
if __name__ == "__main__":
    controlador = Controlador()
