from typing import TypeVar, Callable
from collections import namedtuple
from functools import partial

T = TypeVar("T")

# Cliente como namedtuple
Customer = namedtuple("Customer", ["name", "rfc", "address"])

# Función hash usando método de Horner
def hash_code(e: Customer, m: int) -> int:
    base = 36
    code = 0
    for c in e.rfc:
        if c.isdigit():
            num = ord(c) - ord('0')
        else:
            num = ord(c) - ord('A') + 10
        code = (code * base + num) % m
    return code

# Clase HashTable con chaining
class HashTable:
    def __init__(self, A: list[T], hash_code: Callable) -> None:
        self.table = {}
        self.hash_code = hash_code
        for e in A:
            self.insert(e)

    def __repr__(self) -> str:
        return str(self.table)

    def insert(self, e: T) -> bool:
        key = self.hash_code(e)
        if key not in self.table:
            self.table[key] = [e]
            return True
        elif e in self.table[key]:
            return False
        else:
            self.table[key].append(e)
            return True

    def search(self, e: T) -> bool:
        key = self.hash_code(e)
        return key in self.table and e in self.table[key]

    def delete(self, e: T) -> bool:
        key = self.hash_code(e)
        if key in self.table and e in self.table[key]:
            self.table[key].remove(e)
            if not self.table[key]:
                del self.table[key]
            return True
        return False

# Prueba principal
if __name__ == "__main__":
    with open("Clientes.txt", "r", encoding="utf-8") as f:
        customers = [
            Customer(*[e.strip() for e in l.split("\t")]) 
            for l in f.readlines()
            if len(l.split("\t")) >= 3
        ]

    hc = partial(hash_code, m=len(customers))
    ht = HashTable(customers, hc)

    print(ht)
    print(ht.search(customers[0]))  # True
    print(ht.insert(customers[0]))  # False
    print(ht.delete(customers[0]))  # True
    print(ht.delete(customers[0]))  # False
    print(ht.insert(customers[0]))  # True
