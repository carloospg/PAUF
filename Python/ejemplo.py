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

