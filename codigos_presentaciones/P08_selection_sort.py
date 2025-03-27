def selection_sort(A):  
    for p in range(len(A) - 1):  # 1: For p ← 1 to A.length - 1 → Iteramos desde el primer hasta el penúltimo elemento de la lista
        min_idx = p  # 2: Let min ← p → Inicializamos el índice mínimo en la posición actual
        
        for i in range(p + 1, len(A)):  # 3: For i ← p + 1 to A.length → Iteramos sobre los elementos restantes de la lista
            if A[i] < A[min_idx]:  # 4: If A[i] < A[min] then → Si encontramos un elemento menor al actual mínimo
                min_idx = i  # 5: Let min ← i → Actualizamos el índice mínimo

        if p != min_idx:  # 6: If p ≠ min then {swap A[p] and A[min]} → Si el índice mínimo ha cambiado, intercambiamos los valores
            tmp = A[p]  # 7: Let tmp ← A[p] → Guardamos el valor de A[p] en una variable temporal
            A[p] = A[min_idx]  # 8: Let A[p] ← A[min] → Asignamos el valor mínimo a A[p]
            A[min_idx] = tmp  # 9: Let A[min] ← tmp → Asignamos el valor original de A[p] a A[min_idx]

    return A  # Retornamos la lista ordenada

# Ejemplo de uso
A = [64, 25, 12, 22, 11]
print(selection_sort(A))  # Salida esperada: [11, 12, 22, 25, 64]
