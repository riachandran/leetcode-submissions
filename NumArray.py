class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixs = [self.nums[0]]
        for i in range(1,len(self.nums)):
            self.prefixs.append(self.nums[i]+self.prefixs[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixs[right] - self.prefixs[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
