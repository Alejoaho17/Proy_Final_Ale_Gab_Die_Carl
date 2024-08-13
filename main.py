from Especie import Especie
from Mision import Mision
from Personaje import Personaje
from Planeta import Planeta
from Nave import Nave
from Pelicula import Pelicula
from Arma import Arma
from Vehiculo import Vehiculo

import matplotlib.pyplot as plt
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
def api(lista_peliculas, lista_especies, lista_planetas, lista_personajes, lista_armas, lista_naves,lista_mision,lista_vehiculos):
    '''
    # URL del endpoint de películas
    url = "https://www.swapi.tech/api/films"

    # Obtener los datos de las películas
    response = requests.get(url)
    data = response.json()

    # Iterar sobre cada película y obtener su información detallada
    for pelicula in data["result"]:
        # Imprimir la estructura de cada película para identificar la clave correcta
        #print(pelicula)
        id = pelicula["uid"]
        pelicula = pelicula["properties"]
        # Puedes crear una instancia de una clase Pelicula si tienes una clase definida
        nuevo_pelicula = Pelicula(id, pelicula["title"], pelicula["episode_id"], pelicula["release_date"], pelicula["opening_crawl"],  pelicula["director"], pelicula["species"], pelicula["characters"], pelicula["planets"])
        lista_peliculas.append(nuevo_pelicula)
    

    page = "https://www.swapi.tech/api/vehicles"

    # Mientras haya una página siguiente, seguir obteniendo personajes
    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada personaje y obtener su información detallada
        for vehiculo in results:
            vehiculo_url = vehiculo["url"]
            vehiculo = requests.get(vehiculo_url).json()
            id = vehiculo["result"]["uid"]
            vehiculo = vehiculo["result"]["properties"]
            #print(vehiculo)  
            # Imprimir la información del personaje
            nuevo_vehiculo = Vehiculo(id, vehiculo["name"], vehiculo["model"], vehiculo["manufacturer"], vehiculo["cost_in_credits"], vehiculo["length"], vehiculo["max_atmosphering_speed"], vehiculo["crew"], vehiculo["passengers"], vehiculo["cargo_capacity"], vehiculo["consumables"], vehiculo["vehicle_class"], vehiculo["pilots"], vehiculo["films"], vehiculo["url"])
                        
            lista_vehiculos.append(nuevo_vehiculo)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]
    
    
    

    page = "https://www.swapi.tech/api/species"

    # Mientras haya una página siguiente, seguir obteniendo personajes
    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada personaje y obtener su información detallada
        for especie in results:
            especie_url = especie["url"]
            especie = requests.get(especie_url).json()
            id = especie["result"]["uid"]
            especie = especie["result"]["properties"]
            #print(especie)  
            # Imprimir la información del personaje
            nuevo_especie = Especie(id, especie["name"], especie["homeworld"], especie["classification"], especie['homeworld'], especie["language"], especie["people"], [])
            for pelicula in lista_peliculas:
                for url in pelicula.especies:
                    if url.split('/')[-1] == id:
                        nuevo_especie.episodios.append(pelicula.titulo)
            
            lista_especies.append(nuevo_especie)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]
    
    
    
    page = "https://www.swapi.tech/api/starships"

    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada nave y obtener su información detallada
        for nave in results:
            nave_url = nave["url"]
            
            nave = requests.get(nave_url).json()
            id = nave["result"]["uid"]
            nave = nave["result"]["properties"]
            
            # Crear una nueva instancia de Nave
            nueva_nave = Nave(id, nave["name"], nave["model"], nave["starship_class"], nave["manufacturer"], nave["cost_in_credits"], nave["length"], nave["crew"], nave["passengers"], nave["max_atmosphering_speed"], nave["hyperdrive_rating"], nave["MGLT"], nave["cargo_capacity"], nave["consumables"], nave["pilots"])
            
            lista_naves.append(nueva_nave)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]
       
    page = "https://www.swapi.tech/api/people"

    # Mientras haya una página siguiente, seguir obteniendo personajes
    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada personaje y obtener su información detallada
        for character in results:
            character_url = character["url"]
            character = requests.get(character_url).json()
            id = character["result"]["uid"]
            character = character["result"]["properties"]
            #print(character)  
            # Imprimir la información del personaje
            nuevo_personaje = Personaje(id, character["name"], character["homeworld"], [], character['gender'], "", [], [])
            #print(nuevo_personaje.__str__())
            for pelicula in lista_peliculas:
                for url in pelicula.personajes:
                    if url.split('/')[-1] == id:
                        nuevo_personaje.episodios.append(pelicula.titulo)

            for especie in lista_especies:
                for url in especie.personajes_pertenecen:
                    if url.split('/')[-1] == id:
                        #print("si")
                        nuevo_personaje.especie = especie.nombre

            for nave in lista_naves:
                for url in nave.pilots:
                    if url.split('/')[-1] == id:
                        nuevo_personaje.naves.append(nave.name)

            for vehiculo in lista_vehiculos:
                for url in vehiculo.pilots:
                    if url.split('/')[-1] == id:
                        nuevo_personaje.vehiculos.append(vehiculo.name)
            

            
            lista_personajes.append(nuevo_personaje)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]

    #print(lista_personajes)
    page = "https://www.swapi.tech/api/planets"

    # Mientras haya una página siguiente, seguir obteniendo personajes
    while page:
        response = requests.get(page)
        data = response.json()
        results = data['results']

        # Iterar sobre cada personaje y obtener su información detallada
        for planeta in results:
            planeta_url = planeta["url"]
            
            planeta = requests.get(planeta_url).json()
            id = planeta["result"]["uid"]
            planeta = planeta["result"]["properties"]
            #print(planeta)  
            # Imprimir la información del personaje
            nuevo_planeta = Planeta(id, planeta["name"], planeta["orbital_period"], planeta["rotation_period"], planeta["population"], planeta["climate"], [], [])
            
            for personaje in lista_personajes:
                if personaje.nombre_planeta_origen.split('/')[-1] == id:
                    nuevo_planeta.personajes.append(personaje.nombre)
                    #print(personaje.nombre)
            
            #print(nuevo_planeta.personajes)
            
            for pelicula in lista_peliculas:
                for url in pelicula.planetas:
                    if (url.split('/')[-1] == id):
                        (nuevo_planeta.episodios).append(pelicula.titulo)

            #print(nuevo_planeta.episodios) 

            lista_planetas.append(nuevo_planeta)
            
        # Actualizar la URL de la siguiente página
        page = data["next"]
    '''
    
    with open('starwars/csv/weapons.csv','r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if row[0] != "id":
                nueva_arma = Arma(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                lista_armas.append([row[1], 0])  
    
    with open('misiones.txt','r') as file:
        informacion = file.readlines()
        for info in informacion:
            info = info.split("///")
            info.remove(info[-1])

            #print(info)
            nueva_mision = Mision(info[0], info[1], info[2], [], [])
            nueva_mision.armas.append(info[3])
            nueva_mision.integrantes.append(info[4])

            lista_mision.append(nueva_mision)

    
    
#Main
def main():
    lista_peliculas = []
    lista_especies = []
    lista_planetas = []
    lista_personajes = []
    lista_mision = []
    lista_armas = []
    lista_naves = []
    lista_vehiculos = []

    api(lista_peliculas, lista_especies, lista_planetas, lista_personajes, lista_armas, lista_naves,lista_mision,lista_vehiculos)
    
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
            mision(lista_planetas, lista_mision, lista_personajes, lista_armas, lista_naves)
        elif opcion == 5:
            guardar_mision(lista_mision)
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
            print('----'+ str(contador) +'----')
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

    #print(planetas)

    listado_planeta = []
    listado_numero = []

    for planeta in planetas:
        listado_planeta.append(planeta[0])
        listado_numero.append(planeta[1])

    plt.figure(figsize=(12, 6))
    plt.plot(listado_planeta, listado_numero)
    plt.title('Gráfico de numero de nacidos en cada planeta')
    plt.xlabel('Planetas')
    plt.ylabel('Numero de nacidos')
    plt.show()


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
                lista = [row[11], row[12], row[6], row[4]]
                for i in range(len(lista)):
                    if lista[i]:
                        lista[i] = float(lista[i])
                    else:
                        lista[i] = 0
                naves.append(lista)


    #print(naves)
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
        'titulo': 'velocidad máxima',
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

    mostrar_estadistica(dicc_hiperimpulsor, dicc_MGLT, dicc_velocidad, dicc_costo)

#Muestra la tabla de estadistica
def mostrar_estadistica(dicc_hiperimpulsor, dicc_MGLT, dicc_velocidad, dicc_costo):
    print(f"{'Nombre':<20} | {'Promedio':<20} | {'Moda':<20} | {'Maximo':<20} | {'Minimo':<20}")
    print(f"{dicc_hiperimpulsor['titulo']:<20} | {dicc_hiperimpulsor['promedio']:<20} | {dicc_hiperimpulsor['moda']:<20} | {dicc_hiperimpulsor['max']:<20} | {dicc_hiperimpulsor['min']:<20}")
    print(f"{dicc_MGLT['titulo']:<20} | {dicc_MGLT['promedio']:<20} | {dicc_MGLT['moda']:<20} | {dicc_MGLT['max']:<20} | {dicc_MGLT['min']:<20}")
    print(f"{dicc_velocidad['titulo']:<20} | {dicc_velocidad['promedio']:<20} | {dicc_velocidad['moda']:<20} | {dicc_velocidad['max']:<20} | {dicc_velocidad['min']:<20}")
    print(f"{dicc_costo['titulo']:<20} | {dicc_costo['promedio']:<20} | {dicc_costo['moda']:<20} | {dicc_costo['max']:<20} | {dicc_costo['min']:<20}")

#calcula las estadisticas de los 4 diccionarios
def calculos_estadistica(dicc, lista, posicion):
    promedio = calcular_promedio(lista, posicion)
    moda = calcular_moda(lista, posicion)
    max_d, min_d = calcular_maximo_minimo(lista, posicion)

    dicc["promedio"] = promedio
    dicc["moda"] = moda
    dicc["max"] = max_d
    dicc["min"] = min_d

#Calcula el promedio de cada dicc
def calcular_promedio(lista, posicion):
    suma = 0
    
    # Recorremos cada sublista en la lista principal
    for item in lista:
        n = item[posicion]
        #print(n)
        suma += float(n)
    
    # Calculamos el promedio dividiendo la suma por el número de elementos
    return suma / len(lista)

#Calcula el moda de cada dicc
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

#Calcula el max y min de cada dicc
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
def mision(lista_planetas, lista_mision, lista_personajes, lista_armas, lista_naves):

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
            while not mision_planeta.isnumeric() or not int(mision_planeta) in range(1, cantidad_planetas+1):
                mision_planeta = input("Error, Ingresa el numero del planeta que desea: ")
            
            mision_planeta = lista_planetas[int(mision_planeta)-1].nombre



            for i, nave in enumerate(lista_naves):
                print(i+1, nave.name)
            mision_nave = input("Ingresa el numero del naves que desea: ")
            cantidad_naves = len(lista_naves)
            while not mision_nave.isnumeric() or not int(mision_nave) in range(1, cantidad_naves+1):
                mision_nave = input("Error, Ingresa el numero del naves que desea: ")
            
            mision_nave = lista_naves[int(mision_nave)-1].name


            maximo = 7
            mision_armas = []
            while len(mision_armas) <= maximo:
                for i, arma in enumerate(lista_armas):
                    print(i+1, arma[0])
                mision_arma = input("Ingresa el numero del arma que desea: ")
                cantidad_armas = len(lista_armas)
                while not mision_arma.isnumeric() or not int(mision_arma) in range(1, cantidad_armas+1):
                    mision_arma = input("Error, Ingresa el numero del planeta que desea: ")
                
                mision_arma = lista_armas[int(mision_arma)-1]
                mision_armas.append(mision_arma[0])
                pregunta = input("Quieres agregar otra arma? 1. si 2. no")
                while not pregunta.isnumeric() or not int(pregunta) in range(1, 3):
                    pregunta = input("error, Quieres agregar otra arma? 1. si 2. no")
                
                if pregunta == "2":
                    break
            

            mision_integrantes = []
            while len(mision_integrantes) <= maximo:
                for i, integrante in enumerate(lista_personajes):
                    print(i+1, integrante.nombre)
                mision_integrante = input("Ingresa el numero del integrante que desea: ")
                cantidad_integrantes = len(lista_personajes)
                while not mision_integrante.isnumeric() or not int(mision_integrante) in range(1, cantidad_integrantes+1):
                    mision_integrante = input("Error, Ingresa el numero del integrante que desea: ")
                
                mision_integrante = lista_personajes[int(mision_integrante)-1]
                mision_integrantes.append(mision_integrante.nombre)

                pregunta = input("Quieres agregar otra integrante? 1. si 2. no")
                while not pregunta.isnumeric() or not int(pregunta) in range(1, 3):
                    pregunta = input("error, Quieres agregar otra integrante? 1. si 2. no")
                
                if pregunta == "2":
                    break
            
            nueva_mision = Mision(mision, mision_planeta, mision_nave, mision_armas, mision_integrantes)
            lista_mision.append(nueva_mision)
        
        #edicion de la mision - se escoge la mision, luego lo que deseas editar, para preceder a guardar la nueva info
        elif opcion == 1:
            if len(lista_mision) != 0:
                for i, mision in enumerate(lista_mision):
                    print(f"{i+1}. {mision}")
            
                opcion = input("ingrese el numero de la mision que desea elegir: ")
                while not opcion.isnumeric() or not int(opcion) in range(1, len(lista_mision)+1):
                    opcion = input("Error, ingrese el numero de la mision que desea elegir: ")

                mision = lista_mision[int(opcion)-1]
                mision.modificacion(lista_planetas, lista_mision, lista_personajes, lista_armas, lista_naves)
            else:
                print("Debe crear al menos una mision")
        #visualizar mision - recorre la lista y muestra cada elemento
        elif opcion == 2:
            print("Lista de misiones")
            for i, mision in enumerate(lista_mision):
                print(i+1)
                print(mision.__str__())

        #Salir
        elif opcion == 3:
            break

def guardar_mision(lista_mision):
    str_misiones = ""
    for mision in range(0, len(lista_mision)):
        str_misiones = str_misiones + lista_mision[mision].convertir_str()

    with open('misiones.txt', 'w') as a:
        a.write(str_misiones)
    
    
main()