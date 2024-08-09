class Vehiculo:
    def __init__(self, nombre, modelo, clase_vehiculo, fabricante, costo_en_creditos, longitud, tripulacion, pasajeros, velocidad_maxima_atmosferica, capacidad_carga, consumibles, peliculas, pilotos):
        self.nombre = nombre
        self.modelo = modelo
        self.clase_vehiculo = clase_vehiculo
        self.fabricante = fabricante
        self.costo_en_creditos = costo_en_creditos
        self.longitud = longitud
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
        self.velocidad_maxima_atmosferica = velocidad_maxima_atmosferica
        self.capacidad_carga = capacidad_carga
        self.consumibles = consumibles
        self.peliculas = peliculas
        self.pilotos = pilotos

    def __str__(self):
        return f"Vehículo: {self.nombre}\n" \
               f"Modelo: {self.modelo}\n" \
               f"Clase de Vehículo: {self.clase_vehiculo}\n" \
               f"Fabricante: {self.fabricante}\n" \
               f"Costo en Créditos: {self.costo_en_creditos}\n" \
               f"Longitud: {self.longitud}\n" \
               f"Tripulación: {self.tripulacion}\n" \
               f"Pasajeros: {self.pasajeros}\n" \
               f"Velocidad Máxima Atmosférica: {self.velocidad_maxima_atmosferica}\n" \
               f"Capacidad de Carga: {self.capacidad_carga}\n" \
               f"Consumibles: {self.consumibles}\n" \
               f"Películas: {', '.join(self.peliculas)}\n" \
               f"Pilotos: {', '.join(self.pilotos)}"