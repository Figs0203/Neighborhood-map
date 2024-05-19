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

    def encontrar_caminos(self, inicio_id, destino_id, camino_actual=None, peso=0, curvas=-1, calle_anterior=None):
        if camino_actual is None:
            camino_actual = []  # lista
        inicio = self.nodos.get(inicio_id)
        destino = self.nodos.get(destino_id)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        camino_actual = camino_actual + [inicio]
        if inicio == destino:
            camino_actual.append(curvas)
            camino_actual.append(peso)
            self.caminos.append(camino_actual[:])  # Almacenar una copia del camino actual
            return
        for arista in self.aristas:
            if arista.nodo_inicio == inicio and arista.nodo_destino not in camino_actual:
                nuevo_peso = peso + arista.peso
                nuevas_curvas = curvas
                if calle_anterior != arista.calle:
                    nuevas_curvas += 1
                self.encontrar_caminos(arista.nodo_destino.id, destino_id, camino_actual[:], nuevo_peso, nuevas_curvas,
                                       arista.calle)

    def buscar_arista(self, inicio_id, destino_id):
        for arista in self.aristas:
            if arista.nodo_inicio.id == inicio_id and arista.nodo_destino.id == destino_id:
                return arista

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

    def merge_sort(self, array, key):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half, key)
            self.merge_sort(right_half, key)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i][key] < right_half[j][key]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

    def ordenar_y_guardar_caminos(self, criterio='distancia'):
        print("Ordenando caminos\n")
        self.merge_sort(self.caminos, criterio)

        print("Escribiendo el archivo de texto\n")
        with open('caminos_ordenados.txt', 'w', encoding='utf-8') as file:
            for numero, camino in enumerate(self.caminos, start=1):
                file.write(f"Camino número {numero}:\n")
                for i in range(len(camino) - 2):
                    nodo_actual = camino[i]
                    nodo_siguiente = camino[i + 1]
                    for arista in self.aristas:
                        if arista.nodo_inicio == nodo_actual and arista.nodo_destino == nodo_siguiente:
                            file.write(f"{nodo_actual.id} ---> {arista.calle} ---> {nodo_siguiente.id}\n")
                file.write(f"Peso del camino: {camino[-1]/1000} kilometros\nCurvas del camino: {camino[-2]}\n\n")
