# Modificado a partir de L14_bst.py

class Node:
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BSTMap:
    def __init__(self):
        self.root = None

    def search_node(self, k):
        x = self.root
        while x and x.key != k:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def get(self, k):
        node = self.search_node(k)
        return node.value if node else None

    def put(self, k, v):
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
                x.value = v   # Actualiza valor si clave existe
                return
        z.parent = y
        if not y:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    # Opcional: mantener métodos mínimo y máximo…
    def minimum(self):
        x = self.root
        while x and x.left:
            x = x.left
        return (x.key, x.value) if x else None

    def maximum(self):
        x = self.root
        while x and x.right:
            x = x.right
        return (x.key, x.value) if x else None

# Ejemplo de uso
if __name__ == "__main__":
    # Instancia del mapa
    clientes = BSTMap()

    # Insertar varios clientes
    datos = [
      ("XAXX010101000", {"nombre":"Empresa A", "correo":"contacto@a.com"}),
      ("ABC123456789", {"nombre":"Juan Pérez",  "correo":"juan@dominio.mx"}),
      ("DEF987654321", {"nombre":"María López", "correo":"maria@dominio.mx"})
    ]
    for rfc, info in datos:
        clientes.put(rfc, info)

    # Buscar un cliente por RFC
    clave = "ABC123456789"
    resultado = clientes.get(clave)
    if resultado:
        print(f"Cliente {clave}: {resultado['nombre']}, email: {resultado['correo']}")
    else:
        print(f"RFC {clave} no encontrado.")
