class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1+nums2)
        n = len(arr)
        if (n%2 == 0): return (arr[int(n/2)] + arr[int((n/2)-1)])/2
        else: return arr[int((n-1)/2)]
