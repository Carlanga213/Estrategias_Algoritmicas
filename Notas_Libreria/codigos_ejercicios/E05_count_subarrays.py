// count_subarrays(array: list[int], min_: int, max_: int) -> int
def count_subarrays(array: list[int], min_: int, max_: int) -> int:
    count = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            holds = True
            for k in range(i, j+1):
                # <-- esta es la expresión a contar
                if array[k] < min_ or array[k] > max_:
                    holds = False
                    break
            if holds:
                count += 1
    return count
