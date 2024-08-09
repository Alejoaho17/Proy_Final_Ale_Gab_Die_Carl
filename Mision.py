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