class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = list(sorted(set(nums)))[::-1][:3]
        if len(nums_set) < 3: return nums_set[0]
        return nums_set[-1]
