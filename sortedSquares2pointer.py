class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        pointer = len(nums)-1
        res = [0]*len(nums)
        while i<=j:
            if abs(nums[i]) > abs(nums[j]):
                res[pointer] = nums[i]**2
                i+=1
            else:
                res[pointer] = nums[j]**2
                j-=1
            pointer -=1
        return res
