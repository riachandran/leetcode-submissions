class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sumLeft = 0
        for i in range(len(nums)):
            if total - nums[i] - sumLeft == sumLeft: return i
            sumLeft += nums[i]
        
        return -1
