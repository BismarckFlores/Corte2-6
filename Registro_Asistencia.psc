Proceso Registro_Asistencia
	
	Definir asistencias_A, asistencias_B, asistencias_C, total_general Como Entero
	Definir dia, estudiante Como Entero
	Definir respuesta Como Caracter
	
	asistencias_A <- 0
	asistencias_B <- 0
	asistencias_C <- 0
	
	Para dia <- 1 Hasta 5 Con Paso 1
		Escribir ""
		Escribir "Dia ", dia, " de asistencia"
		
		// Seccion A
		Escribir "Seccion A:"
		Para estudiante <- 1 Hasta 6 Con Paso 1
			Repetir
				Escribir "Estudiante ", estudiante, " está presente? (s/n): "
				Leer respuesta
			Hasta Que respuesta = "s" O respuesta = "n"
			Si respuesta = "s" Entonces
				asistencias_A <- asistencias_A + 1
			FinSi
		FinPara
		
		// Seccion B
		Escribir "Seccion B:"
		Para estudiante <- 1 Hasta 6 Con Paso 1
			Repetir
				Escribir "Estudiante ", estudiante, " est� presente? (s/n): "
				Leer respuesta
			Hasta Que respuesta = "s" O respuesta = "n"
			Si respuesta = "s" Entonces
				asistencias_B <- asistencias_B + 1
			FinSi
		FinPara
		
		// Seccion C
		Escribir "Seccin C:"
		Para estudiante <- 1 Hasta 6 Con Paso 1
			Repetir
				Escribir "Estudiante ", estudiante, " está presente? (s/n): "
				Leer respuesta
			Hasta Que respuesta = "s" O respuesta = "n"
			Si respuesta = "s" Entonces
				asistencias_C <- asistencias_C + 1
			FinSi
		FinPara
		
	FinPara
	
	// Mostrar resultados
	Escribir ""
	Escribir "Resumen de asistencias en la semana:"
	Escribir "Seccion A: ", asistencias_A, " asistencias"
	Escribir "Seccion B: ", asistencias_B, " asistencias"
	Escribir "Seccion C: ", asistencias_C, " asistencias"
	
	total_general <- asistencias_A + asistencias_B + asistencias_C
	Escribir "Total general de asistencias: ", total_general

FinProceso
