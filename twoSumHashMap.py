class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i,n in enumerate(nums):
            rem = target - n
            if rem in mp:
                return [mp[rem],i]
            mp[n] = i
