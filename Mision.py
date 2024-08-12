class Mision:
    def __init__(self, nombre_mision, planeta_destino, nave, armas, integrantes):
        self.nombre_mision = nombre_mision
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def __str__(self):
        return f"\nMisión: {self.nombre_mision}\n" \
               f"Planeta Destino: {self.planeta_destino}\n" \
               f"Nave a Utilizar: {self.nave}\n" \
               f"Armas a Utilizar: {', '.join(self.armas)}\n" \
               f"Integrantes de la Misión: {', '.join(self.integrantes)}"

    #edicion de la mision - se escoge la mision, luego lo que deseas editar, para preceder a guardar la nueva info
    def modificacion(self, lista_planetas, lista_mision, lista_personajes, lista_armas, lista_naves):
        print("Que deseas modificar?")
        opciones = ["Nombre de la mision", "planeta de la mision", "nave de la mision", "armas para la mision", "Integrantes de la mision"]
        for i, opcion in enumerate(opciones):
            print(f"{i+1}. {opcion}")
        
        opcion = input("ingrese el numero de la opcion que desea elegir: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, len(opciones)+1):
            opcion = input("Error, ingrese el numero de la opcion que desea elegir: ")

        opcion = int(opcion)-1

        nuevo_valor = []

        if opcion == 0:
            nuevo_valor = input("Ingrese el nuevo valor: ")
            self.nombre_mision = nuevo_valor

        elif opcion == 1:
            for i, planeta in enumerate(lista_planetas):
                print(i+1, planeta.nombre)
            mision_planeta = input("Ingresa el numero del planeta que desea: ")
            cantidad_planetas = len(lista_planetas)
            while not mision_planeta.isnumeric() or not int(mision_planeta) in range(1, cantidad_planetas+1):
                mision_planeta = input("Error, Ingresa el numero del planeta que desea: ")
            
            nuevo_valor = lista_planetas[int(mision_planeta)-1].nombre
            self.planeta_destino = nuevo_valor

        elif opcion == 2:
            for i, nave in enumerate(lista_naves):
                print(i+1, nave.name)
            mision_nave = input("Ingresa el numero del naves que desea: ")
            cantidad_naves = len(lista_naves)
            while not mision_nave.isnumeric() or not int(mision_nave) in range(1, cantidad_naves+1):
                mision_nave = input("Error, Ingresa el numero del naves que desea: ")
            
            nuevo_valor = lista_naves[int(mision_nave)-1].name
            self.nave = nuevo_valor
            
        elif opcion == 3:
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
            
        
            self.armas = mision_armas
        elif opcion == 4:
            maximo = 7
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
            
            self.integrantes = mision_integrantes
        
        print("Cambio con exito")


    def convertir_str(self):
        return f"{self.nombre_mision}///{self.planeta_destino}///{self.nave}///{', '.join(self.armas)}///{', '.join(self.integrantes)}///\n"