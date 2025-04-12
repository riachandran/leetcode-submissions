class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     npop = nums.pop(-1)
        #     nums.insert(0,npop)
        # n = len(nums)
        # k = k % n
        # r = n - k
        # new = nums[0:r]
        # nums[0:r] = []
        # nums.extend(new)
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
