from modelo import Modelo
from vista import Vista
from datetime import datetime
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
    
    def obtener_nombre_roles(self):
        return self.modelo.obtener_nombre_roles()
    
    def comprobar_nombre_rol(self, correo):
        estado_consulta = self.modelo.comprobar_nombre_rol(correo)
        return estado_consulta
    
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
    
    def obtener_nombre_disponibilidades(self):
        return self.modelo.obtener_nombre_disponibilidades()

    def comprobar_nombre_disponibilidad(self, correo):
        estado_consulta = self.modelo.comprobar_nombre_disponibilidad(correo)
        return estado_consulta
    
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
    
    def obtener_nombre_turnos(self):
        return self.modelo.obtener_nombre_turnos()
    
    def comprobar_nombre_turno(self, correo):
        estado_consulta = self.modelo.comprobar_nombre_turno(correo)
        return estado_consulta
    

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
            res_comprobacion = self.modelo.comprobar_correo_colaborador(row["Correo"])
            if not res_comprobacion:
                estado_consulta = self.modelo.agregar_colaborador(row["Nombre"], row["Correo"], row["Telefono"]
                                                , row["Rol"].item(), row["Turno"].item(), row["Disponibilidad"].item()
                                                , row["Modalidad"].item())
                if (not estado_consulta):
                    return False
            else:
                #Hay un colaborador que ya está en la base, se sigue
                continue
        return True
    
    def comprobar_correo_colaborador(self, correo):
        estado_consulta = self.modelo.comprobar_correo_colaborador(correo)
        #print(estado_consulta)
        return estado_consulta
    
    def obtener_filtros_colaborador(self):
        return self.modelo.obtener_filtros_colaborador()
    
    def filtrar_colaboradores(self, filtro, valor):
        return self.modelo.filtrar_colaboradores(filtro, valor)
    
    def obtener_colaboradores_bonito(self):
        return self.modelo.obtener_colaboradores_bonito()
    
    def obtener_colaboradores_nombre_id(self):
        return self.modelo.obtener_colaboradores_nombre_id()
    
