# Implementación de una lista utilizando una lista enlazada con un iteradores
def create_node(data):
    return {"data": data, "next": None}  # Crea un nodo con un dato y referencia al siguiente

def create_list():
    return {"head": None}  # Inicializa la lista vacía

def append_to_list(lst, data):
    new_node = create_node(data)  # Crea un nuevo nodo con el dato
    if lst["head"] is None:  # Si la lista está vacía
        lst["head"] = new_node  # El nuevo nodo se convierte en la cabeza
    else:
        current = lst["head"]  # Se inicia desde la cabeza
        while current["next"] is not None:  # Se recorre hasta el último nodo
            current = current["next"]
        current["next"] = new_node  # Se enlaza el nuevo nodo al final

# Iterador para la lista enlazada usando una función
def linked_list_iterator(lst):
    current = lst["head"]
    while current is not None:
        yield current["data"]  # Devuelve el dato del nodo actual
        current = current["next"]  # Avanza al siguiente nodo

def display_list(lst):
    return [data for data in linked_list_iterator(lst)]  # Usamos el iterador para mostrar los elementos

# Prueba de lista enlazada con iterador
linked_list = create_list()
append_to_list(linked_list, 10)
append_to_list(linked_list, 20)
append_to_list(linked_list, 30)

print(display_list(linked_list))  # [10, 20, 30]
