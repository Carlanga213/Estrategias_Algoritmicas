def insertion_sort(A):
    # 1. Para p ← 2 to A.length: Recorremos el arreglo desde la segunda posición
    for p in range(1, len(A)):  
        # 2. Let pivot ← Ap: Se selecciona el elemento en la posición p como pivote
        pivot = A[p]  
        # 3. Let i ← p - 1: i representa la posición anterior al pivote en el subarreglo ordenado
        i = p - 1  
        # 4. While i > 0 and Ai > pivot: Se mueve a la izquierda si A[i] es mayor que el pivote
        while i >= 0 and A[i] > pivot:  
            # 5. Let Ai+1 ← Ai: Se desplaza A[i] una posición a la derecha para hacer espacio para el pivote
            A[i + 1] = A[i]  
            # 6. Let i ← i - 1: Se sigue revisando hacia la izquierda
            i -= 1 
        # 7. Let Ai+1 ← pivot: Se coloca el pivote en su posición correcta dentro del subarreglo ordenado
        A[i + 1] = pivot  
    return A  # Regresar lista ordenada
# Ejemplo de uso
A = [4, 1, 7, 2, 6, 3, 8, 5]
print("Lista original:", A)
sorted_A = insertion_sort(A)
print("Lista ordenada:", sorted_A) 