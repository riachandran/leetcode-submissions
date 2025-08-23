class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        numd = {}
        for num in nums:
            if num in numd:
                numd[num] += 1
            else:
                numd[num] = 1

        return sum([d for d in numd if numd[d] == 1])
