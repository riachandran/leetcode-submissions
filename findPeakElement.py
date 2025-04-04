class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Last occurance of digit
        last = {digit:i for i,digit in enumerate(nums)}
        return last[max(k for k,v in last.items())]
