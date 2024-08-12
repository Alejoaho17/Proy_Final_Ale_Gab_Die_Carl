class Nave:
    def __init__(self, id, name, model, starship_class, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, pilots):
        self.id = id
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.pilots = pilots

    def __str__(self):
        return f"Nombre: {self.name}\n" \
               f"Modelo: {self.model}\n" \
               f"Clase de Nave: {self.starship_class}\n" \
               f"Fabricante: {self.manufacturer}\n" \
               f"Costo en Créditos: {self.cost_in_credits}\n" \
               f"Longitud: {self.length}\n" \
               f"Tripulación: {self.crew}\n" \
               f"Pasajeros: {self.passengers}\n" \
               f"Velocidad Máxima Atmosférica: {self.max_atmosphering_speed}\n" \
               f"Calificación de Hiperimpulsor: {self.hyperdrive_rating}\n" \
               f"MGLT: {self.MGLT}\n" \
               f"Capacidad de Carga: {self.cargo_capacity}\n" \
               f"Consumibles: {self.consumables}\n" \
               f"Pilotos: {', '.join(self.pilots) if self.pilots else 'N/A'}"
