from collections import Counter
from heapq import *
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(letter),count) for letter,count in Counter(s).items()]
        heapify(max_heap)
        result = []

        while max_heap:
            neg_char,count = heappop(max_heap)
            char = chr(-neg_char)
            use = min(count,repeatLimit)
            result.append(char*use)

            if count > use and max_heap:
                next_neg_char, next_count = heappop(max_heap)
                result.append(chr(-next_neg_char))
                if next_count > 1:
                    heappush(max_heap,(next_neg_char,next_count - 1))

                heappush(max_heap,(neg_char,count - use))

        return "".join(result)
