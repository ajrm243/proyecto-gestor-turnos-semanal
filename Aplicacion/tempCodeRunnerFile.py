from modelo import Modelo
from vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo("usuarios.db")
        self.vista = Vista(self)
        self.vista.actualizar_lista_usuarios()
        self.vista.iniciar_aplicacion()

    def agregar_usuario(self, nombre, edad):
        self.modelo.agregar_usuario(nombre, edad)
        self.vista.actualizar_lista_usuarios()

    def actualizar_usuario(self, id, nombre, edad):
        self.modelo.actualizar_usuario(id, nombre, edad)
        self.vista.actualizar_lista_usuarios()    
    
    def eliminar_usuario(self, id):
        self.modelo.eliminar_usuario(id)
        self.vista.actualizar_lista_usuarios()

    def obtener_usuarios(self):
        return self.modelo.obtener_usuarios()

if __name__ == "__main__":
    controlador = Controlador()
