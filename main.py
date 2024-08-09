from Especie import Especie
from Mision import Mision
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo

def menu(opciones):
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    
    opcion = input("ingrese el numero de la opcion que desea elegir: ")
    while not opcion.isnumeric() or not int(opcion) in range(1, len(opciones)+1):
        opcion = input("Error, ingrese el numero de la opcion que desea elegir: ")

    opcion = int(opcion)-1

    return opcion

def main():
    while True:
        opciones = ["Ver listas", "Buscar personaje", "Graficos", "Estadisticas", "Mision", "Salir"]
        opcion = menu(opciones)
        
        if opcion == 0:
            listas()
        elif opcion == 1:
            buscar()
        elif opcion == 2:
            graficos()
        elif opcion == 3:
            estadisticas()
        elif opcion == 4:
            mision()
        elif opcion == 5:
            print("Hasta luego")
            break

def listas():
    while True:
        opciones = ["Lista de Películas de la saga", "Lista de las especies de seres vivos de la saga", "Lista de planetas", "Salir"]
        opcion = menu(opciones)

        
        if opcion == 0:
            pass
        elif opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            break

def buscar():
    pass

def graficos():
    while True:
        opciones = ["Gráfico de cantidad de personajes nacidos en cada planeta", "Gráficos de características de naves", "Graficos", "Mision", "Salir"]
        opcion = menu(opciones)

        
        if opcion == 0:
            pass
        elif opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            break

def estadisticas():
    pass
    
def mision():
    while True:
        opciones = ["Construir misión", "Modificar misión", "Visualizar misión", "Salir"]
        opcion = menu(opciones)

        
        if opcion == 0:
            pass
        elif opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            break

    
    
main()