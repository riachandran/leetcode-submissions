class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        mp = {0:1}
        prefix = 0
        for num in nums:
            prefix += num
            ans += mp.get(prefix-goal,0)
            mp[prefix] = mp.get(prefix,0) + 1

        return ans
