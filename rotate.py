class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 1
        while count <= k:
            num = nums[-1]
            nums.pop(-1)
            nums.insert(0,num)
            count+=1
        return nums
