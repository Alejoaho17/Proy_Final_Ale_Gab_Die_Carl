class Pelicula:
    def __init__(self, id, titulo, numero_episodio, fecha_lanzamiento, opening_crawl, nombre_director, especies, personajes, planetas):
        self.id = id
        self.titulo = titulo
        self.numero_episodio = numero_episodio
        self.fecha_lanzamiento = fecha_lanzamiento
        self.opening_crawl = opening_crawl
        self.nombre_director = nombre_director
        self.especies = especies
        self.personajes = personajes
        self.planetas = planetas

    def __str__(self):
        return f"-Titulo: {self.titulo}\n" \
               f"-Numero de Episodio: {self.numero_episodio}\n" \
               f"-fecha de lanzamiento: {self.fecha_lanzamiento}\n" \
               f"-nombre del director: {self.nombre_director}\n" \
               f"-opening crawl: {self.opening_crawl}\n" 
               
