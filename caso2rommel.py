#Implemente un programa que simule el estado de uso de computadoras en dos laboratorios del campus. Cada laboratorio contiene cinco filas de cuatro computadoras. Por cada computadora se debe registrar si está ocupada o libre (puede ingresarse manualmente o simularse con valores aleatorios). Al finalizar, el programa debe mostrar el resumen de computadoras ocupadas y libres por laboratorio.
# Definimos las constantes
import random

# Definir tamaño del laboratorio
FILAS = 5
COLUMNAS = 4

def generar_laboratorio():
    """Genera un laboratorio con computadoras ocupadas o libres aleatoriamente."""
    return [[random.choice(["Ocupada", "Libre"]) for _ in range(COLUMNAS)] for _ in range(FILAS)]

def mostrar_laboratorio(lab, nombre):
    """Muestra el estado de cada computadora en el laboratorio."""
    print(f"\nEstado del {nombre}:")
    for fila in lab:
        print(" | ".join(fila))

def contar_estados(lab):
    """Cuenta cuántas computadoras están ocupadas y cuántas libres."""
    ocupadas = sum(fila.count("Ocupada") for fila in lab)
    libres = sum(fila.count("Libre") for fila in lab)
    return ocupadas, libres

# Generar los dos laboratorios
laboratorio_1 = generar_laboratorio()
laboratorio_2 = generar_laboratorio()

# Mostrar el estado de los laboratorios
mostrar_laboratorio(laboratorio_1, "Laboratorio 1")
mostrar_laboratorio(laboratorio_2, "Laboratorio 2")

# Contar computadoras ocupadas y libres
ocupadas_1, libres_1 = contar_estados(laboratorio_1)
ocupadas_2, libres_2 = contar_estados(laboratorio_2)

# Mostrar resumen
print("\nResumen:")
print(f"Laboratorio 1 - Ocupadas: {ocupadas_1}, Libres: {libres_1}")
print(f"Laboratorio 2 - Ocupadas: {ocupadas_2}, Libres: {libres_2}")


