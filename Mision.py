class Mision:
    def __init__(self, nombre_mision, planeta_destino, nave, armas, integrantes):
        self.nombre_mision = nombre_mision
        self.planeta_destino = planeta_destino
        self.nave = nave
        self.armas = armas
        self.integrantes = integrantes

    def __str__(self):
        return f"Misión: {self.nombre_mision}\n" \
               f"Planeta Destino: {self.planeta_destino}\n" \
               f"Nave a Utilizar: {self.nave}\n" \
               f"Armas a Utilizar: {', '.join(self.armas)}\n" \
               f"Integrantes de la Misión: {', '.join(self.integrantes)}"

    #edicion de la mision - se escoge la mision, luego lo que deseas editar, para preceder a guardar la nueva info
    def modificacion(self):
        print("Que deseas modificar?")
        opciones = ["Nombre de la mision", "planeta de la mision", "nave de la mision", "armas para la mision", "Integrantes de la mision"]
        opcion = menu(opciones)

        nuevo_valor = []

        if opcion == 0:
            nuevo_valor = input("Ingrese el nuevo valor: ")
            self.nombre_mision = nuevo_valor

        elif opcion == 1:
            for i, planeta in enumerate(lista_planetas):
                print(i+1, planeta.nombre)
            mision_planeta = input("Ingresa el numero del planeta que desea: ")
            cantidad_planetas = len(lista_planetas)
            while not mision_planeta.isnumeric() or not int(mision_planeta) in range(1, cantidad+1):
                mision_planeta = input("Error, Ingresa el numero del planeta que desea: ")
            
            nuevo_valor = lista_planetas[int(mision_planeta)-1]
            self.planeta_destino = nuevo_valor
        elif opcion == 2:
            for i, nave in enumerate(lista_naves):
                print(i+1, nave.nombre)
            mision_nave = input("Ingresa el numero del planeta que desea: ")
            cantidad_naves = len(lista_naves)
            while not mision_nave.isnumeric() or not int(mision_nave) in range(1, cantidad+1):
                mision_nave = input("Error, Ingresa el numero del planeta que desea: ")
            
            nuevo_valor = lista_naves[int(mision_nave)-1]

            self.nave = nuevo_valor
            
        elif opcion == 3:
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
        
            self.armas = mision_armas
        elif opcion == 4:
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
            self.integrantes = mision_integrantes
        
        print("Cambio con exito")


    def convertir_str(self):
        return f"{self.nombre_mision}///{self.planeta_destino}///{self.nave}///{', '.join(self.armas)}///{', '.join(self.integrantes)}///\n"