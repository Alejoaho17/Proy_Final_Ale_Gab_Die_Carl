from Especie import Especie
from Mision import Mision
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo
import requests
import json

#funcion de menu, desde una lista muestra como menu las opciones con su validacion
def menu(opciones):
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    
    opcion = input("ingrese el numero de la opcion que desea elegir: ")
    while not opcion.isnumeric() or not int(opcion) in range(1, len(opciones)+1):
        opcion = input("Error, ingrese el numero de la opcion que desea elegir: ")

    opcion = int(opcion)-1

    return opcion
def api(lista_peliculas, lista_especies, lista_planetas, lista_personajes):
    page = "https://www.swapi.tech/api/people"

    # Mientras haya una página siguiente, seguir obteniendo personajes
    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada personaje y obtener su información detallada
        for character in results:
            character_url = character["url"]
            character = requests.get(character_url).json()["result"]["properties"]
            #print(character)  
            # Imprimir la información del personaje
            nuevo_personaje = Personaje(character["name"], character["homeworld"], [], character['gender'], "", [], [])
            lista_personajes.append(nuevo_personaje)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]
    

    


#obtener info de api

#Main
def main():
    lista_peliculas = []
    lista_especies = []
    lista_planetas = []
    lista_personajes = []
    api(lista_peliculas, lista_especies, lista_planetas, lista_personajes)

    while True:
        opciones = ["Ver listas", "Buscar personaje", "Graficos", "Estadisticas", "Mision", "Salir"]
        opcion = menu(opciones)
        
        if opcion == 0:
            listas(lista_peliculas, lista_especies, lista_planetas)
        elif opcion == 1:
            buscar(lista_personajes)
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
def listas(lista_peliculas, lista_especies, lista_planetas):
    while True:
        opciones = ["Lista de Películas de la saga", "Lista de las especies de seres vivos de la saga", "Lista de planetas", "Salir"]
        opcion = menu(opciones)

        
        if opcion == 0:
            for i, pelicula in enumerate(lista_peliculas):
                print(i+1)
                print(pelicula.__str__())

        elif opcion == 1:
            for i, especie in enumerate(lista_especies):
                print(i+1)
                print(especie.__str__())

        elif opcion == 2:
            for i, planeta in enumerate(lista_planetas):
                print(i+1)
                print(planeta.__str__())
        elif opcion == 3:
            break

#Funcion de busqueda de personajes
def buscar(personajes):
    busqueda = input("Ingrese el nombre del personaje que desea buscar: ")
    
    contador = 1
    for i in personajes:
        if busqueda.upper() in i.nombre.upper():
            print("")
            print('----'+contador+'----')
            print(i.__str__())
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