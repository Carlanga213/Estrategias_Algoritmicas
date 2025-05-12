# ------------------------ Ejercicio 6: Verificar ciclo en grafo no dirigido ------------------------
def contiene_ciclo(grafo, cantidad_vertices):
    visitado = [False] * cantidad_vertices

    def dfs(vertice, padre):
        visitado[vertice] = True
        for vecino in grafo.get(vertice, []):
            if not visitado[vecino]:
                if dfs(vecino, vertice):
                    return True
            elif vecino != padre:
                return True
        return False

    for v in range(cantidad_vertices):
        if not visitado[v]:
            if dfs(v, -1):
                return True
    return False

print("\n--- Prueba Ejercicio 6 ---")
grafo1 = {
    0: [1],
    1: [2],
    2: [0]
}
print("¿El grafo tiene ciclo?", contiene_ciclo(grafo1, 3))

# ------------------------ Ejercicio 7: DFS no recursivo ------------------------
def recorrido_dfs_no_recursivo(grafo, inicio):
    visitado = set()
    pila = [inicio]
    resultado = []

    while pila:
        actual = pila.pop()
        if actual not in visitado:
            visitado.add(actual)
            resultado.append(actual)
            for vecino in reversed(grafo.get(actual, [])):
                if vecino not in visitado:
                    pila.append(vecino)
    return resultado


print("\n--- Prueba Ejercicio 7 ---")
grafo2 = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}
print("Recorrido DFS desde el nodo 0:", recorrido_dfs_no_recursivo(grafo2, 0))

# ------------------------ Ejercicio 8: Recorrido de Euler ------------------------
def recorrido_euler_dirigido(grafo, inicio):
    adyacencia = {}
    grado_entrada = {}
    grado_salida = {}

    for origen in grafo:
        for destino in grafo[origen]:
            adyacencia.setdefault(origen, []).append(destino)
            grado_salida[origen] = grado_salida.get(origen, 0) + 1
            grado_entrada[destino] = grado_entrada.get(destino, 0) + 1
            adyacencia.setdefault(destino, [])

    for nodo in adyacencia:
        if grado_entrada.get(nodo, 0) != grado_salida.get(nodo, 0):
            return "No existe recorrido de Euler"

    pila = [inicio]
    recorrido = []

    while pila:
        nodo = pila[-1]
        if adyacencia[nodo]:
            siguiente = adyacencia[nodo].pop()
            pila.append(siguiente)
        else:
            recorrido.append(pila.pop())

    recorrido.reverse()
    return recorrido

print("\n--- Prueba Ejercicio 8 ---")
grafo3 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
print("Recorrido de Euler desde 'A':", recorrido_euler_dirigido(grafo3, 'A'))

# ------------------------ Ejercicio 9: Camino más confiable ------------------------
import math

def camino_mas_confiable(grafo, inicio, destino):
    distancias = {v: float('inf') for v in grafo}
    distancias[inicio] = 0
    padre = {v: None for v in grafo}
    visitado = set()

    while True:
        nodo_actual = None
        minimo = float('inf')
        for nodo in distancias:
            if nodo not in visitado and distancias[nodo] < minimo:
                minimo = distancias[nodo]
                nodo_actual = nodo
        if nodo_actual is None or nodo_actual == destino:
            break
        visitado.add(nodo_actual)

        for vecino, probabilidad in grafo.get(nodo_actual, []):
            peso = -math.log(probabilidad)
            if distancias[nodo_actual] + peso < distancias.get(vecino, float('inf')):
                distancias[vecino] = distancias[nodo_actual] + peso
                padre[vecino] = nodo_actual

    if distancias[destino] == float('inf'):
        return "No existe camino"

    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = padre[actual]
    camino.reverse()

    prob_total = 1.0
    for i in range(len(camino) - 1):
        desde = camino[i]
        hacia = camino[i + 1]
        for vecino, prob in grafo[desde]:
            if vecino == hacia:
                prob_total *= prob
                break

    return camino, prob_total

print("\n--- Prueba Ejercicio 9 ---")
grafo4 = {
    'A': [('B', 0.5)],
    'B': [('C', 0.6)],
    'C': [('D', 0.8)],
    'D': []
}
camino, prob = camino_mas_confiable(grafo4, 'A', 'D')
print("Camino más confiable de A a D:", camino)
print("Probabilidad total:", prob)