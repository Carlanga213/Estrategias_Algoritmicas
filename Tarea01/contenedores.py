#a)/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None
    
    def is_empty(self):
        return not self.stack1 and not self.stack2

# Complejidad de operaciones:
# - Enqueue: O(1), ya que simplemente agregamos un elemento a stack1.
# - Dequeue: O(n) en el peor caso cuando stack2 está vacío y se transfieren elementos de stack1.
# - Complejidad amortizada: O(1) ya que cada elemento se mueve solo una vez entre las pilas.

# Ejemplo de uso
queue = QueueWithStacks()
queue.enqueue(10)
queue.enqueue(42)
queue.enqueue(73)
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
queue.enqueue(47)
print(queue.dequeue())  # 3
print(queue.dequeue())  # 4

#b)/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class StackWithQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self, item):
        self.queue1.append(item)
    
    def pop(self):
        if not self.queue1:
            return None  # La pila está vacía
        
        # Mover todos los elementos excepto el último a queue2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        # El último elemento es el que se debe eliminar (simula un pop de pila)
        popped_item = self.queue1.pop(0)
        
        # Intercambiar queue1 y queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_item
    
    def is_empty(self):
        return not self.queue1

# Complejidad de operaciones:
# - Push: O(1), ya que simplemente agregamos un elemento a queue1.
# - Pop: O(n) en el peor caso, ya que debemos mover elementos entre las colas.
# - Complejidad amortizada: O(n), porque cada elemento se mueve solo una vez antes de ser eliminado.

# Ejemplo de uso
stack = StackWithQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3
print(stack.pop())  # 2
stack.push(4)
print(stack.pop())  # 4
print(stack.pop())  # 1

#c)/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Guardamos el siguiente nodo
            current.next = prev  # Invertimos el enlace
            prev = current  # Movemos prev hacia adelante
            current = next_node  # Movemos current hacia adelante
        self.head = prev  # La nueva cabeza es el último nodo procesado

# Complejidad de operaciones:
# - Invertir la lista: θ(n), ya que recorremos la lista solo una vez.
# - Uso de memoria adicional: O(1), ya que solo usamos tres punteros auxiliares.

# Ejemplo de uso
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.print_list()  # 1 -> 2 -> 3 -> 4 -> None
linked_list.reverse()
linked_list.print_list()  # 4 -> 3 -> 2 -> 1 -> None
