# Implementación de una lista utilizando un arreglo dinámico
def create_list(initial_capacity=10):
    return {"array": [None] * initial_capacity, "size": 0, "capacity": initial_capacity}  # Inicializa la lista con un tamaño y capacidad definidos

def append_to_list(lst, data):
    if lst["size"] >= lst["capacity"]:  # Si la lista está llena
        lst["capacity"] *= 2  # Duplica la capacidad
        new_array = [None] * lst["capacity"]  # Crea un nuevo arreglo más grande
        for i in range(lst["size"]):  # Copia los elementos al nuevo arreglo
            new_array[i] = lst["array"][i]
        lst["array"] = new_array  # Asigna el nuevo arreglo
    
    lst["array"][lst["size"]] = data  # Agrega el nuevo dato al final
    lst["size"] += 1  # Aumenta el tamaño de la lista

def display_list(lst):
    return [lst["array"][i] for i in range(lst["size"])]  # Retorna los elementos de la lista

# Prueba de lista con arreglo
array_list = create_list()
append_to_list(array_list, 10)
append_to_list(array_list, 20)
append_to_list(array_list, 30)
print(display_list(array_list))  # [10, 20, 30]
