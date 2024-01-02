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
        estado_consulta = self.modelo.inicio_usuario(username, password)
        self.vista.procesar_inicio_usuario(estado_consulta)
            
    def inicio_admin(self, username, password):
        autenticado = username == "admin" and password == "admin"
        self.vista.procesar_inicio_admin(autenticado)
    #--------USUARIOS------------
    def agregar_usuario(self, username, password):
        estado_consulta = self.modelo.agregar_usuario(username, password)
        return estado_consulta

    def eliminar_usuario(self, id):
        estado_consulta = self.modelo.eliminar_usuario(id)
        return estado_consulta

    def actualizar_usuario(self, id, username, password):
        estado_consulta = self.modelo.actualizar_usuario(id, username, password)
        return estado_consulta

    def obtener_usuarios(self):
        return self.modelo.obtener_usuarios()
    
    #--------ROLES-----------
    def agregar_rol(self, nombre, descripcion):
        estado_consulta = self.modelo.agregar_rol(nombre, descripcion)
        return estado_consulta

    def actualizar_rol(self, id, nombre, descripcion):
        estado_consulta = self.modelo.actualizar_rol(id, nombre, descripcion)
        return estado_consulta 
    
    def eliminar_rol(self, id):
        estado_consulta = self.modelo.eliminar_rol(id)
        return estado_consulta

    def obtener_roles(self):
        return self.modelo.obtener_roles()
    
    def obtener_id_roles(self):
        return self.modelo.obtener_id_roles()
    
    #--------DISPONIBILIDADES-----------

    def agregar_disponibilidad(self, nombre, descripcion):
        estado_consulta = self.modelo.agregar_disponibilidad(nombre, descripcion)
        return estado_consulta

    def actualizar_disponibilidad(self, id, nombre, descripcion):
        estado_consulta = self.modelo.actualizar_disponibilidad(id, nombre, descripcion)
        return estado_consulta
    
    def eliminar_disponibilidad(self, id):
        estado_consulta = self.modelo.eliminar_disponibilidad(id)
        return estado_consulta

    def obtener_disponibilidades(self):
        return self.modelo.obtener_disponibilidades()
    
    def obtener_id_disponibilidades(self):
        return self.modelo.obtener_id_disponibilidades()
    
    #--------TURNOS-----------
    
    def agregar_turno(self, nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida):
        estado_consulta = self.modelo.agregar_turno(nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida)
        return estado_consulta
    
    def actualizar_turno(self, nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id):
        estado_consulta = self.modelo.actualizar_turno(nombre, lunes_ingreso,lunes_salida, martes_ingreso, martes_salida, miercoles_ingreso, miercoles_salida, jueves_ingreso, jueves_salida, viernes_ingreso, viernes_salida, sabado_ingreso, sabado_salida, domingo_ingreso, domingo_salida, id)
        return estado_consulta
    
    def eliminar_turno(self, id):
        estado_consulta = self.modelo.eliminar_turno(id)
        return estado_consulta
    
    def obtener_turnos(self):
        return self.modelo.obtener_turnos()
        #self.vista.actualizar_lista_colaboradores()
    
    def obtener_id_turnos(self):
        return self.modelo.obtener_id_turnos()


    #--------COLABORADORES-----------
    
    def agregar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad):
        estado_consulta = self.modelo.agregar_colaborador(nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad)
        return estado_consulta
    
    def actualizar_colaborador(self, nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador):
        estado_consulta = self.modelo.actualizar_colaborador(nombre, correo, telefono, id_rol, id_turno, id_disponibilidad, modalidad, id_colaborador)
        return estado_consulta
    
    def eliminar_colaborador(self, id):
        estado_consulta = self.modelo.eliminar_colaborador(id)
        return estado_consulta
    
    def obtener_colaboradores(self):
        return self.modelo.obtener_colaboradores()
        #self.vista.actualizar_lista_colaboradores()
    
    def cargar_lista_colaboradores(self, ruta):
        file = pd.ExcelFile(ruta)
        df = pd.read_excel(file, converters={'Telefono':str, 'Rol':int, 'Turno':int, 'Disponibilidad':int, 'Modalidad':int})
        for row in df.to_records(index=False):
            self.modelo.agregar_colaborador(row["Nombre"], row["Correo"], row["Telefono"]
                                            , row["Rol"].item(), row["Turno"].item(), row["Disponibilidad"].item()
                                            , row["Modalidad"].item())
        

#--------MAIN----------
if __name__ == "__main__":
    controlador = Controlador()
