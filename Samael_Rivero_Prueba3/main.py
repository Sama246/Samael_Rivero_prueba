import os
import asignar_montos_aleatorios 
import globales

def menu_principal():
    os.system("cls")
    print("1. Asignar Montos Aleatorios")
    print("2. Ver Estadísticas")
    print("3. Salir")

    opcion = globales.seleccionar_opcion(3)

    if opcion == 1:
        asignar_montos_aleatorios.montos_aleatorios()
    elif opcion == 2:
        print("2. Ver Estadisticas")
    elif opcion == 3:
        print("3. Salir")
        return
    
    input()

if __name__ == "__main__":
    menu_principal()