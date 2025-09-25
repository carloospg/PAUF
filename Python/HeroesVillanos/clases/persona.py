class Persona:
    nombre = ""
    ap1 = ""
    ap2 = ""
    fechaNac = ""
    id = 0
    puntuacionTotal = 0

    def __init__(self, nombre, ap1, ap2, fechaNac, id, puntuacionTotal):
        self.nombre = nombre
        self.ap1 = ap1
        self.ap2 = ap2
        self.fechaNac = fechaNac
        self.id = id
        self.puntuacionTotal = puntuacionTotal


    def __str__(self):
        print("Nombre: " + self.nombre + " Apellido 1: " + self.ap1 + " Apellido 2: " + self.ap2 + " Fecha nacimiento: " + self.fechaNac + " Id: " + self.id + " Puntuacion Total: " + self.puntuacionTotal)

