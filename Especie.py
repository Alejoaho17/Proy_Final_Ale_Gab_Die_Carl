class Especie:
    def __init__(self, nombre, altura, clasificacion, nombre_planeta, lengua_materna, personajes_pertenecen, episodios):
        self.nombre = nombre
        self.altura = altura
        self.clasificacion = clasificacion
        self.nombre_planeta = nombre_planeta
        self.lengua_materna = lengua_materna
        self.personajes_pertenecen = personajes_pertenecen
        self.episodios = episodios

    def __str__(self):
        return f"Especie: {self.nombre}\n" \
               f"Altura: {self.altura}\n" \
               f"Clasificación: {self.clasificacion}\n" \
               f"Planeta: {self.nombre_planeta}\n" \
               f"Lengua Materna: {self.lengua_materna}\n" \
               f"Personajes que Pertenecen: {', '.join(self.personajes_pertenecen)}\n" \
               f"Episodios: {', '.join(self.episodios)}"