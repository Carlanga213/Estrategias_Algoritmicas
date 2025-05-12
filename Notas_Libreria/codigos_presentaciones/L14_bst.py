# L14_bst_map.py
# Version adaptada para actuar como mapa clave→valor usando ABB

class Node:
    def __init__(self, key, value=None, parent=None, left=None, right=None):
        self.key    = key
        self.value  = value
        self.parent = parent
        self.left   = left
        self.right  = right

class BSTMap:
    def __init__(self):
        self.root = None

    def search_node(self, k):
        """Devuelve el nodo con clave k o None si no existe."""
        x = self.root
        while x and x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def get(self, k):
        """Retorna el valor asociado a k, o None si no está."""
        node = self.search_node(k)
        return node.value if node else None

    def put(self, k, v):
        """
        Inserta la pareja (k, v) en el árbol.
        Si k ya existía, reemplaza su valor por v.
        """
        z = Node(k, v)
        y = None
        x = self.root
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            elif z.key > x.key:
                x = x.right
            else:
                # La clave ya existe: actualizamos y salimos
                x.value = v
                return
        z.parent = y
        if y is None:
            # Árbol vacío → nuevo nodo raíz
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def minimum(self):
        """Devuelve (clave, valor) del nodo mínimo, o None si el árbol está vacío."""
        x = self.root
        if x is None:
            return None
        while x.left:
            x = x.left
        return (x.key, x.value)

    def maximum(self):
        """Devuelve (clave, valor) del nodo máximo, o None si el árbol está vacío."""
        x = self.root
        if x is None:
            return None
        while x.right:
            x = x.right
        return (x.key, x.value)

    # Con esto podriamos añadir aqui otros metodos: delete, successor, predecessor, recorridos, etc.


if __name__ == "__main__":
    # Ejemplo de uso: clientes indexados por RFC
    clientes = BSTMap()

    # Insertar algunos clientes
    datos = [
        ("XAXX010101000", {"nombre": "Empresa A",   "correo": "contacto@a.com"}),
        ("ABC123456789",  {"nombre": "Juan Pérez",  "correo": "juan@dominio.mx"}),
        ("DEF987654321",  {"nombre": "María López", "correo": "maria@dominio.mx"}),
    ]
    for rfc, info in datos:
        clientes.put(rfc, info)

    # Obtener un cliente
    clave = "ABC123456789"
    resultado = clientes.get(clave)
    if resultado is not None:
        print(f"Cliente {clave}: {resultado['nombre']}, email: {resultado['correo']}")
    else:
        print(f"RFC {clave} no encontrado.")

    # Mostrar MIN & MAX
    print("Cliente con RFC mínimo:", clientes.minimum())
    print("Cliente con RFC máximo:", clientes.maximum())
