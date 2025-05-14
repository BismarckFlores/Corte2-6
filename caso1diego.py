# Contadores de asistencia por sección
asistencias_A = 0
asistencias_B = 0
asistencias_C = 0

# 5 días de clases
for dia in range(1, 6):
    print(f"Día {dia} de asistencia: ")

    # Sección A
    print("Sección A: ")
    for estudiante in range(1, 7):
        while True:
            respuesta = input(f"¿Estudiante {estudiante} está presente? (s/n): ").strip().lower()
            if respuesta in ["s", "n"]:
                break
            else:
                print("Entrada inválida. Escriba 's' para sí o 'n' para no.")
        if respuesta == "s":
            asistencias_A += 1

    # Sección B
    print("Sección B: ")
    for estudiante in range(1, 7):
        while True:
            respuesta = input(f"¿Estudiante {estudiante} está presente? (s/n): ").strip().lower()
            if respuesta in ["s", "n"]:
                break
            else:
                print("Entrada inválida. Escriba 's' para sí o 'n' para no.")
        if respuesta == "s":
            asistencias_B += 1

    # Sección C
    print("Sección C: ")
    for estudiante in range(1, 7):
        while True:
            respuesta = input(f"¿Estudiante {estudiante} está presente? (s/n): ").strip().lower()
            if respuesta in ["s", "n"]:
                break
            else:
                print("Entrada inválida. Escriba 's' para sí o 'n' para no.")
        if respuesta == "s":
            asistencias_C += 1

# Mostrar resultados
print("Resumen de asistencias en la semana: ")
print(f"Sección A: {asistencias_A} asistencias")
print(f"Sección B: {asistencias_B} asistencias")
print(f"Sección C: {asistencias_C} asistencias")

total_general = asistencias_A + asistencias_B + asistencias_C
print(f"Total general de asistencias: {total_general}")
