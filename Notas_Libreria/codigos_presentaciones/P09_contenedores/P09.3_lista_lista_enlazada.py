# Implementación de una lista utilizando una lista enlazada
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

def display_list(lst):
    elements = []  # Lista para almacenar los datos
    current = lst["head"]  # Inicia desde la cabeza
    while current is not None:  # Recorre toda la lista
        elements.append(current["data"])  # Agrega el dato a la lista
        current = current["next"]  # Avanza al siguiente nodo
    return elements  # Retorna los elementos de la lista

# Prueba de lista enlazada
linked_list = create_list()
append_to_list(linked_list, 10)
append_to_list(linked_list, 20)
append_to_list(linked_list, 30)
print(display_list(linked_list))  # [10, 20, 30]
