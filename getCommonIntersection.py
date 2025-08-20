class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        result = min(list(set(nums1) & set(nums2))) if list(set(nums1) & set(nums2)) != [] else -1
        return result
