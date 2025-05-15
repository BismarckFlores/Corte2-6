// Ejercicio 4: Monitoreo del consumo energético
// Desarrolle un programa que registre el consumo energético de cuatro edificios del campus
// universitario a lo largo de una semana. Por cada día se ingresarán los kilovatios consumidos en
// tres turnos: mañana, tarde y noche. El programa debe calcular el consumo total por edificio y
// generar el promedio semanal correspondiente.

Proceso Monitoreo_del_consumo_energetico
	// Declaracion de variables
    Definir edificios, dias, turnos Como Entero;
    Definir edificio, dia, turno Como Entero;
    Definir consumo, total_dia, total_edificio, promedio Como Real;
    Definir pausa Como Caracter;
    Definir total_edificio1, total_edificio2, total_edificio3, total_edificio4 Como Real;
    Definir promedio_edificio1, promedio_edificio2, promedio_edificio3, promedio_edificio4 Como Real;
	
    edificios <- 4;															// Número de edificios
    dias <- 7;																// Número de días de la semana
    turnos <- 3;																// Número de turnos por día
	
	// Bucle principal que repite por cada edificio
    Para edificio <- 1 Hasta edificios Hacer
        Escribir "Registro de consumo para el Edificio #", edificio;
        total_edificio <- 0;													// Acumulador del consumo total semanal por edificio
		
        Para dia <- 1 Hasta dias Hacer
            total_dia <- 0;													// Acumulador del consumo total diario
			
			// Mostrar el nombre del día según el índice
            Segun dia Hacer
                1:
                    Escribir "Consumo del Lunes";
                2:
                    Escribir "Consumo del Martes";
                3:
                    Escribir "Consumo del Miércoles";
                4:
                    Escribir "Consumo del Jueves";
                5:
                    Escribir "Consumo del Viernes";
                6:
                    Escribir "Consumo del Sábado";
                7:
                    Escribir "Consumo del Domingo";
            FinSegun
			
			// Bucle que recorre los turnos del día
            Para turno <- 1 Hasta turnos Hacer
				# Mostrar el turno actual
                Si turno = 1 Entonces
                    Escribir "Turno Matutino";
                Sino
                    Si turno = 2 Entonces
                        Escribir "Turno Vespertino";
                    Sino
                        Escribir "Turno Nocturno";
                    FinSi
                FinSi
				
				// Solicitar al usuario el consumo de kWh
                Repetir
                    Escribir "Ingrese el consumo de kWh: ";
                    Leer consumo;
                    Si consumo >= 0 Entonces
                        total_dia <- total_dia + consumo;					// Acumular consumo del turno al día
                    Sino
                        Escribir "Error. El consumo no puede ser negativo.";
                        Escribir "Presione enter para continuar...";
                        Leer pausa;
                    FinSi
                Hasta Que consumo >= 0
            FinPara
			
            Escribir "Total de consumo en el día: ", total_dia;
            Escribir "Presione enter para continuar...";
            Leer pausa;
            total_edificio <- total_edificio + total_dia;
        FinPara;
		
		promedio <- total_edificio / 7;
		
        Escribir "El consumo total del edificio #", edificio, ": ", total_edificio, " kWh";
        Escribir "Promedio de consumo semanal: ", promedio, " kWh";
        Escribir "Presione enter para continuar...";
        Leer pausa;
		
        Si edificio = 1 Entonces
            total_edificio1 <- total_edificio;
            promedio_edificio1 <- promedio;
        Sino
            Si edificio = 2 Entonces
                total_edificio2 <- total_edificio;
                promedio_edificio2 <- promedio;
            Sino
                Si edificio = 3 Entonces
                    total_edificio3 <- total_edificio;
                    promedio_edificio3 <- promedio;
                Sino
                    total_edificio4 <- total_edificio;
                    promedio_edificio4 <- promedio;
                FinSi
            FinSi
        FinSi
    FinPara
	
    Escribir "-------------------------------------------";
    Escribir "RESUMEN DE CONSUMOS POR EDIFICIO";
    Escribir "-------------------------------------------";
    Escribir "Edificio 1 - Total semanal: ", total_edificio1, " kWh - Promedio diario: ", promedio_edificio1, " kWh";
    Escribir "Edificio 2 - Total semanal: ", total_edificio2, " kWh - Promedio diario: ", promedio_edificio2, " kWh";
    Escribir "Edificio 3 - Total semanal: ", total_edificio3, " kWh - Promedio diario: ", promedio_edificio3, " kWh";
    Escribir "Edificio 4 - Total semanal: ", total_edificio4, " kWh - Promedio diario: ", promedio_edificio4, " kWh";
	Escribir "Presione enter para continuar...";
	leer pausa;
FinProceso