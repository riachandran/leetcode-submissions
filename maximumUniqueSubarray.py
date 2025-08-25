class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mp = set()
        left = curr = res = 0
        for right in range(len(nums)):
            while nums[right] in mp:
                mp.remove(nums[left])
                curr -= nums[left]
                left += 1

            mp.add(nums[right])
            curr += nums[right]
            res = max(res,curr)

        return res
