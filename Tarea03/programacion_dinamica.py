# ------------------------ Ejercicio 1: Palíndromo más largo ------------------------
def subsecuencia_palindroma_mas_larga(cadena: str) -> str:
    n = len(cadena)
    reverso = cadena[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if cadena[i] == reverso[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    i, j = n, n
    resultado = []
    while i > 0 and j > 0:
        if cadena[i - 1] == reverso[j - 1]:
            resultado.append(cadena[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(resultado))

print("\n--- Prueba Ejercicio 1 ---")
print("Subsecuencia palíndroma más larga:", subsecuencia_palindroma_mas_larga("abcbga"))

# ------------------------ Ejercicio 2: Asignación de actividades en dos salones ------------------------
def asignar_actividades_dos_salones(actividades):
    n = len(actividades)
    actividades.sort(key=lambda a: a[1])
    dp = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
    rastro = [[[[] for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n + 1):
        actual = actividades[i - 1]
        for j in range(i):
            for k in range(i):
                if dp[i - 1][j][k] >= dp[i][j][k]:
                    dp[i][j][k] = dp[i - 1][j][k]
                    rastro[i][j][k] = rastro[i - 1][j][k][:]

                if j == 0 or actividades[j - 1][1] <= actual[0]:
                    nuevo_valor = dp[i - 1][j][k] + actual[2]
                    if nuevo_valor > dp[i][i][k]:
                        dp[i][i][k] = nuevo_valor
                        rastro[i][i][k] = rastro[i - 1][j][k][:] + [("A", actual)]

                if k == 0 or actividades[k - 1][1] <= actual[0]:
                    nuevo_valor = dp[i - 1][j][k] + actual[2]
                    if nuevo_valor > dp[i][j][i]:
                        dp[i][j][i] = nuevo_valor
                        rastro[i][j][i] = rastro[i - 1][j][k][:] + [("B", actual)]

    mejor_valor = 0
    mejor_rastro = []
    for j in range(n + 1):
        for k in range(n + 1):
            if dp[n][j][k] > mejor_valor:
                mejor_valor = dp[n][j][k]
                mejor_rastro = rastro[n][j][k]

    asignadas = {"A": [], "B": []}
    for salon, act in mejor_rastro:
        asignadas[salon].append(act)

    return mejor_valor, asignadas

print("\n--- Prueba Ejercicio 2 ---")
actividades = [
    (1, 3, 50),
    (3, 5, 20),
    (0, 6, 60),
    (5, 7, 30),
    (8, 9, 25),
    (6, 10, 40)
]
valor, asignadas = asignar_actividades_dos_salones(actividades)
print("Valor total máximo asignado:", valor)
print("Actividades en Salón A:", asignadas["A"])
print("Actividades en Salón B:", asignadas["B"])

# ------------------------ Ejercicio 3: Algoritmo de Viterbi ------------------------
import math

def viterbi_maxima_probabilidad(grafo, inicio, secuencia):
    longitud = len(secuencia)
    dp = [{} for _ in range(longitud + 1)]
    camino = [{} for _ in range(longitud + 1)]
    dp[0][inicio] = 0

    for i in range(1, longitud + 1):
        esperado = secuencia[i - 1]
        for nodo in dp[i - 1]:
            for destino, sonido, prob in grafo.get(nodo, []):
                if sonido == esperado:
                    prob_log = dp[i - 1][nodo] + math.log(prob)
                    if destino not in dp[i] or prob_log > dp[i][destino]:
                        dp[i][destino] = prob_log
                        camino[i][destino] = nodo

    mejor = -math.inf
    final = None
    for nodo in dp[longitud]:
        if dp[longitud][nodo] > mejor:
            mejor = dp[longitud][nodo]
            final = nodo

    if mejor == -math.inf:
        return "No path found"

    resultado = [final]
    for i in range(longitud, 0, -1):
        resultado.append(camino[i][resultado[-1]])
    resultado.reverse()
    return resultado

print("\n--- Prueba Ejercicio 3 ---")
grafo = {
    "A": [("B", "a", 0.5), ("C", "a", 0.4)],
    "B": [("C", "b", 0.9)],
    "C": [("D", "b", 0.8)],
    "D": []
}
print("Camino más probable para secuencia ['a', 'b'] desde A:", viterbi_maxima_probabilidad(grafo, "A", ["a", "b"]))
