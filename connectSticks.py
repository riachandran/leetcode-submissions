from heapq import *
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1: return 0
        
        heapify(sticks)
        total = 0
        while len(sticks) > 1:
            stick1 = heappop(sticks)
            stick2 = heappop(sticks)
            cost = stick1+stick2
            total += cost
            heappush(sticks,cost)
            
        return total
