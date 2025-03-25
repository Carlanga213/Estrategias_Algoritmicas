# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

def print_young_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(str(tablero[i][j]) if tablero[i][j] != float('inf') else "0", end="\t")
        print()

def create_young_tablero(elements, m, n):
    tablero = [[float('inf')] * n for _ in range(m)]
    elements = sorted(elements)[:m * n]  # Asegurar que solo se toman los elementos necesarios
    
    index = 0
    for i in range(m):
        for j in range(n):
            if index < len(elements):
                tablero[i][j] = elements[index]
                index += 1
    
    return tablero

def is_young_tablero_empty(tablero):
    return tablero[0][0] == float('inf')

def is_young_tablero_full(tablero, m, n):
    return tablero[m-1][n-1] < float('inf')

def extract_min_young(tablero, m, n):
    if is_young_tablero_empty(tablero):
        return None  # No hay elementos que extraer
    
    min_val = tablero[0][0]  # El mínimo siempre está en la esquina superior izquierda
    tablero[0][0] = float('inf')  # Marcar la celda como vacía
    
    def youngify(i, j):
        smallest_i, smallest_j = i, j
        if i + 1 < m and tablero[i + 1][j] < tablero[smallest_i][smallest_j]:
            smallest_i, smallest_j = i + 1, j
        if j + 1 < n and tablero[i][j + 1] < tablero[smallest_i][smallest_j]:
            smallest_i, smallest_j = i, j + 1
        
        if (smallest_i, smallest_j) != (i, j):
            tablero[i][j], tablero[smallest_i][smallest_j] = tablero[smallest_i][smallest_j], tablero[i][j]
            youngify(smallest_i, smallest_j)
    
    youngify(0, 0)
    return min_val

def insert_into_young_tablero(tablero, m, n, value):
    if is_young_tablero_full(tablero, m, n):
        print("El tablero está lleno, no se puede insertar.")
        return
    
    tablero[m-1][n-1] = value  # Insertar el nuevo valor en la última celda
    
    def bubble_up(i, j):
        largest_i, largest_j = i, j
        if i > 0 and tablero[i-1][j] > tablero[largest_i][largest_j]:
            largest_i, largest_j = i-1, j
        if j > 0 and tablero[i][j-1] > tablero[largest_i][largest_j]:
            largest_i, largest_j = i, j-1
        
        if (largest_i, largest_j) != (i, j):
            tablero[i][j], tablero[largest_i][largest_j] = tablero[largest_i][largest_j], tablero[i][j]
            bubble_up(largest_i, largest_j)
    
    bubble_up(m-1, n-1)

def young_sort(tablero, m, n):
    sorted_list = []
    tablero_copy = [row[:] for row in tablero]  # Crear una copia del tablero
    
    for _ in range(m * n):
        sorted_list.append(extract_min_young(tablero_copy, m, n))
    
    return sorted_list

def search_in_young_tablero(tablero, m, n, target):
    for i in range(m):
        for j in range(n):
            if tablero[i][j] == target:
                return True
    return False

# Elementos dados
elements = [9, 16, 3, 2, 4, 8, 5, 14, 12]

# Crear e imprimir el tablero de Young
young_tablero = create_young_tablero(elements, 4, 4)
print_young_tablero(young_tablero)

# Verificar si el tablero está vacío o lleno
print("El tablero está vacío:", is_young_tablero_empty(young_tablero))
print("El tablero está lleno:", is_young_tablero_full(young_tablero, 4, 4))

# Extraer el elemento mínimo
elemento_minimo = extract_min_young(young_tablero, 4, 4)
print("Elemento mínimo extraído:", elemento_minimo)
print("Tablero después de extraer el mínimo:")
print_young_tablero(young_tablero)

# Insertar un nuevo elemento
insert_into_young_tablero(young_tablero, 4, 4, 7)
print("Tablero después de insertar 7:")
print_young_tablero(young_tablero)

# Ordenar usando el tablero de Young sin modificarlo
sorted_elements = young_sort(young_tablero, 4, 4)
print("Lista ordenada con el tablero de Young:", sorted_elements)

# Prueba de búsqueda en el tablero
target = 8
found = search_in_young_tablero(young_tablero, 4, 4, target)
print(f"El número {target} está en el tablero:", found)

target = 15
found = search_in_young_tablero(young_tablero, 4, 4, target)
print(f"El número {target} está en el tablero:", found)
