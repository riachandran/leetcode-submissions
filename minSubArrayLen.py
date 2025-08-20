class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        ans = float('inf')
        temp = 0
        for j in range(len(nums)):
            temp += nums[j]
            while temp >= target:
                ans = min(ans,j-i+1)
                temp -= nums[i]
                i+=1

        if ans == float('inf'): return 0
        else: return ans
