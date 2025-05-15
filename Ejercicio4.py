"""
Programa: Monitoreo del Consumo Energético en Edificios Universitarios
Descripción:
    Este programa permite registrar y calcular el consumo energético en kWh de cuatro edificios
    a lo largo de una semana. Por cada edificio, se registra el consumo diario en tres turnos:
    matutino, vespertino y nocturno. Al finalizar, se presentan los totales y promedios de consumo.
"""

# Inicialización de variables
edificios = 4                                                                           # Número de edificios
dias = 7                                                                                # Número de días de la semana
turnos = 3                                                                              # Número de turnos por día

# Bucle principal que repite por cada edificio
for edificio in range(edificios):
    print(f"\nRegistro de consumo para el Edificio #{edificio + 1}")
    total_edificio = 0                                                                  # Acumulador del consumo total semanal por edificio

    # Bucle interno que recorre cada día de la semana
    for dia in range(dias):
        total_dia = 0                                                                   # Acumulador del consumo total diario
        
        # Mostrar el nombre del día según el índice
        if dia == 0:
            print("\nConsumo del Lunes")
        elif dia == 1:
            print("\nConsumo del martes")
        elif dia == 2:
            print("\nConsumo del Miércoles")
        elif dia == 3:
            print("\nConsumo del Jueves")
        elif dia == 4:
            print("\nConsumo del Viernes")
        elif dia == 5:
            print("\nConsumo del Sabado")
        else:
            print("\nConsumo del Domingo")

        # Bucle que recorre los turnos del día
        for turno in range(turnos):
            # Mostrar el turno actual
            if turno == 0:
                print("\nTurno Matutino")
            elif turno == 1:
                print("\nTurno Vespertino")
            else:
                print("\nTurno Nocturno")

            # Solicitar al usuario el consumo de kWh validando entrada correcta
            while True:
                try:
                    consumo = float(input("Ingrese el consumo de kWh: "))
                    if consumo >= 0:
                        total_dia += consumo                                            # Acumular consumo del turno al día
                        break
                    else:
                        print("Error. El consumo no puede ser negativo.")
                        input("Presione enter para continuar...")
                except ValueError:
                    print("Error. Ingrese un valor numérico válido.")
                    input("Presione enter para continuar...")

        # Mostrar el total de consumo en el día actual
        print(f"\nTotal de consumo en el dia: {total_dia}")
        input("Presione enter para continuar...")
        total_edificio += total_dia                                                     # Acumular consumo diario al total del edificio

    promedio_edificio = total_edificio / dias                                           # Calcular promedio semanal (total semanal dividido entre días)
    
    # Mostrar resumen del consumo por edificio
    print(f"\nEl consumo total del edificio #{edificio + 1}: {total_edificio}kWh")
    print(f"\nPromedio de consumo semanal: {promedio_edificio:.2f}kWh")
    input("Presione enter para continuar...")

    # Guardar resultados según el número de edificio actual
    if edificio == 0:
        total_edificio1 = total_edificio
        promedio_edificio1 = promedio_edificio
    elif edificio == 1:
        total_edificio2 = total_edificio
        promedio_edificio2 = promedio_edificio
    elif edificio == 2:
        total_edificio3 = total_edificio
        promedio_edificio3 = promedio_edificio
    else:
        total_edificio4 = total_edificio
        promedio_edificio4 = promedio_edificio

# Mostrar resumen general al finalizar los registros
print("\n-------------------------------------------")
print("RESUMEN DE CONSUMOS POR EDIFICIO")
print("-------------------------------------------")
print(f"Edificio 1 - Total semanal: {total_edificio1} kWh - Promedio diario: {promedio_edificio1:.2f} kWh")
print(f"Edificio 2 - Total semanal: {total_edificio2} kWh - Promedio diario: {promedio_edificio2:.2f} kWh")
print(f"Edificio 3 - Total semanal: {total_edificio3} kWh - Promedio diario: {promedio_edificio3:.2f} kWh")
print(f"Edificio 4 - Total semanal: {total_edificio4} kWh - Promedio diario: {promedio_edificio4:.2f} kWh")