from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        p = (0,0)
        for point in points:
            x = (point[0] - p[0])**2
            y = (point[1] - p[1])**2
            heappush(heap,(-sqrt(x+y),point))
            if len(heap) > k:
                heappop(heap)
                
        return [point[1] for point in heap]
