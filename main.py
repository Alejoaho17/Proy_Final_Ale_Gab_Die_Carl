from Especie import Especie
from Mision import Mision
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo
from Pelicula import Pelicula
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
#obtener info de api
def api(lista_peliculas, lista_especies, lista_planetas, lista_personajes):
    '''page = "https://www.swapi.tech/api/people"

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
    
    


    # URL del endpoint de películas
    url = "https://www.swapi.tech/api/films"

    # Obtener los datos de las películas
    response = requests.get(url)
    data = response.json()

    # Iterar sobre cada película y obtener su información detallada
    for pelicula in data["result"]:
        # Imprimir la estructura de cada película para identificar la clave correcta
        #print(pelicula)
        pelicula = pelicula["properties"]
        # Puedes crear una instancia de una clase Pelicula si tienes una clase definida
        nuevo_pelicula = Pelicula(pelicula["title"], pelicula["episode_id"], pelicula["release_date"], pelicula["opening_crawl"],  pelicula["director"])
        lista_peliculas.append(nuevo_pelicula)
    


    page = "https://www.swapi.tech/api/species"

    # Mientras haya una página siguiente, seguir obteniendo personajes
    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada personaje y obtener su información detallada
        for especie in results:
            especie_url = especie["url"]
            especie = requests.get(especie_url).json()["result"]["properties"]
            #print(especie)  
            # Imprimir la información del personaje
            nuevo_especie = Especie(especie["name"], especie["homeworld"], especie["classification"], especie['homeworld'], especie["language"], especie["people"], [])
            lista_especies.append(nuevo_especie)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]
    '''
    
    page = "https://www.swapi.tech/api/planets"

    # Mientras haya una página siguiente, seguir obteniendo personajes
    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada personaje y obtener su información detallada
        for planeta in results:
            planeta_url = planeta["url"]
            planeta = requests.get(planeta_url).json()["result"]["properties"]
            print(planeta)  
            # Imprimir la información del personaje
            nuevo_planeta = Planeta(planeta["name"], planeta["orbital_period"], planeta["rotation_period"], planeta["population"], planeta["climate"], [], [])
            lista_planetas.append(nuevo_planeta)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]
    
    


    

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