# Función para crear una pila con capacidad inicial C
def create_stack(initial_capacity):
    return {"array": [None] * initial_capacity, "top": 0, "capacity": initial_capacity}  # Inicializa la pila

def top(stack):
    result = None  # 1: Inicializamos el resultado como None
    if stack["top"] != 0:  # 2: If top = 0, return null → Si la pila no está vacía
        result = stack["array"][stack["top"]]  # 3: return array[top] → Retorna el dato en la posición top
    return result  # 4: Retorna el dato o None si la pila está vacía

def pop(stack):
    result = None  # 1: Inicializamos el resultado como None
    if stack["top"] != 0:  # 2: If top = 0, return null → Si la pila no está vacía
        stack["top"] -= 1  # 3: Let top ← top - 1 → Disminuimos el valor de top
        result = stack["array"][stack["top"] + 1]  # 4: return array[top + 1] → Retorna el dato eliminado
    return result  # 5: Retorna el dato o None si la pila estaba vacía

def push(stack, e):
    stack["top"] += 1  # 1: Let top ← top + 1 → Aumentamos la posición de top

    if stack["top"] >= stack["capacity"]:  # 2: If top > C then → Verificamos si superamos la capacidad
        new_capacity = 2 * stack["capacity"]  # 3: Create newArray of length 2 * C → Duplicamos la capacidad
        new_array = [None] * new_capacity  # Creamos un nuevo arreglo con el doble de capacidad

        for k in range(stack["capacity"]):  # 4: For each k ← 1 to C: newArray_k ← array_k → Copiamos los elementos
            new_array[k] = stack["array"][k]

        stack["capacity"] = new_capacity  # 5: Let C ← 2 * C {free array} → Actualizamos la capacidad
        stack["array"] = new_array  # 6: Let array ← newArray → Asignamos el nuevo arreglo a la pila

    stack["array"][stack["top"]] = e  # 7: Let array[top] ← e → Insertamos el nuevo elemento en la pila

def is_empty(stack):
    result = stack["top"] == 0  # 1: Return top = 0 → Retorna True si la pila está vacía
    return result

def clear(stack):
    stack["top"] = 0  # 1: Let top ← 0 → Reiniciamos la pila sin eliminar los elementos del arreglo

# Creación de la pila y prueba
stack = create_stack(5)
push(stack, 10)
push(stack, 20)
push(stack, 30)

print(pop(stack))  # 30
print(pop(stack))  # 20
print(pop(stack))  # 10
print(pop(stack))  # None (pila vacía)
