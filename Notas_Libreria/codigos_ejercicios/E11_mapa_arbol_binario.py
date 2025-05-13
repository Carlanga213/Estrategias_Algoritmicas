class Nodo:
    def __init__(self, clave, valor, padre=None, izquierdo=None, derecho=None):
        self.clave = clave
        self.valor = valor
        self.padre = padre
        self.izquierdo = izquierdo
        self.derecho = derecho

class MapaABB:
    def __init__(self):
        self.raiz = None

    def buscar_nodo(self, clave):
        x = self.raiz
        while x and x.clave != clave:
            if clave < x.clave:
                x = x.izquierdo
            else:
                x = x.derecho
        return x

    def obtener(self, clave):
        nodo = self.buscar_nodo(clave)
        return nodo.valor if nodo else None

    def asignar(self, clave, valor):
        nuevo = Nodo(clave, valor)
        y = None
        x = self.raiz
        while x:
            y = x
            if nuevo.clave < x.clave:
                x = x.izquierdo
            elif nuevo.clave > x.clave:
                x = x.derecho
            else:
                x.valor = valor  # Actualiza si clave ya existe
                return
        nuevo.padre = y
        if not y:
            self.raiz = nuevo
        elif nuevo.clave < y.clave:
            y.izquierdo = nuevo
        else:
            y.derecho = nuevo

    def minimo(self):
        x = self.raiz
        while x and x.izquierdo:
            x = x.izquierdo
        return (x.clave, x.valor) if x else None

    def maximo(self):
        x = self.raiz
        while x and x.derecho:
            x = x.derecho
        return (x.clave, x.valor) if x else None
