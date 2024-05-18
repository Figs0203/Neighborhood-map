from Arista import Arista


class GrafoDirigido:
    def __init__(self):
        self.nodos = {}  # diccionario "HashTable"
        self.aristas = []  # lista
        self.caminos = []

    def agregar_nodo(self, nodo):
        self.nodos[nodo.id] = nodo

    def agregar_arista(self, nodo_inicio, nodo_destino, peso, calle):
        if nodo_inicio.id in self.nodos and nodo_destino.id in self.nodos:
            arista = Arista(nodo_inicio, nodo_destino, peso, calle)
            self.aristas.append(arista)

    def mostrar_grafo(self):
        for arista in self.aristas:
            print(f"{arista}")

    def encontrar_caminos(self, inicio_id, destino_id, camino_actual=None, peso=0):
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = self.nodos.get(inicio_id)
        destino = self.nodos.get(destino_id)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            camino_actual.append(peso)
            self.caminos.append(camino_actual[:])  # Almacenar una copia del camino actual
            return
        for arista in self.aristas:
            if arista.nodo_inicio == inicio and arista.nodo_destino not in camino_actual:
                peso += arista.peso
                self.encontrar_caminos(arista.nodo_destino.id, destino_id, camino_actual[:], peso)

    def buscar_arista(self, inicio_id, destino_id):
        for arista in self.aristas:
            if arista.nodo_inicio.id == inicio_id and arista.nodo_destino.id == destino_id:
                return arista

    def eliminar_nodo(self, nodo):
        if nodo in self.nodos.keys():
            self.nodos.pop(nodo)
            print(f"El nodo {nodo} ha sido exterminado.")
            queu = []
            for i in self.aristas:
                if i.nodo_inicio == nodo or i.nodo_destino == nodo:
                    queu.append(i)
                for j in queu:
                    self.aristas.remove(j)

        else:
            return "Esta mondá no existe."

    def get_nodo(self, nodo_id):
        for nodo in self.nodos.values():
            if nodo.id == nodo_id:
                return nodo
        return None

    def dijkstra(self, inicio_id):
        nodos = self.nodos
        distancias = {nodo.id: float('inf') for nodo in nodos.values()}
        distancias[inicio_id] = 0
        visitados = set()

        while len(visitados) < len(nodos):
            nodo_actual = min(set(nodos.values()) - visitados, key=lambda nodo: distancias[nodo.id])
            visitados.add(nodo_actual)

            for arista in self.aristas:
                if arista.nodo_inicio == nodo_actual and arista.nodo_destino not in visitados:
                    distancia = distancias[nodo_actual.id] + arista.peso
                    if distancia < distancias[arista.nodo_destino.id]:
                        distancias[arista.nodo_destino.id] = distancia

        return distancias

    def imprimir_camino(self):
        for numero in range(len(self.caminos)-1):
            print(f"\nImprimiendo el camino número {numero+1}")
            for i in range(len(self.caminos[numero]) - 2):
                nodo_actual = self.caminos[numero][i]
                nodo_siguiente = self.caminos[numero][i + 1]
                for arista in self.aristas:
                    if arista.nodo_inicio == nodo_actual and arista.nodo_destino == nodo_siguiente:
                        print(f"{nodo_actual.id}   --->   {arista.calle}   --->   {nodo_siguiente.id}")
            print(f"Peso del camino: {self.caminos[numero][-1]}")
