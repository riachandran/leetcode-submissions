class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes,currMax = 0,0
        for i in nums:
            if i == 1: currMax +=1
            else:
                maxOnes = max(maxOnes,currMax)
                currMax = 0
        maxOnes = max(maxOnes,currMax)
        return maxOnes 
