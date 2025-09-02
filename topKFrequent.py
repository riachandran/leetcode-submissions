from collections import Counter
from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = [(-val,key) for key,val in counts.items()]
        heapify(heap)

        return [heappop(heap)[1] for _ in range(k)]
