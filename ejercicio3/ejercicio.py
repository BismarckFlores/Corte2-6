""""Cree un programa que permita llevar un registro de ventas en una feria estudiantil organizada
por la UAM. La feria se desarrollará durante tres días, con cuatro stands por día. Cada stand
ofrecerá tres productos distintos. El sistema deberá permitir ingresar el monto de venta por
producto y mostrar un resumen por stand, por día, y un total general de la feria.
"""
def stand_1(): #Funcion para el stand 1/Iniciamos a hacer un molde para cada stand que le siga su misma estructura
                
    print("\nArte y Creatividad Estudiantil") #Iniciamos con el nombre del stand
    cuadros=float(input("Que precio tienen los cuadros en acrílico pequeños (C$): ")) #Pedimos los 3 productos requeridos
    llaveros=float(input("Que precio tienen los llaveros (C$): ")) #El usuario le ingresa el precio
    pulseras=float(input("Que precio tienen las pulseras tejidas a mano (C$): "))
    dia=0 #Hacemos un contador para cada día, que inicie 1 por 1 en secuencia al for 
    total_general1=0 #Hacemos para llevar los totales ganados de cada día 
    for _ in range (0,3): #iniciamos de día 1 a día 3
        dia+=1
        print(f"\nDía {dia}") 
        
        producto_1=int(input("¿Cuantas veces vendio el primer producto? ")) #Pedimos la cantidad de productos vendidos
        total_1=producto_1 * cuadros #Calculamos las veces que se vendio por lo que vale
        print(f"{total_1} C$") #Imprimimos el total de lo vendido por día
        producto_2=int(input("¿Cuantas veces vendio el segundo producto? "))
        total_2=producto_2 * llaveros 
        print(f"{total_2} C$")
        producto_3=int(input("¿Cuantas veces vendio el tercer producto? "))
        total_3=producto_3 * pulseras
        print(f"{total_3} C$")
        total_dia=total_1+total_2+total_3 #Una vez con los totales de cada producto, calculamos el total del día en si
        print(f"Total del día {total_dia:.2f} C$")

        total_general1 += total_dia #Suma el total de cada día (3) para llevar el total general de la feria
    return total_general1 #Pedimos que nos devuelva el valor para poder imprimirlo mas adelante

def stand_2(): #Sigue la misma estructura del stand 1
    print("\nEco-UAM")
    bolsas=float(input("Que precio tienen las bolsas con diseño reutilizables (C$): "))
    velas=float(input("Que precio tienen las velas aromaticas (C$): "))
    macetas=float(input("Que precio tienen las macetas con plantas pequeñas (C$): "))
    dia=0
    total_general2=0
    for _ in range (0,3):
        dia+=1
        print(f"\nDía {dia}")
        
        producto_1=int(input("¿Cuantas veces vendio el primer producto? "))
        total_1=producto_1 * bolsas
        print(f"{total_1} C$")
        producto_2=int(input("¿Cuantas veces vendio el segundo producto? "))
        total_2=producto_2 * velas
        print(f"{total_2} C$")
        producto_3=int(input("¿Cuantas veces vendio el tercer producto? "))
        total_3=producto_3 * macetas
        print(f"{total_3} C$")
        total_dia=total_1+total_2+total_3
        print(f"Total del día {total_dia:.2f} C$")

        total_general2 += total_dia
    return total_general2


def stand_3(): #Sigue la misma estructura del stand 1
    print("\nSabores Callejeros")
    elotes=float(input("Que precio tienen los elotes (C$): "))
    jamaica=float(input("Que precio tiene el fresco de jamaica (C$): "))
    papas_fritas=float(input("Que precio tienen las papitas fritas (C$): "))
    dia=0
    total_general3=0
    for _ in range (0,3):
        dia+=1
        print(f"\nDía {dia}")
        
        producto_1=int(input("¿Cuantas veces vendio el primer producto? "))
        total_1=producto_1 * elotes
        print(f"{total_1} C$")
        producto_2=int(input("¿Cuantas veces vendio el segundo producto? "))
        total_2=producto_2 * jamaica
        print(f"{total_2} C$")
        producto_3=int(input("¿Cuantas veces vendio el tercer producto? "))
        total_3=producto_3 * papas_fritas
        print(f"{total_3} C$")
        total_dia=total_1+total_2+total_3
        print(f"Total del día {total_dia:.2f} C$")

        total_general3 += total_dia
    return total_general3

def stand_4(): #Sigue la misma estructura del stand 1
    print("\nDulce de Feria")
    algodon=float(input("Que precio tienen los algodones (C$): "))
    globos=float(input("Que precio tienen los globos (C$): "))
    manzanas=float(input("Que precio tienen las manzanas caramelizadas (C$): "))
    dia=0
    total_general4=0

    for _ in range (0,3):
        dia+=1
        print(f"\nDía {dia}")
        
        producto_1=int(input("¿Cuantas veces vendio el primer producto? "))
        total_1=producto_1 * algodon
        print(f"{total_1} C$")
        producto_2=int(input("¿Cuantas veces vendio el segundo producto? "))
        total_2=producto_2 * globos
        print(f"{total_2} C$")
        producto_3=int(input("¿Cuantas veces vendio el tercer producto? "))
        total_3=producto_3 * manzanas
        print(f"{total_3} C$")
        total_dia=total_1+total_2+total_3
        print(f"Total del día {total_dia:.2f} C$")

        total_general4 += total_dia
    return total_general4


def main (): #Hacemos una funcion llamada main para ordenar mejor lo datos y el programa
    print("="*70) #Hacemos una introducción o bienvenida al usuario
    print("Bienvenido al inventario de ventas de la feria estudiantil de la UAM")
    print("="*70)
    print("A continuación, se mostraran los 4 stands de la feria estudiantil de estos 3 días")
    print("\nPresione enter") #Presionar enter para seguir con el programa 
    print(input(""))    

    total_general1=stand_1() #Llamamos a la funcion stand_1 y guardamos el resultado en total_general1 gracias al return de antes
    total_general2=stand_2() #Lo mismo en las demas
    total_general3=stand_3()
    total_general4=stand_4()


    print("="*50) 
    print("Resumen del total ganado en los 3 días por cada stand es: ") #Creamos el resumen de los 4 stand en los 3 dias que vendieron
    print("="*50)

    
    print(f"Arte y creatividad estudiantil:  {total_general1:.2f} C$ ") 
    print(f"Eco UAM:                         {total_general2:.2f} C$ ")
    print(f"Sabores callejeros:              {total_general3:.2f} C$ ")
    print(f"Diversion de Feria:              {total_general4:.2f} C$ ")
   
    total_general_feria= total_general1+total_general2+total_general3+total_general4 #Hacemos el total general ganado de la feria durante los 3 dias
    print(f"\nEl total ganado general de la feria es: {total_general_feria:.2f} ")
main()


















        