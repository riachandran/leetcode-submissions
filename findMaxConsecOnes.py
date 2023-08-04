class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        left,right = 0,0
        zeroCount = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroCount +=1
            
            while zeroCount == 2:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxOnes = max(maxOnes,right - left + 1)
            right += 1

        return maxOnes       
