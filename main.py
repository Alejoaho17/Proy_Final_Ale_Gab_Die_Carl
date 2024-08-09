from Especie import Especie
from Mision import Mision
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo

#funcion de menu, desde una lista muestra como menu las opciones con su validacion
def menu(opciones):
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    
    opcion = input("ingrese el numero de la opcion que desea elegir: ")
    while not opcion.isnumeric() or not int(opcion) in range(1, len(opciones)+1):
        opcion = input("Error, ingrese el numero de la opcion que desea elegir: ")

    opcion = int(opcion)-1

    return opcion

#Main
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

#Funcion para mostrar las distintas listas - peliculas, especies, planetas
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

#Funcion de busqueda de personajes
def buscar(personajes):
    busqueda = input("Ingrese el nombre del personaje que desea buscar")
    
    contador = 1
    for i in personajes:
        if busqueda in i.nombre:
            print(contador)
            print(i.mostrar)
            contador = contador + 1

#Funcion para mostrar cantidad de personajes nacidos en cada planeta, características de naves
def graficos():
    while True:
        opciones = ["Gráfico de cantidad de personajes nacidos en cada planeta", "Gráficos de características de naves", "Salir"]
        opcion = menu(opciones)

        
        if opcion == 0:
            pass
        elif opcion == 1:
            pass
        elif opcion == 2:
            break

#funcion para mostrar estadistica sobre naves
def estadisticas():
    pass

#Funcion para crear, modificar y visualizar una mision     
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