import log
import random
from clases.heroe import Heroe
from clases.villano import Villano

personajes = [] #array con los heroes y los villanos

def menu():
    print("1) Para crear Heroe")
    print("2) Para crear Villano")
    print("3) Para buscar un heroe o villano")
    print("4) Emparejar héroe y villano")
    print("5) Salir")

def gestionAulaDeHeroesYVillanos(opcion):
    match opcion:
        case 1:
            nombre = input("Nombre: ")
            ap1 = input("Primer apellido: ")
            ap2 = input("Segundo apellido: ")
            fecha = input("Fecha de nacimiento: (dd/mm/yyyy):")
            id = input("ID: ")
            h = Heroe(nombre, ap1, ap2, fecha, id)
            personajes.append(h)
            log.info(f"Heroe creado: {h}")
            print(h)
        case 2:
            nombre = input("Nombre: ")
            ap1 = input("Primer apellido: ")
            ap2 = input("Segundo apellido: ")
            fecha = input("Fecha de nacimiento: (dd/mm/yyyy): ")
            id = input("ID: ")
            v = Villano(nombre, ap1, ap2, fecha, id)
            personajes.append(v)
            log.info(f"Villano creado: {v}")
            print(v)
        case 3:
            atributo = input("Buscar por atributo: (nombre, ap1, ap2, fecha, id)")
            valor = input("Valor: ")
            encontrados = []
            for p in personajes:
                if hasattr(p, atributo) and str(getattr(p, atributo)) == valor:
                    encontrados.append(p)
                elif isinstance(p, (Heroe, Villano)) and atributo in p.cualidades:
                    if int(p.cualidades[atributo]) >= int(valor):
                        encontrados.append(p)
            if encontrados:
                for e in encontrados:
                    print(e)
            else:
                print("No se encontró nada")
            log.info(f"Búsqueda por {atributo}={valor} → {len(encontrados)} resultados")

        case 4:
            heroes = [p for p in personajes if isinstance(p, Heroe)]
            villanos = [p for p in personajes if isinstance(p, Villano)]
            if not heroes or not villanos:
                print("No hay héroes o villanos suficientes")
                return
            h = random.choice(heroes)
            v = random.choice(villanos)
            hp = h.puntuacionTotal
            vp = v.puntuacionTotal
            diff = hp - vp
            if diff < 15:
                resultado = "Equilibrado"
            elif hp > vp:
                resultado = "El héroe es más fuerte que el villano"
            else:
                resultado = "El villano es más fuerte que el héroe"
            print(f"Emparejamiento: {h.nombre} vs {v.nombre} → {resultado}")
            log.info(f"Emparejamiento: {h} vs {v} → {resultado}")

def main():
    try:
        while True:
            menu()
            opcion = int(input("Que eliges: "))
            if opcion > 5:
                print("Selecciona una opcion valida")
            elif opcion == 5:
                break
            else:
                gestionAulaDeHeroesYVillanos(opcion)
    except Exception as e:
        log.error(f"Error: {e}")
        print(f"Error registrado en el log: {e}")


if __name__ == "__main__":
    main()