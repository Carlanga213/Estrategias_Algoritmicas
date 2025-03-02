# recibe el heap y la posicion del elemento a borrar
def heap_delete(heap, t):
    n = len(heap) - 1  # se asume que el heap está indexado desde 1 y se calcula el tamaño del heap
    if t < 1 or t > n:
        return  # indice invalido

    # intercambiar el elemento con el ultimo y eliminar el ultimo elemento
    heap[t], heap[n] = heap[n], heap[t]
    heap.pop() 

    # se calculan las posiciones de los nodos relacionados con el padre
    parent = t // 2
    left = 2 * t  # hijo izquierdo
    right = 2 * t + 1 # hijo derecho

    if t > 1 and heap[t] > heap[parent]:  # si el nodo es mayor que su padre se sube
        while t > 1 and heap[t] > heap[parent]:
            heap[t], heap[parent] = heap[parent], heap[t] # intercambiar con el padre
            t = parent # se mueve t hacia arriba
            parent = t // 2 # se actualiza el nuevo padre

    else:  # si es menor que alguno de sus hijos se baja
        while left <= len(heap) - 1:  # mientras tenga un hijo
            largest = left
            if right <= len(heap) - 1 and heap[right] > heap[left]:
                largest = right
            if heap[t] >= heap[largest]:  # si ya cumple la propiedad se termina el ciclo
                break
            heap[t], heap[largest] = heap[largest], heap[t]
            t = largest # se mueve t hacia abajo
            left = 2 * t # nuevo hijo izquierdo
            right = 2 * t + 1  # nuevo hijo derecho