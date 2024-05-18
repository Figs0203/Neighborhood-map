class Arista:
    def __init__(self, nodo_inicio, nodo_destino, peso, calle):
        self.nodo_inicio = nodo_inicio
        self.nodo_destino = nodo_destino
        self.peso = peso
        self.calle = calle

    def __str__(self):
        return f'Vía: {self.calle}. Peso: {self.peso}'