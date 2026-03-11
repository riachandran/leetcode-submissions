from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict()
        ans = []
        for num in nums:
            for n in num:
                if n in count: count[n] += 1
                else: count[n] = 1
            
                if count[n] == len(nums):
                    ans.append(n)
        
        
        return sorted(ans)