#--------HORARIO-----------
    
    def obtener_colaboradores_disponibles(self):
        id_disponible = self.modelo.obtener_id_disponible()
        lista_colaboradores_disponibles = self.modelo.obtener_colaboradores_disponibles(id_disponible)
        if len(lista_colaboradores_disponibles) >= 15:
        #if len(lista_colaboradores_disponibles) >= 5:
            print("Pasa")
            return lista_colaboradores_disponibles
        else:
            print("No pasa")
            return 0
        
    def identificar_turno(self,colaborador, lista_turnos):
        for turno in lista_turnos:
            if colaborador[5] == turno[0]:
                return turno


    def informacion_turno(self,nombre_turno):
        match nombre_turno:
            case "T1_F":
                return [['Lunes','NA','NA','NA','NA','NA'],
                        ['Martes','NA','NA','NA','NA','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Domingo','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA']]
            case "T2_F":
                return [['Lunes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Martes','NA','NA','NA','NA','NA'],
                        ['Miercoles','NA','NA','NA','NA','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Domingo','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA']]
            case "T3_F":
                return [['Lunes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Martes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Miercoles','NA','NA','NA','NA','NA'],
                        ['Jueves','NA','NA','NA','NA','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Domingo','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA']]
            case "T4_F":
                return [['Lunes','NA','NA','NA','NA','NA'],
                        ['Martes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Miercoles','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Sabado','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "T5_F":
                return [['Lunes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Martes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Miercoles','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','NA','NA','NA','NA','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA']]
            case "T6_F":
                return [['Lunes','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Martes','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "TF1_FF":
                return [['Lunes','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Martes','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "TF2_FN":
                return [['Lunes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Martes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Miercoles','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Jueves','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Viernes','NA','NA','NA','NA','NA'],
                        ['Sabado','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Domingo','19:50-20:00','NA','NA','21:50-22:10','NA']]
            case "TF3_FN":
                return [['Lunes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Martes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Miercoles','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Jueves','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Viernes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','19:50-20:00','NA','NA','21:50-22:10','NA']]
            case "TF4_FN":
                return [['Lunes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Martes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Miercoles','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Jueves','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Viernes','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Sabado','19:50-20:00','NA','NA','21:50-22:10','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "TF7_FM":
                return [['Lunes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Martes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Miercoles','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Jueves','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Viernes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','2:15-2:25','NA','NA','4:05-4:25','NA']]
            case "TF8_FM":
                return [['Lunes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Martes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Miercoles','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Jueves','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Viernes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Sabado','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "TF9_FM":
                return [['Lunes','NA','NA','NA','NA','NA'],
                        ['Martes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Miercoles','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Jueves','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Viernes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Sabado','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Domingo','2:15-2:25','NA','NA','4:05-4:25','NA']]
            case "TF10_FM":
                return [['Lunes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Martes','NA','NA','NA','NA','NA'],
                        ['Miercoles','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Jueves','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Viernes','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Sabado','2:15-2:25','NA','NA','4:05-4:25','NA'],
                        ['Domingo','2:15-2:25','NA','NA','4:05-4:25','NA']]
            case "TF12_MN":
                return [['Lunes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Martes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Miercoles','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Jueves','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Viernes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','20:10-20:20','NA','NA','22:20-22:40','NA']]
            case "TF13_MN":
                return [['Lunes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Martes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Miercoles','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Jueves','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Viernes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Sabado','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "TF14_FF":
                return [['Lunes','NA','NA','NA','NA','NA'],
                        ['Martes','NA','NA','NA','NA','NA'],
                        ['Miercoles','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Sabado','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Domingo','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA']]
            case "T1_M":
                return [['Lunes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Martes','NA','NA','NA','NA','NA'],
                        ['Miercoles','NA','NA','NA','NA','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Domingo','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA']]
            case "T2_M":
                return [['Lunes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Martes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Miercoles','NA','NA','NA','NA','NA'],
                        ['Jueves','NA','NA','NA','NA','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Domingo','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA']]
            case "T3_M":
                return [['Lunes','NA','NA','NA','NA','NA'],
                        ['Martes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Sabado','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "T4_M":
                return [['Lunes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Martes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Miercoles','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','NA','NA','NA','NA','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA']]
            case "T5_M":
                return [['Lunes','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Martes','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "T6_M":
                return [['Lunes','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Martes','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "HFC1":
                return [['Lunes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Martes','NA','NA','NA','NA','NA'],
                        ['Miercoles','NA','NA','NA','NA','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Domingo','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA']]
            case "HFC2":
                return [['Lunes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Martes','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "HFC3":
                return [['Lunes','NA','NA','NA','NA','NA'],
                        ['Martes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Miercoles','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            case "HFC4":
                return [['Lunes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Martes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Miercoles','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Jueves','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Viernes','NA','NA','NA','NA','NA'],
                        ['Sabado','NA','NA','NA','NA','NA'],
                        ['Domingo','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA']]
            case "HFC5":
                return [['Lunes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Martes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Miercoles','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Jueves','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Viernes','20:10-20:20','NA','NA','22:20-22:40','NA'],
                        ['Sabado','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Domingo','NA','NA','NA','NA','NA']]
            
            case default:
                return [['Lunes','NA','NA','NA','NA','NA'],
                        ['Martes','NA','NA','NA','NA','NA'],
                        ['Miercoles','9:00-9:10','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Jueves','9:40-9:50','2:00-2:10','NA','12:00-12:45','NA'],
                        ['Viernes','9:20-9:30','2:20-2:30','NA','12:00-12:45','NA'],
                        ['Sabado','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA'],
                        ['Domingo','11:00-11:10','16:00-16:10','NA','13:00-13:45','NA']]
    

    def generar_horario(self):
        self.modelo.eliminar_horario()
        lista_colaboradores_disponibles = self.obtener_colaboradores_disponibles()
        lista_turnos = self.modelo.obtener_turnos()
        if type(lista_colaboradores_disponibles) == list:
            self.modelo.eliminar_horario()
            for colaborador in lista_colaboradores_disponibles:
                turno = self.identificar_turno(colaborador,lista_turnos)
                horario = self.informacion_turno(turno[1])
                
                for dia in horario:
                    info_horario = [colaborador[0]]+dia
                    print(info_horario)
                    self.modelo.agregar_horario(info_horario)

        return lista_colaboradores_disponibles

    def obtener_horario_colaborador(self, id_colaborador):
        return self.modelo.obtener_horario_colaborador(id_colaborador)
    
    def obtener_horario_colaborador2(self, id_colaborador):
        return self.modelo.obtener_horario_colaborador2(id_colaborador)
    
    def actualizar_horario(self, id_colaborador, dia_semana, prof1, prof2, prof3, almuerzo, horas_extra):
        estado_consulta = self.modelo.actualizar_horario(id_colaborador, dia_semana, prof1, prof2, prof3, almuerzo, horas_extra)
        return estado_consulta
    
    def generar_archivo_horario_completo(self):
        datos = self.modelo.obtener_horario_completo()
        i = -1
        id_colaborador, colaborador, diaSemana, ingreso, salida, prof_1, prof_2, prof_3, almuerzo, horasExtr = [], [], [], [], [], [], [], [], [], []
        for dato in datos:
            i = i+1
            id_colaborador.append(datos[i][0])
            colaborador.append(datos[i][1])
            diaSemana.append(datos[i][2])
            ingreso.append(datos[i][3])
            salida.append(datos[i][4])
            prof_1.append(datos[i][5])
            prof_2.append(datos[i][6])
            prof_3.append(datos[i][7])
            almuerzo.append(datos[i][8])
            horasExtr.append(datos[i][9])
        fecha = str(datetime.now().strftime('%d-%m-%Y'))
        datos = {"ID Colaborador": id_colaborador, "Nombre":colaborador,"Día":diaSemana,"Ingreso":ingreso,"Salida":salida,"Profiláctico 1":prof_1, "Profiláctico 2":prof_2, "Profiláctico 3": prof_3, "Almuerzo":almuerzo, "Horas Extra":horasExtr}
        df = pd.DataFrame(datos,columns = ["ID Colaborador", "Nombre","Día","Ingreso","Salida","Profiláctico 1", "Profiláctico 2", "Profiláctico 3", "Almuerzo","Horas Extra"])
        df.to_excel((f'HORARIO SEMANAL {fecha}.xlsx'))

    def generar_archivo_horario_individual(self, id_colaborador):
        datos = self.modelo.obtener_horario_individual(id_colaborador)
        i = -1
        ids_colaborador, colaborador, diaSemana, ingreso, salida, prof_1, prof_2, prof_3, almuerzo, horasExtr = [], [], [], [], [], [], [], [], [], []
        for dato in datos:
            i = i+1
            ids_colaborador.append(datos[i][0])
            colaborador.append(datos[i][1])
            diaSemana.append(datos[i][2])
            ingreso.append(datos[i][3])
            salida.append(datos[i][4])
            prof_1.append(datos[i][5])
            prof_2.append(datos[i][6])
            prof_3.append(datos[i][7])
            almuerzo.append(datos[i][8])
            horasExtr.append(datos[i][9])
        fecha = str(datetime.now().strftime('%d-%m-%Y'))
        datos = {"ID Colaborador": ids_colaborador, "Nombre":colaborador,"Día":diaSemana,"Ingreso":ingreso,"Salida":salida,"Profiláctico 1":prof_1, "Profiláctico 2":prof_2, "Profiláctico 3": prof_3, "Almuerzo":almuerzo, "Horas Extra":horasExtr}
        df = pd.DataFrame(datos,columns = ["ID Colaborador", "Nombre","Día","Ingreso","Salida","Profiláctico 1", "Profiláctico 2", "Profiláctico 3", "Almuerzo","Horas Extra"])
        df.to_excel((f'HORARIO {id_colaborador} {colaborador[0]} {fecha}.xlsx'))

#--------MAIN----------
if __name__ == "__main__":
    controlador = Controlador()
