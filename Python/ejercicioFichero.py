from datetime import datetime

nombre ="Carlos"
fecha = datetime.now().strftime("%d%m%Y").lower()
nombreFichero = f"log/{fecha}{nombre}_Persona.log"

fijo = "Insert into Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) values"

insert = "personas_seq Francisco Alia 04/05/1992 Falsa 123 +34666666666" "\n"

with open(nombreFichero, "r") as fich:
    linea = fich.readline()
    while linea:
        print(linea, end="")
        linea = fich.readline()


with open(nombreFichero, "a") as f:
    f.write(insert)