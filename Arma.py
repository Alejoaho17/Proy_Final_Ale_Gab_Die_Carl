class Arma():
    def __init__(self, id,name,model,manufacturer,cost_in_credits,length,tipo,description,films):
        self.id = id
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.tipo = tipo
        self.description = description
        self.films = films


    def __str__(self):
        return f"Nombre: {self.name}\n" \
               f"Modelo: {self.model}\n" \
               f"Fabricante: {self.manufacturer}\n" \
               f"Costo en Créditos: {self.cost_in_credits}\n" \
               f"Longitud: {self.length}\n" \
               f"Tipo: {self.tipo}\n" \
               f"Descripción: {self.description}\n" \
               f"Películas: {', '.join(self.films)}"
