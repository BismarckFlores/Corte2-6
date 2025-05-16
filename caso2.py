
# Este programa simula el estado de dos laboratorios de computación
import random

# Definimos las constantes

computadoras_en_fila=4
computadoras_en_columna=5

for lab in range(2):
    ocupadas=0
    libres=0

    # Simulamos el estado de las computadoras en un laboratorio
    for i in range(computadoras_en_columna):
        for j in range(computadoras_en_fila):
            if random.randint(0,1)==0:
                libres+=1
            else:
                ocupadas+=1
    # Almacenar los resultados en variables diferentes para cada laboratorio
    # Mostrar el estado de cada laboratorio
    if lab==0:
        libres_1=libres
        ocupadas_1=ocupadas 
    else:
        libres_2=libres
        ocupadas_2=ocupadas

print(f"Laboratorio 1 - Ocupadas: {ocupadas_1}, Libres: {libres_1}")
print(f"Laboratorio 2 - Ocupadas: {ocupadas_2}, Libres: {libres_2}")