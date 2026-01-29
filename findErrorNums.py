class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tot = n*(n+1) // 2
        unique = sum(set(nums))
        tot_sum = sum(nums)

        return [tot_sum - unique, tot - unique]
