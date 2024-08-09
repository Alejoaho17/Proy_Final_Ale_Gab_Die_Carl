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
        opciones = ["Ver listas", "Buscar personaje", "Graficos", "Mision", "Salir"]
        opcion = menu(opciones)
        
        if opcion == 0:
            listas()
        elif opcion == 1:
            buscar()
        elif opcion == 2:
            graficos()
        elif opcion == 3:
            mision()
        elif opcion == 4:
            print("Hasta luego")
            break

def listas():
    pass

def buscar():
    pass

def graficos():
    pass

def mision():
    pass

    
    
main()