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
    lista_mision = []
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
            mision(lista_peliculas, lista_especies, lista_planetas, lista_mision)
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
def mision(lista_peliculas, lista_especies, lista_planetas, lista_mision):
    while True:
        opciones = ["Construir misión", "Modificar misión", "Visualizar misión", "Salir"]
        opcion = menu(opciones)

        
        if opcion == 0:
            mision = input("Ingresa el nombre de la mision: ")

            for i, planeta in enumerate(lista_planetas):
                print(i+1, planeta.nombre)
            mision_planeta = input("Ingresa el numero del planeta que desea: ")
            cantidad_planetas = len(lista_planetas)
            while not mision_planeta.isnumeric() or not int(mision_planeta) in range(1, cantidad+1):
                mision_planeta = input("Error, Ingresa el numero del planeta que desea: ")
            
            mision_planeta = lista_planetas[int(mision_planeta)-1]



            for i, nave in enumerate(lista_naves):
                print(i+1, nave.nombre)
            mision_nave = input("Ingresa el numero del planeta que desea: ")
            cantidad_naves = len(lista_naves)
            while not mision_nave.isnumeric() or not int(mision_nave) in range(1, cantidad+1):
                mision_nave = input("Error, Ingresa el numero del planeta que desea: ")
            
            mision_nave = lista_naves[int(mision_nave)-1]


            maximo = 7
            mision_armas = []
            while len(mision_armas) <= maximo:
                for i, arma in enumerate(lista_armas):
                    print(i+1, arma.nombre)
                mision_arma = input("Ingresa el numero del arma que desea: ")
                cantidad_armas = len(lista_armas)
                while not mision_arma.isnumeric() or not int(mision_arma) in range(1, cantidad+1):
                    mision_arma = input("Error, Ingresa el numero del planeta que desea: ")
                
                mision_arma = lista_armas[int(mision_arma)-1]

                pregunta = input("Quieres agregar otra arma? 1. si 2. no")
                while not pregunta.isnumeric() or not int(pregunta) in range(1, 3):
                    pregunta = input("error, Quieres agregar otra arma? 1. si 2. no")
                
                if pregunta == "2":
                    break
            

            mision_integrantes = []
            while len(mision_integrantes) <= maximo:
                for i, integrante in enumerate(lista_integrantes):
                    print(i+1, integrante.nombre)
                mision_integrante = input("Ingresa el numero del integrante que desea: ")
                cantidad_integrantes = len(lista_integrantes)
                while not mision_integrante.isnumeric() or not int(mision_integrante) in range(1, cantidad+1):
                    mision_integrante = input("Error, Ingresa el numero del planeta que desea: ")
                
                mision_integrante = lista_integrantes[int(mision_integrante)-1]

                pregunta = input("Quieres agregar otra integrante? 1. si 2. no")
                while not pregunta.isnumeric() or not int(pregunta) in range(1, 3):
                    pregunta = input("error, Quieres agregar otra integrante? 1. si 2. no")
                
                if pregunta == "2":
                    break
            
            nueva_mision = Mision(mision, mision_planeta, mision_nave, mision_armas, mision_integrantes)
            lista_mision.append(nueva_mision)



        elif opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            break

    
    
main()