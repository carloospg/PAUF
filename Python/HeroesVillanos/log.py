import logging
from datetime import datetime
import os

# Crear carpeta de logs si no existe
if not os.path.exists("log"):
    os.makedirs("log")

# Nombre del fichero con fecha
fecha = datetime.now().strftime("%d%m%Y")
nombre_fichero = f"log/{fecha}_HEROESYVILLANOS.log"

# Configuración del logging
logging.basicConfig(
    filename=nombre_fichero,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Función opcional para loggear mensajes
def info(mensaje):
    logging.info(mensaje)

def error(mensaje):
    logging.error(mensaje)