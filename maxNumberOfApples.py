class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        limit = 0
        sumw = 0
        for i in range(len(weight)):
            sumw += weight[i]
            if sumw <= 5000: 
                limit += 1
        return limit
