from os import remove

locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]

# Imprimir los partidos

for i in range(5):
    print(locales[i] + " vs " + visitantes[i])

# Elimina un partido (por ejemplo, el de Sevilla vs Villarreal).

locales.remove("Sevilla")
visitantes.remove("Villarreal")

# Añade un nuevo partido con un equipo inventado.

locales.append("Manchester City")
visitantes.append("PSG")

print(" ")

for i in range(5):
    print(locales[i] + " vs " + visitantes[i])