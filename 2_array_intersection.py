class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        largest = nums1 if len(nums1)>len(nums2) else nums2
        smallest = nums1 if len(nums1)<len(nums2) else nums2
        for i in largest:
            if i in smallest: result.append(i)
        return set(result)
