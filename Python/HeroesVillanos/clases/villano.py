from clases.persona import Persona
import random

class Villano(Persona):
    atributos = ["Chatgepeteador", "Entregador Tardio", "Ausencias", "Hablador"]

    def __init__(self, nombre, ap1, ap2, fechaNac, id):
        super().__init__(nombre, ap1, ap2, fechaNac, id)
        self.cualidades = {atrib: random.randint(0, 100) for atrib in Villano.atributos}
        self.puntuacionTotal = sum(self.cualidades.values()) / len(self.cualidades)

    def __str__(self):
        return f"Nombre: {self.nombre}, ap1: {self.ap1}, ap2: {self.ap2}, fecha de nacimiento: {self.fechaNac}, id: {self.id}, puntuacion total: {self.puntuacionTotal}, cualidades: {self.cualidades}"