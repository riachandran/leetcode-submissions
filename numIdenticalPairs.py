class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for num in nums:
            mp[num] +=1

        ans = 0
        for m in mp:
            ans += (mp[m] * (mp[m] -1)) // 2 

        return ans
