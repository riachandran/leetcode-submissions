from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = curr = 0
        count = defaultdict(int)
        count[0] = 1
        for num in nums:
            curr += num
            ans += count[curr - k]
            count[curr] += 1

        return ans
