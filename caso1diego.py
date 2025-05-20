#Desarrolle un programa que registre la asistencia de estudiantes en tres secciones distintas de la UAM, durante cinco días de clases. Cada día se tomará asistencia a seis estudiantes por sección. El programa deberá contabilizar y mostrar el total de asistencias registradas por sección, así como el total general de la semana.

# Se inicializan las variables que contarán las asistencias por sección
asistencias_A = 0
asistencias_B = 0
asistencias_C = 0

# Se inicia un ciclo para representar los 5 días de clases
for dia in range(1, 6):
    print(f"\nDía {dia} de asistencia:")

    # ------------------ Sección A ------------------
    print("\nSección A:")
    # Se repite 6 veces, una por cada estudiante
    for estudiante in range(1, 7):
        while True:
            # Se solicita si el estudiante está presente o no
            respuesta = input(f"¿Estudiante {estudiante} está presente? (s/n): ").strip().lower()
            # Se verifica que la respuesta sea válida
            if respuesta == 's' or respuesta == 'n':
                break
            else:
                print("Entrada inválida. Escriba 's' para sí o 'n' para no.")
        # Si el estudiante está presente, se suma 1 al total de asistencias de la sección A
        if respuesta == 's':
            asistencias_A += 1

    # ------------------ Sección B ------------------
    print("\nSección B:")
    for estudiante in range(1, 7):
        while True:
            respuesta = input(f"¿Estudiante {estudiante} está presente? (s/n): ").strip().lower()
            if respuesta == 's' or respuesta == 'n':
                break
            else:
                print("Entrada inválida. Escriba 's' para sí o 'n' para no.")
        if respuesta == 's':
            asistencias_B += 1

    # ------------------ Sección C ------------------
    print("\nSección C:")
    for estudiante in range(1, 7):
        while True:
            respuesta = input(f"¿Estudiante {estudiante} está presente? (s/n): ").strip().lower()
            if respuesta == 's' or respuesta == 'n':
                break
            else:
                print("Entrada inválida. Escriba 's' para sí o 'n' para no.")
        if respuesta == 's':
            asistencias_C += 1

# Al finalizar los 5 días, se muestran los resultados de cada sección
print("\nResumen de asistencias en la semana:")
print(f"Sección A: {asistencias_A} asistencias")
print(f"Sección B: {asistencias_B} asistencias")
print(f"Sección C: {asistencias_C} asistencias")

# Se calcula el total general sumando todas las asistencias de las tres secciones
total_general = asistencias_A + asistencias_B + asistencias_C
# Se imprime el total general de asistencias
print(f"\nTotal general de asistencias: {total_general}")