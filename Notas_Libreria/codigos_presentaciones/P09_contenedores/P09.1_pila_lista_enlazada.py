# Se representa un nodo como un diccionario
def create_node(data, prior):
    return {"data": data, "prior": prior}  # Crea un nodo con un dato y referencia al anterior

# Se representa la pila como un diccionario con clave "top"
def create_stack():
    return {"top": None}  # Inicializa la pila vacía

def top(stack):
    result = None  # 1: Inicializa el resultado como None
    if stack["top"] is not None:  # 2: Si la pila no está vacía
        result = stack["top"]["data"]  # 3: Retorna el dato del nodo en la cima
    return result  # 4: Retorna el valor

def is_empty(stack):
    result = stack["top"] is None  # 1: Retorna True si la pila está vacía
    return result

def push(stack, d):
    new_node = create_node(d, stack["top"])  # 1-3: Crea un nuevo nodo con el dato y lo enlaza con top
    stack["top"] = new_node  # 4: Let top ← n → Actualiza top para que apunte al nuevo nodo

def pop(stack):
    result = None  # 1: Inicializa el resultado como None
    if stack["top"] is not None:  # 2: Si la pila no está vacía
        result = stack["top"]["data"]  # 3: Guarda el dato del nodo superior
        stack["top"] = stack["top"]["prior"]  # 4: top ← top.prior → Mueve top al nodo anterior
    return result  # 5: Retorna el dato eliminado o None si estaba vacía

def clear(stack):
    stack["top"] = None  # 1: Let top ← null → Vacía la pila en un lenguaje con recolección de basura

    while stack["top"] is not None:  # 2: While top ≠ null → Mientras la pila no esté vacía
        temp = stack["top"]  # 3: Guarda el nodo actual antes de eliminarlo
        stack["top"] = stack["top"]["prior"]  # 4: Let top ← top.prior → Mueve top al nodo anterior
        del temp  # 5: Free(top) → Libera la memoria del nodo (simula free en C/C++)

# Creación de la pila y prueba
stack = create_stack()
push(stack, 10)
push(stack, 20)
push(stack, 30)

print(pop(stack))  # 30
print(pop(stack))  # 20
print(pop(stack))  # 10
print(pop(stack))  # None (pila vacía)
