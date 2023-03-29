class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        maxResult = 0
        counter = 1
        sat_sorted = sorted(satisfaction)
        for i in range(0,len(sat_sorted)):
            currResult = 0
            for sat in sat_sorted[i:]:
                currResult += sat*counter
                counter += 1
            if currResult > maxResult: maxResult = currResult
            counter = 1
        return maxResult
       
