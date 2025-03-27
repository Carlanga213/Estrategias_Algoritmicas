# Función para crear una cola con capacidad inicial C
def create_queue(initial_capacity):
    return {"array": [None] * initial_capacity, "front": 0, "rear": 0, "size": 0, "capacity": initial_capacity}  # Inicializa la cola

def is_empty(queue):
    return queue["size"] == 0  # Retorna True si la cola está vacía

def is_full(queue):
    return queue["size"] == queue["capacity"]  # Retorna True si la cola está llena

def enqueue(queue, e):
    if is_full(queue):  # Si la cola está llena, duplicamos la capacidad
        new_capacity = 2 * queue["capacity"]
        new_array = [None] * new_capacity
        
        for i in range(queue["size"]):  # Copiamos los elementos en el nuevo arreglo
            new_array[i] = queue["array"][(queue["front"] + i) % queue["capacity"]]
        
        queue["array"] = new_array
        queue["front"] = 0
        queue["rear"] = queue["size"]
        queue["capacity"] = new_capacity
    
    queue["array"][queue["rear"]] = e  # Insertamos el nuevo elemento
    queue["rear"] = (queue["rear"] + 1) % queue["capacity"]  # Movemos rear circularmente
    queue["size"] += 1

def dequeue(queue):
    result = None
    if not is_empty(queue):  # Si la cola no está vacía
        result = queue["array"][queue["front"]]  # Obtenemos el dato del frente
        queue["front"] = (queue["front"] + 1) % queue["capacity"]  # Movemos el frente circularmente
        queue["size"] -= 1
    return result  # Retorna el dato eliminado o None si estaba vacía

def front(queue):
    return queue["array"][queue["front"]] if not is_empty(queue) else None  # Retorna el valor en el frente sin eliminarlo

def clear(queue):
    queue["front"] = 0  # Reiniciamos los índices y el tamaño
    queue["rear"] = 0
    queue["size"] = 0

# Creación de la cola y prueba
queue = create_queue(5)
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)

print(dequeue(queue))  # 10
print(dequeue(queue))  # 20
print(dequeue(queue))  # 30
print(dequeue(queue))  # None (cola vacía)