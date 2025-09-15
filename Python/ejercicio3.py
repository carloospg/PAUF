import numpy as np

# Crea una lista con los goles de 6 jugadores
goleadores = [3, 4, 7, 10, 1, 14]

# Muestra cuántos jugadores hay
print(len(goleadores))

# Ordena la lista de goles de menor a mayor y luego de mayor a menor.

goleadores.sort(reverse=True)
print(goleadores)
goleadores.sort(reverse=False)
print(goleadores)

# Muestra el máximo y el mínimo de la lista (max() y min()).

print(max(goleadores))
print(min(goleadores))

# Media de goles
print("------------------")

golesTotales = sum(goleadores)
print(golesTotales)

media = golesTotales / len(goleadores)
print(media)

print("------------------")

goles = np.array([1,2,3])
print(np.mean(goles))