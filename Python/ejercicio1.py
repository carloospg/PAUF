#Crea una lista con los 5 primeros equipos de la clasificación (puedes inventar el orden)
equipos = ["Real Madrid", "Athletic", "Villarreal", "Barcelona", "Espanyol"]

#1. Muestra en pantalla el primer y último equipo.
print(equipos[0] + " " + equipos[-1])

#2. Añade un equipo nuevo al final de la lista.
equipos.append("Getafe")
print(equipos)

#3 Inserta a mano un equipo en la primera posición.
equipos.insert(0, "Betis")
print(equipos)

#4. Elimina un equipo que ya no quieras que esté en la lista.
equipos.remove("Betis")
print(equipos)