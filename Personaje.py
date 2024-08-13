class Personaje:
    def __init__(self, id, nombre, nombre_planeta_origen, episodios, genero, especie, naves, vehiculos):
        self.id = id
        self.nombre = nombre
        self.nombre_planeta_origen = nombre_planeta_origen
        self.episodios = episodios
        self.genero = genero
        self.especie = especie
        self.naves = naves
        self.vehiculos = vehiculos

    def __str__(self):
        return f"Personaje: {self.nombre}\n" \
               f"Planeta de Origen: {self.nombre_planeta_origen}\n" \
               f"Episodios: {', '.join(self.episodios)}\n" \
               f"Género: {self.genero}\n" \
               f"Especie: {self.especie}\n" \
               f"Naves: {', '.join(self.naves)}\n" \
               f"Vehículos: {', '.join(self.vehiculos)}\n"

