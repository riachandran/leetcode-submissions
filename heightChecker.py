class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for x,y in zip(heights,sorted(heights)):
            if x != y : count +=1
        return count
