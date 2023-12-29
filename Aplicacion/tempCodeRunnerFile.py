from modelo import Modelo
from vista import Vista
# Es para la carga de colaboradores
import pandas as pd

class Controlador:
    def __init__(self):
        self.modelo = Modelo("proyecto_verano.db")
        self.vista = Vista(self)
        self.vista.iniciar_aplicacion()

    #--------USUARIOS------------
    def agregar_usuario(self, username, password):
        self.modelo.agregar_usuario(username, password)
        self.vista.actualizar_lista_usuarios()

    def actualizar_usuario(self, id, username, pass