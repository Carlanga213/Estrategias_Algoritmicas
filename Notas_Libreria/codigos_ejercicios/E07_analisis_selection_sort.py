import random

def selection_cmp_mov(arr):
    cmp = 0
    mov = 0
    n = len(arr)
    for p in range(n-1):
        mn = p
        for i in range(p+1, n):
            cmp += 1
            if arr[i] < arr[mn]:
                mn = i
        if p != mn:
            arr[p], arr[mn] = arr[mn], arr[p]
            mov += 3
    return cmp, mov

# Experimento promedio
for n in range(1000, 5001, 100):
    sum_cmp = 0
    sum_mov = 0
    for _ in range(100):
        A = [random.randint(1,1000) for _ in range(n)]
        c, m = selection_cmp_mov(A)
        sum_cmp += c
        sum_mov += m
    print(n, sum_cmp/100, sum_mov/100)
