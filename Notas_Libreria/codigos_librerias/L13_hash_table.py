from typing import TypeVar, Callable
from collections import namedtuple
from functools import partial

T = TypeVar("T")

Customer = namedtuple("Customer", ["name", "rfc", "address"])


# HASH CODE FUNCTION FOR CUSTOMER OBJECTS
def hash_code(e: Customer, m: int) -> int:
    """ Calcula el hash code de un objeto Customer a partir de su RFC. Se suma el valor ASCII de cada caracter y se aplica módulo m. """ 
    return sum(ord(c) for c in e.rfc) % m


class HashTable:
    def __init__(self, A: list[T], hash_code: Callable) -> None:
        self.table = {}
        self.hash_code = hash_code
        for e in A:
            self.insert(e)

    def __repr__(self) -> str:
        return str(self.table)

    def search(self, e: T) -> bool:
        """
        Retorna True si el elemento e se encuentra en la tabla hash; de lo contrario, False.
        """
        key = self.hash_code(e)
        if key in self.table:
            return e in self.table[key]
        return False

    def insert(self, e: T) -> bool:
        """
        Inserta el elemento e en la tabla hash.
        Retorna True si la inserción fue exitosa; False si el elemento ya existía.
        """
        key = self.hash_code(e)
        if key not in self.table:
            self.table[key] = [e]
            return True
        else:
            if e in self.table[key]:
                return False
            else:
                self.table[key].append(e)
                return True

    def delete(self, e: T) -> bool:
        """
        Elimina el elemento e de la tabla hash.
        Retorna True si se eliminó correctamente; False si no se encontró el elemento.
        """
        key = self.hash_code(e)
        if key in self.table and e in self.table[key]:
            self.table[key].remove(e)
            if not self.table[key]:
                del self.table[key]
            return True
        return False

if __name__ == "__main__":
    with open("Clientes.txt", "r") as f:
        customers = [
            Customer(*[e.strip() for e in l.split("\t")]) for l in f.readlines()
        ]

    hc = partial(hash_code, m=len(customers))
    ht = HashTable(customers, hc)
    print(ht)
    # {22: [Customer(name='...'...)...]...}
    print(ht.search(customers[0]))
    # True
    print(ht.insert(customers[0]))
    # False
    print(ht.delete(customers[0]))
    # True
    print(ht.delete(customers[0]))
    # False
    print(ht.insert(customers[0]))
    # True
