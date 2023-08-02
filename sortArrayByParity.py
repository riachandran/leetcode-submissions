class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,count = 0,0
        while count < len(nums):
            if nums[i] % 2 != 0:
                val = nums[i]
                nums.remove(val)
                nums.append(val)
            else:
                i+=1
            count+=1
        return nums
