# Se representa un nodo como un diccionario
def create_node(data):
    return {"data": data, "next": None}  # Crea un nodo con un dato y referencia al siguiente


# Se representa la cola como un diccionario con claves "front" y "rear"
def create_queue():
    return {"front": None, "rear": None}  # Inicializa la cola vacía


def is_empty(queue):
    return queue["front"] is None  # Retorna True si la cola está vacía


def enqueue(queue, d):
    new_node = create_node(d)  # Crea un nuevo nodo con el dato
    if is_empty(queue):  # Si la cola está vacía
        queue["front"] = new_node  # El frente y el final apuntan al nuevo nodo
        queue["rear"] = new_node
    else:
        queue["rear"]["next"] = new_node  # El último nodo apunta al nuevo nodo
        queue["rear"] = new_node  # Se actualiza el final de la cola


def dequeue(queue):
    result = None
    if not is_empty(queue):  # Si la cola no está vacía
        result = queue["front"]["data"]  # Se obtiene el dato del frente
        queue["front"] = queue["front"]["next"]  # Se mueve el frente al siguiente nodo
        if queue["front"] is None:  # Si la cola queda vacía, rear también debe ser None
            queue["rear"] = None
    return result  # Retorna el dato eliminado o None si estaba vacía

def front(queue):
    return queue["front"]["data"] if not is_empty(queue) else None  # Retorna el valor en el frente sin eliminarlo

def clear(queue):
    queue["front"] = None  # Vacía la cola
    queue["rear"] = None

# Creación de la cola y prueba
queue = create_queue()
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)

print(dequeue(queue))  # 10
print(dequeue(queue))  # 20
print(dequeue(queue))  # 30
print(dequeue(queue))  # None (cola vacía)
