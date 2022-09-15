class Solution(object):
    def removeDuplicates(self, nums):
        count = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
            else:
                continue
        return count
