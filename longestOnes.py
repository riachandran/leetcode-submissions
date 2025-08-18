class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = left = 0
        curr = 0
        n = len(nums)
        if n <= k: return n
        for right in range(n):
            if nums[right] == 0:
                curr += 1
                
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
                
            ans = max(ans,right - left + 1)
            
        return ans
