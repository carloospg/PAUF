import calculadora as cal

#print("hola")
#resultado = 10
#a = float(input("dame un numero: "))
#concateno = a + 10

#print(concateno)

def miPrimerMetodo():
    nombre = "Carlos"
    print(nombre)
    ap1 = "Perez"
    print(ap1)
    ap2 = "Gosalvez"
    print(ap2)
    nombreCompleto = nombre + " " + ap1 + " " + ap2
    print(nombreCompleto)
    cal.sumar()

miPrimerMetodo()

a = 20
b = 30

if a > b:
    print("hola")
    if a > 100:
        print("que grande eres")
    elif a < 100:
        print("no eres tan grande")
else:
    print("adios")

#bucle for

ciclos = ["DAM1", "ASIR1", "DAW1"]
for ciclo in ciclos:
    print(ciclo)

for i in range(5):
    print(i)

#bucle while

x = 20

while x > 20:
    print("hola")

#listas

lista = ['Marta' 'Victor', 'Cristina', 'Noelia']

lista.append('Javi')
lista.remove('Javi')

alumno = lista.pop() #pop enseña y borra el ultimo de la lista

del lista[1] #borra la posicion de la lista que le pones

lista.insert(1, 'Diego')

print(alumno)
print(lista)