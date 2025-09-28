from datetime import datetime

class Persona:

    def __init__(self, nombre, ap1, ap2, fechaNac, id, puntuacionTotal=0):
        self.nombre = nombre
        self.ap1 = ap1
        self.ap2 = ap2
        self.fechaNac = fechaNac
        self.id = id
        self.puntuacionTotal = puntuacionTotal


    def __str__(self):
        print("Nombre: " + self.nombre + " Apellido 1: " + self.ap1 + " Apellido 2: " + self.ap2 + " Fecha nacimiento: " + self.fechaNac + " Id: " + self.id + " Puntuacion Total: " + self.puntuacionTotal)

    def anios(self):
        dia, mes, anio = map(int, self.fechaNac.split("/")) # ma
        fecha = datetime(anio, mes, dia)

        hoy = datetime.now()
        diferencia = hoy - fecha

        edad = int(diferencia.days / 365)
        return edad