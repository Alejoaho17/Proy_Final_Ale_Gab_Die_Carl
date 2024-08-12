from Especie import Especie
from Mision import Mision
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo
from Pelicula import Pelicula
import requests
import json
import csv

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
            #print(planeta)  
            # Imprimir la información del personaje
            nuevo_planeta = Planeta(planeta["name"], planeta["orbital_period"], planeta["rotation_period"], planeta["population"], planeta["climate"], [], [])
            lista_planetas.append(nuevo_planeta)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]'''
    
    
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
#Recorre la lista de peliculas, especies y planetas y las imprime y las enumera
def listas(lista_peliculas, lista_especies, lista_planetas):
    while True:
        opciones = ["Lista de Películas de la saga", "Lista de las especies de seres vivos de la saga", "Lista de planetas", "Salir"]
        opcion = menu(opciones)

        #Lista de Películas de la saga
        if opcion == 0:
            for i, pelicula in enumerate(lista_peliculas):
                print(i+1)
                print(pelicula.__str__())

        #Lista de las especies de seres vivos de la saga
        elif opcion == 1:
            for i, especie in enumerate(lista_especies):
                print(i+1)
                print(especie.__str__())
        
        #Lista de planetas
        elif opcion == 2:
            for i, planeta in enumerate(lista_planetas):
                print(i+1)
                print(planeta.__str__())
        
        elif opcion == 3:
            break

#Funcion de busqueda de personajes
def buscar(personajes):
    busqueda = input("Ingrese el nombre del personaje que desea buscar: ")
    
    #Recorre la lista de personajes, si el nombre del objecto contiene el string que se busca muestra el objecto
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
            grafico_personajes()
        elif opcion == 1:
            grafico_naves()
        elif opcion == 2:
            break


def grafico_personajes():
    planetas = []
    planetas_personajes = []
    # Abre el archivo CSV
    with open('starwars/csv/planets.csv','r') as file:
        # Crea un lector de CSV
        reader = csv.reader(file)
        
        # Recorre cada fila en el archivo CSV
        for row in reader:
            if row[0] != "id":
                planetas.append([row[1], 0])
    
    with open('starwars/csv/characters.csv','r') as file:
        # Crea un lector de CSV
        reader = csv.reader(file)
        
        # Recorre cada fila en el archivo CSV
        for row in reader:
            if row[0] != "id":
                planetas_personajes.append(row[10])

        
    for planeta in planetas:
        for p in planetas_personajes:
            if planeta[0].upper() == p.upper():
                planeta[1] += 1

    print(planetas)


def grafico_naves():
    naves = []
    with open('starwars/csv/starships.csv','r') as file:
        # Crea un lector de CSV
        reader = csv.reader(file)
        
        # Recorre cada fila en el archivo CSV
        for row in reader:
            if row[0] != "id":
                naves.append([row[1], row[5], row[9], row[11], row[12]])

    print(naves)
    while True:
        print("Seleccione la categoria que desea ver en la grafica de las naves: ")
        opciones = ["Longitud de la nave", "Capacidad de carga", "Clasificación de hiperimpulsor", "MGLT (Modern Galactic Light Time)", "salir"]
        opcion = menu(opciones)
            
        if opcion == 0:
            pass
        elif opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 3:
            break

#funcion para mostrar estadistica sobre naves
def estadisticas():
    naves = []
    with open('starwars/csv/starships.csv','r') as file:
        # Crea un lector de CSV
        reader = csv.reader(file)
        
        # Recorre cada fila en el archivo CSV
        for row in reader:
            if row[0] != "id":
                naves.append([row[11], row[12], row[6], row[4]])

    dicc_hiperimpulsor = {
        'titulo': 'Hiperimpulsor',
        'promedio': 0,
        'moda': 0,
        'max': 0,
        'min': 0
    }
    dicc_MGLT = {
        'titulo': 'MGLT',
        'promedio': 0,
        'moda': 0,
        'max': 0,
        'min': 0
    }
    dicc_velocidad = {
        'titulo': 'velocidad máxima en atmósfera',
        'promedio': 0,
        'moda': 0,
        'max': 0,
        'min': 0
    }
    dicc_costo = {
        'titulo': 'costo',
        'promedio': 0,
        'moda': 0,
        'max': 0,
        'min': 0
    }
    
    calculos_estadistica(dicc_hiperimpulsor, naves, 0)
    calculos_estadistica(dicc_MGLT, naves, 1)
    calculos_estadistica(dicc_velocidad, naves, 2)
    calculos_estadistica(dicc_costo, naves, 3)
    


def calculos_estadistica(dicc, lista, posicion):
    promedio = calcular_promedio(lista, posicion)
    moda = calcular_moda(lista, posicion)
    max_d, min_d = calcular_maximo_minimo(lista, posicion)

    dicc["promedio"] = promedio
    dicc["moda"] = moda
    dicc["max"] = max_d
    dicc["min"] = min_d



def calcular_promedio(lista, posicion):
    suma = 0
    
    # Recorremos cada sublista en la lista principal
    for item in lista:
        suma += item[posicion]
    
    # Calculamos el promedio dividiendo la suma por el número de elementos
    return suma / len(lista)


def calcular_moda(lista, posicion):
    valores = []
    
    # Recorremos cada sublista en la lista principal
    for item in lista:
        valores.append(item[posicion])
    
    frecuencia = {}
    # Recorremos la lista 'valores' para contar las repeticiones de cada valor
    # Si el valor ya está en el diccionario, incrementamos su cuenta si no lo añadimos con una cuenta inicial de 1
    for valor in valores:
        if valor in frecuencia:
            frecuencia[valor] += 1
        else:
            frecuencia[valor] = 1
    
    moda = None
    max_frecuencia = 0
    # Recorremos el diccionario de frecuencias para encontrar el valor con mayor frecuencia
    for key, value in frecuencia.items():
        if value > max_frecuencia:
            max_frecuencia = value
            moda = key
    
    return moda


    def calcular_maximo_minimo(lista, posicion):
        # Inicializamos los valores de máximo y mínimo
        maximo = lista[0][posicion]
        minimo = lista[0][posicion]
        
        # Recorremos la lista para encontrar el máximo y mínimo
        for item in lista:
            valor = item[posicion]
            if valor > maximo:
                maximo = valor
            if valor < minimo:
                minimo = valor
        
        return maximo, minimo

#Funcion para crear, modificar y visualizar una mision     
def mision(lista_peliculas, lista_especies, lista_planetas, lista_mision):
    while True:
        opciones = ["Construir misión", "Modificar misión", "Visualizar misión", "Salir"]
        opcion = menu(opciones)

        #Creacion y guardado de la mision - pide los campos, crea el objeto y guarda en la lista
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
        
        #edicion de la mision - se escoge la mision, luego lo que deseas editar, para preceder a guardar la nueva info
        elif opcion == 1:
            for i, mision in enumerate(lista_mision):
                print(f"{i+1}. {mision}")
        
            opcion = input("ingrese el numero de la mision que desea elegir: ")
            while not opcion.isnumeric() or not int(opcion) in range(1, len(lista_mision)+1):
                opcion = input("Error, ingrese el numero de la mision que desea elegir: ")

            mision = int(opcion)-1
            mision.modificacion()

        #visualizar mision - recorre la lista y muestra cada elemento
        elif opcion == 2:
            print("Lista de misiones")
            for i, mision in enumerate(lista_misiones):
                print(i+1)
                print(mision.__str__())

        #Salir
        elif opcion == 3:
            break

    
    
main()