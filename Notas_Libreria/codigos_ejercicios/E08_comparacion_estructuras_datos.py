import time
import random
import array
from collections import deque

N = 100_000

# Ejercicio 1 y 2: Crear array y list
start = time.time()
arr = array.array('f', [k + random.random() for k in range(N)])
end = time.time()
print(f"Tiempo array: {end - start:.4f} s")
start = time.time()
lst = [k + random.random() for k in range(N)]
end = time.time()
print(f"Tiempo list: {end - start:.4f} s")

# Ejercicio 3 y 4: Promedio con índice
start = time.time()
prom_arr = sum([arr[i] for i in range(N)]) / N
end = time.time()
print(f"Promedio array [i]: {end - start:.4f} s")
start = time.time()
prom_lst = sum([lst[i] for i in range(N)]) / N
end = time.time()
print(f"Promedio list [i]: {end - start:.4f} s")

# Ejercicio 5: Promedio con for-each
start = time.time()
prom_arr2 = sum(arr) / N
end = time.time()
print(f"Promedio array for-each: {end - start:.4f} s")
start = time.time()
prom_lst2 = sum(lst) / N
end = time.time()
print(f"Promedio list for-each: {end - start:.4f} s")

# Ejercicio 6 y 7: Inserciones
lst_a = lst.copy()
k = 0
start = time.time()
while k < len(lst_a):
    lst_a.insert(k + 1, lst_a[k] + random.random()/4)
    k += 2
end = time.time()
print(f"Inserción en ArrayList: {end - start:.4f} s")
linked = deque(lst)
k = 0
start = time.time()
while k < len(linked):
    linked.insert(k + 1, linked[k] + random.random()/4)
    k += 2
end = time.time()
print(f"Inserción en LinkedList: {end - start:.4f} s")

