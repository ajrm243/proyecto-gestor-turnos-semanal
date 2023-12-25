from modelo import Modelo
from vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo("proyecto_verano.db")
        self.vista = Vista(self)
        self.vista.iniciar_aplicacion()

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

    
#--------MAIN----------
    
if __name__ == "__main__":
    controlador = Controlador()
