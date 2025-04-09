class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        idx = len(nums)//2
        if len(nums) % 2 == 0:
            return (nums[idx-1]+nums[idx]) / 2
        else:
            return nums[idx]
