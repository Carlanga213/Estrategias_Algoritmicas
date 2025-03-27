# Función para imprimir el heap con formato girado
import math

def print_heap(heap, nodo=0, prefijo="", es_ultimo=True):
    """ Imprime un heap con los nodos más llenos a la izquierda. """
    if nodo >= len(heap):
        return
    
    conector = "└── " if es_ultimo else "├── "
    print(prefijo + conector + str(heap[nodo]))  # Imprime el nodo actual
    
    prefijo += "    " if es_ultimo else "│   "  # Ajusta el prefijo para los hijos

    # Llamadas recursivas para los hijos (izquierda primero)
    if 2 * nodo + 2 < len(heap):
        print_heap(heap, 2 * nodo + 2, prefijo, False)
    if 2 * nodo + 1 < len(heap):
        print_heap(heap, 2 * nodo + 1, prefijo, True)

# Función de heapify hacia abajo (max-heap)
def heapify(heap, n, i):
    """ Convierte el subárbol con raíz en el índice i a un max-heap """
    largest = i
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho
    intercambio_hecho = False
    
    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right
    
    print(f"\n------------- Heapify en el nodo {heap[i]} (índice {i}):")
    
    if largest != i:
        print(f"Cambiando {heap[i]} con {heap[largest]}")
        heap[i], heap[largest] = heap[largest], heap[i]
        intercambio_hecho = True
        print("\n------------- Estado del heap después del cambio:")
        print_heap(heap)
        print(f"Estado como arreglo: {heap}")
        heapify(heap, n, largest)
    
    if not intercambio_hecho:
        print(f"No se hizo intercambio en el nodo {heap[i]} (índice {i})")
        print(f"Estado como arreglo: {heap}")

# Función para construir el max-heap
def build_max_heap(heap):
    """ Construye un max-heap desde un arreglo """
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(heap, n, i)
    return heap

# Arreglo de ejemplo
heap = [5, 8, 7, 9, 1, 3]

print("-------------------------- Estado inicial del heap: --------------------------")
print_heap(heap)
print(f"Estado como arreglo: {heap}")

print("\n-------------------------- Construyendo el max-heap: --------------------------")
heap = build_max_heap(heap)

print("\n-------------------------- Heap final: --------------------------")
print_heap(heap)
print(f"Estado como arreglo: {heap}")
