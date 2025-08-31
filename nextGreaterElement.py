class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = [-1]*len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i]) + 1
            while idx < len(nums2):
                if nums2[idx] > nums1[i]:
                    output[i] = nums2[idx]
                    break
                idx+=1
            
        return output
