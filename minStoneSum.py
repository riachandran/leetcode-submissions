from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones = [-stone for stone in piles]
        heapify(stones)
        while k > 0:
            heappush(stones,heappop(stones)//2)
            k -= 1
            
        return abs(sum(stones))
