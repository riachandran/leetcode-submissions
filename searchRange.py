class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1,-1]
        first_occurence = nums.index(target)
        if target not in nums[first_occurence+1:]: return [first_occurence,first_occurence]
        else:last_occurence = len(nums) - 1 - nums[::-1].index(target)
        return [first_occurence,last_occurence]
