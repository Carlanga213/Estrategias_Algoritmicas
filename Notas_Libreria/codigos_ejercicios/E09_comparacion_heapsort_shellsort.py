import random

def contar_movimientos_heap(arreglo):
    movimientos = 0
    def heapificar_max(heap, raiz, tam):
        nonlocal movimientos
        izquierda, derecha = 2 * raiz + 1, 2 * raiz + 2
        mayor = raiz
        if izquierda < tam and heap[izquierda] > heap[mayor]:
            mayor = izquierda
        if derecha < tam and heap[derecha] > heap[mayor]:
            mayor = derecha
        if mayor != raiz:
            heap[raiz], heap[mayor] = heap[mayor], heap[raiz]
            movimientos += 3
            heapificar_max(heap, mayor, tam)
    # construir heap
    n = len(arreglo)
    for i in range(n // 2 - 1, -1, -1):
        heapificar_max(arreglo, i, n)
    # ordenar
    for tam in range(n - 1, 0, -1):
        arreglo[0], arreglo[tam] = arreglo[tam], arreglo[0]
        movimientos += 3
        heapificar_max(arreglo, 0, tam)
    return movimientos

def contar_movimientos_shell(arreglo):
    movimientos = 0
    n = len(arreglo)
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    while h > 0:
        for i in range(h, n):
            temp = arreglo[i]
            movimientos += 1
            j = i
            while j >= h and arreglo[j - h] > temp:
                arreglo[j] = arreglo[j - h]
                movimientos += 1
                j -= h
            arreglo[j] = temp
            movimientos += 1
        h //= 3
    return movimientos

resultados = []
for N in range(1000, 10001, 100):
    suma_heap = suma_shell = 0
    repeticiones = N // 10
    for _ in range(repeticiones):
        datos = [random.randint(1, 10000) for _ in range(N)]
        suma_heap += contar_movimientos_heap(datos.copy())
        suma_shell += contar_movimientos_shell(datos.copy())
    resultados.append((N, suma_heap / repeticiones, suma_shell / repeticiones))
    print(N, suma_heap / repeticiones, suma_shell / repeticiones)
