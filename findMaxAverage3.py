class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lo = min(nums)
        hi = max(nums)

        def can(mid:float) -> bool:
            prefix = 0.0
            prev_prefix = 0.0
            min_prev = 0.0

            for i in range(k):
                prefix += nums[i] - mid

            if prefix >= 0: return True

            for j in range(k,len(nums)):
                prefix += nums[j] - mid
                prev_prefix += nums[j-k] - mid
                min_prev = min(min_prev,prev_prefix)
                if prefix - min_prev >= 0: return True

            return False

        while hi - lo > 1e-5:
            mid = (lo+hi)/2.0
            if can(mid):
                lo = mid
            else:
                hi = mid

        return lo
