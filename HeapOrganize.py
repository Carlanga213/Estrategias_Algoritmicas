# se reorganiza un heap desde la posición i para mantener la propiedad de max-heap
def heapify(heap, i, heap_size):
    left = 2 * i # se obtiene la posicion del hijo izquierdo
    right = 2 * i + 1 # se obtiene la posicion del hijo derecho

    if left > heap_size and right > heap_size: # si el elemento i no tiene hijos termina
        return  

    elif right > heap_size:  # si el nodo i solo tiene hijo izquierdo
        largest = left

    elif heap[left] > heap[right]:  # si tiene dos hijos
        largest = left

    else:
        largest = right  # el hijo derecho es mayor

    if heap[i] < heap[largest]:  # si el nodo i es menor se intercambia con el hijo mas grande
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest, heap_size)  # se hace asi de forma recursiva hasta que i este en la posicion correcta

# guardar arreglo de strings en un heap
def build_heap(strings):
    heap_size = len(strings) - 1
    for i in range(heap_size // 2, 0, -1):  # se recorre de abajo hacia arriba
        heapify(strings, i, heap_size) # se organiza el heap pasando el arreglo de strings

heap = [None, "david", "vela", "enrique", "pepe", "eli"]  # arreglo empezando desde la posicion 1 para facilitar calculos
build_heap(heap)
print(heap)  # se imprime el heap reorganizado