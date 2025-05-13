import heapq
from collections import Counter

def pqSort(strArray: list[str]) -> None:
    heapq.heapify(strArray)
    for i in range(len(strArray)):
        strArray[i] = heapq.heappop(strArray)

def hasDuplicates(strArray: list[str]) -> bool:
    seen = set()
    for word in strArray:
        if word in seen:
            return True
        seen.add(word)
    return False

def mode(intArray: list[int]) -> int:
    count = Counter(intArray)
    return count.most_common(1)[0][0]

