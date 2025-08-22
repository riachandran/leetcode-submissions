class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        res = 0
        for num in arr:
            if num+1 in nums: res += 1
        return res
