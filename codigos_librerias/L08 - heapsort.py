from enum import Enum
from typing import TypeVar, Callable

T = TypeVar("T")


def parent(i):
    return i >> 1


def left(i):
    return i << 1


def right(i):
    return (i << 1) + 1


class HeapType(Enum):
    MAX = 0
    MIN = 1


class Heap:
    def __init__(
        self,
        A: list[T],
        heapType: HeapType = HeapType.MAX,
        key: Callable = lambda x: x,
    ) -> None:
        self._heap = [None] + list(A)  # Make the array 1-indexed
        self._key = key
        self.heap_size = len(A)
        self.type = heapType
        self.build_heap()

    def __repr__(self):
        return str(self._heap[1 : self.heap_size + 1])

    def _compare_eq(self, a, b) -> bool:
        # Para Heap MAX: a debe ser mayor o igual que b
        # Para Heap MIN: a debe ser menor o igual que b
        return (
            self._key(a) >= self._key(b)
            if self.type == HeapType.MAX
            else self._key(a) <= self._key(b)
        )

    def assert_heap_property(self) -> None:
        for i in range(2, self.heap_size + 1):
            assert self._compare_eq(
                self._heap[parent(i)], self._heap[i]
            ), f"{self._heap[parent(i)]}, {self._heap[i]}, {self.type}"

    def heapify(self, i) -> None:
        l = left(i)
        r = right(i)
        extreme = i
        if l <= self.heap_size and not self._compare_eq(self._heap[extreme], self._heap[l]):
            extreme = l
        if r <= self.heap_size and not self._compare_eq(self._heap[extreme], self._heap[r]):
            extreme = r
        if extreme != i:
            self._heap[i], self._heap[extreme] = self._heap[extreme], self._heap[i]
            self.heapify(extreme)

    def build_heap(self) -> None:
        for i in range(self.heap_size // 2, 0, -1):
            self.heapify(i)

    def get_heap(self) -> list[T]:
        return self._heap[1 : self.heap_size + 1]


def heapsort(A: list[T], key: Callable = lambda x: x, reverse: bool = False) -> list[T]:
    """
    Ordena la lista A utilizando el algoritmo de heapshort. Para orden ascendente se utiliza min-heap; para descendente, un max heap
    """
    heap_type = HeapType.MIN if not reverse else HeapType.MAX 
    #Se crea una copia de A para no modificar el original.
    heap = Heap(A.copy(), heap_type, key)
    sorted_list = []
    while heap.heap_size > 0:
        sorted_list.append(heap._heap[1])
        heap._heap[1] = heap._heap[heap.heap_size]
        heap.heap_size -= 1
        heap.heapify(1)
    return sorted_list

if __name__ == "__main__":
    H = Heap([3, 2, 5, 1, 9, 0, 8, 6, 7, 4], HeapType.MIN)
    print(H)
    # [0, 1, 3, 2, 4, 5, 8, 6, 7, 9]
    H = Heap([3, 2, 5, 1, 9, 0, 8, 6, 7, 4], HeapType.MAX)
    print(H)
    # [9, 7, 8, 6, 4, 0, 5, 3, 1, 2]

    A = [3, 2, 5, 1, 9, 0, 8, 6, 7, 4]
    C = heapsort(A)
    print(C)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    C = heapsort(A, reverse=True)
    print(C)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    B = [(3, 8), (2, 0), (5, 5), (1, 6), (9, 3), (0, 2), (8, 1), (6, 4), (7, 9), (4, 7)]
    C = heapsort(B)
    print(C)
    # [(0, 2), (1, 6), (2, 0), (3, 8), (4, 7), (5, 5), (6, 4), (7, 9), (8, 1), (9, 3)]
    C = heapsort(B, key=lambda x: x[1])
    print(C)
    # [(2, 0), (8, 1), (0, 2), (9, 3), (6, 4), (5, 5), (1, 6), (4, 7), (3, 8), (7, 9)]
