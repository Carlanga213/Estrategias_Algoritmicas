import random

def count_moves_heap(A):
    moves = 0
    def max_heapify(H, root, sz):
        nonlocal moves
        left, right = 2*root+1, 2*root+2
        largest = root
        if left < sz and H[left] > H[largest]:
            largest = left
        if right < sz and H[right] > H[largest]:
            largest = right
        if largest != root:
            H[root], H[largest] = H[largest], H[root]
            moves += 3
            max_heapify(H, largest, sz)
    # build
    n = len(A)
    for i in range(n//2-1, -1, -1):
        max_heapify(A, i, n)
    # sort
    for sz in range(n-1, 0, -1):
        A[0], A[sz] = A[sz], A[0]; moves += 3
        max_heapify(A, 0, sz)
    return moves

def count_moves_shell(A):
    moves = 0
    n = len(A)
    h = 1
    while h < n//3:
        h = 3*h + 1
    while h > 0:
        for i in range(h, n):
            temp = A[i]; moves += 1
            j = i
            while j >= h and A[j-h] > temp:
                A[j] = A[j-h]; moves += 1
                j -= h
            A[j] = temp; moves += 1
        h //= 3
    return moves

results = []
for N in range(1000, 10001, 100):
    sum_heap = sum_shell = 0
    runs = N // 10
    for _ in range(runs):
        data = [random.randint(1,10000) for _ in range(N)]
        sum_heap += count_moves_heap(data.copy())
        sum_shell += count_moves_shell(data.copy())
    results.append((N, sum_heap/runs, sum_shell/runs))
    print(N, sum_heap/runs, sum_shell/runs)

