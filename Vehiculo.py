class Vehiculo:
    def __init__(self, id, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class, pilots, films, url):
        self.id = id
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.vehicle_class = vehicle_class
        self.pilots = pilots
        self.films = films
        self.url = url

    def __str__(self):
        return f"Nombre: {self.name}\n" \
               f"Modelo: {self.model}\n" \
               f"Fabricante: {self.manufacturer}\n" \
               f"Costo en Créditos: {self.cost_in_credits}\n" \
               f"Longitud: {self.length}\n" \
               f"Velocidad Máxima Atmosférica: {self.max_atmosphering_speed}\n" \
               f"Tripulación: {self.crew}\n" \
               f"Pasajeros: {self.passengers}\n" \
               f"Capacidad de Carga: {self.cargo_capacity}\n" \
               f"Consumibles: {self.consumables}\n" \
               f"Clase de Vehículo: {self.vehicle_class}\n" \
               f"Pilotos: {', '.join(self.pilots) if self.pilots else 'N/A'}\n" \
               f"Películas: {', '.join(self.films) if self.pilots else 'N/A'}\n" \
               f"URL: {self.url}"