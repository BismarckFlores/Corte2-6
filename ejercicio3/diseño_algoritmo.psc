Algoritmo feria_uam
	Definir total1, total2, total3, total_dia, total_general1, total_general2, total_general3, total_general4, total_general_feria Como Real
    Definir dia, producto_1, producto_2, producto_3 Como Entero
    Definir cuadros, llaveros, pulseras Como Real
    Definir bolsas, velas, macetas Como Real
    Definir elotes, jamaica, papas_fritas Como Real
    Definir algodon, globos, manzanas Como Real
	Definir nada Como caracter
	
    Escribir "======================================================================"
    Escribir "Bienvenido al inventario de ventas de la feria estudiantil de la UAM"
    Escribir "======================================================================="
    Escribir "A continuación se registrarán las ventas de los 4 stands durante 3 días"
    Escribir "Presione ENTER para continuar"
     leer nada
	 
    // STAND 1 - Arte y Creatividad Estudiantil
    Escribir "Stand 1: Arte y Creatividad Estudiantil"
    Escribir "Ingrese el precio de los cuadros (C$): "
    Leer cuadros
    Escribir "Ingrese el precio de los llaveros (C$): "
    Leer llaveros
    Escribir "Ingrese el precio de las pulseras (C$): "
    Leer pulseras
    total_general1 <- 0
	
    Para dia <- 1 Hasta 3 Con Paso 1
        Escribir "Día ", dia
        Escribir "¿Cuántas veces vendió el primer producto? "
        Leer producto_1
        total1 <- producto_1 * cuadros
		
        Escribir "¿Cuántas veces vendió el segundo producto? "
        Leer producto_2
        total2 <- producto_2 * llaveros
		
        Escribir "¿Cuántas veces vendió el tercer producto? "
        Leer producto_3
        total3 <- producto_3 * pulseras
		
        total_dia <- total1 + total2 + total3
        total_general1 <- total_general1 + total_dia
		
        Escribir "Total del día ", dia, ": ", total_dia, " C$"
    FinPara
	
    // STAND 2 - Eco-UAM
    Escribir "Stand 2: Eco-UAM"
    Escribir "Precio de bolsas reutilizables: "
    Leer bolsas
    Escribir "Precio de velas aromáticas: "
    Leer velas
    Escribir "Precio de macetas: "
    Leer macetas
    total_general2 <- 0
	
    Para dia <- 1 Hasta 3 Con Paso 1
        Escribir "Día ", dia
        Escribir "¿Cuántas veces vendió el primer producto? "
        Leer producto_1
        total1 <- producto_1 * bolsas
		
        Escribir "¿Cuántas veces vendió el segundo producto? "
        Leer producto_2
        total2 <- producto_2 * velas
		
        Escribir "¿Cuántas veces vendió el tercer producto? "
        Leer producto_3
        total3 <- producto_3 * macetas
		
        total_dia <- total1 + total2 + total3
        total_general2 <- total_general2 + total_dia
		
        Escribir "Total del día ", dia, ": ", total_dia, " C$"
    FinPara
	
    // STAND 3 - Sabores Callejeros
    Escribir "Stand 3: Sabores Callejeros"
    Escribir "Precio de elotes: "
    Leer elotes
    Escribir "Precio de fresco de jamaica: "
    Leer jamaica
    Escribir "Precio de papas fritas: "
    Leer papas_fritas
    total_general3 <- 0
	
    Para dia <- 1 Hasta 3 Con Paso 1
        Escribir "Día ", dia
        Escribir "¿Cuántas veces vendió el primer producto? "
        Leer producto_1
        total1 <- producto_1 * elotes
		
        Escribir "¿Cuántas veces vendió el segundo producto? "
        Leer producto_2
        total2 <- producto_2 * jamaica
		
        Escribir "¿Cuántas veces vendió el tercer producto? "
        Leer producto_3
        total3 <- producto_3 * papas_fritas
		
        total_dia <- total1 + total2 + total3
        total_general3 <- total_general3 + total_dia
		
        Escribir "Total del día ", dia, ": ", total_dia, " C$"
    FinPara
	
    // STAND 4 - Dulce de Feria
    Escribir "Stand 4: Dulce de Feria"
    Escribir "Precio de algodón de azúcar: "
    Leer algodon
    Escribir "Precio de globos: "
    Leer globos
    Escribir "Precio de manzanas caramelizadas: "
    Leer manzanas
    total_general4 <- 0
	
    Para dia <- 1 Hasta 3 Con Paso 1
        Escribir "Día ", dia
        Escribir "¿Cuántas veces vendió el primer producto? "
        Leer producto_1
        total1 <- producto_1 * algodon
		
        Escribir "¿Cuántas veces vendió el segundo producto? "
        Leer producto_2
        total2 <- producto_2 * globos
		
        Escribir "¿Cuántas veces vendió el tercer producto? "
        Leer producto_3
        total3 <- producto_3 * manzanas
		
        total_dia <- total1 + total2 + total3
        total_general4 <- total_general4 + total_dia
		
        Escribir "Total del día ", dia, ": ", total_dia, " C$"
    FinPara
	
    // RESUMEN FINAL
    Escribir "==============================================="
    Escribir "Resumen total por stand:"
    Escribir "Arte y Creatividad Estudiantil: ", total_general1, " C$"
    Escribir "Eco-UAM: ", total_general2, " C$"
    Escribir "Sabores Callejeros: ", total_general3, " C$"
    Escribir "Dulce de Feria: ", total_general4, " C$"
	
    total_general_feria <- total_general1 + total_general2 + total_general3 + total_general4
	
    Escribir "==============================================="
    Escribir "TOTAL GENERAL DE LA FERIA: ", total_general_feria, " C$"
	
FinAlgoritmo
