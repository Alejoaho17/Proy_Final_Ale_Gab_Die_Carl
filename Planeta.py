class Planeta:
    def __init__(self, nombre, periodo_orbita, periodo_rotacion, cantidad_habitantes, tipo_clima, episodios, personajes):
        self.nombre = nombre
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_habitantes = cantidad_habitantes
        self.tipo_clima = tipo_clima
        self.episodios = episodios
        self.personajes = personajes

    def __str__(self):
        return f"Planeta: {self.nombre}\n" \
               f"Período de Órbita: {self.periodo_orbita}\n" \
               f"Período de Rotación: {self.periodo_rotacion}\n" \
               f"Cantidad de Habitantes: {self.cantidad_habitantes}\n" \
               f"Tipo de Clima: {self.tipo_clima}\n" \
               f"Episodios: {', '.join(self.episodios)}\n" \
               f"Personajes Originarios: {', '.join(self.personajes)}"
