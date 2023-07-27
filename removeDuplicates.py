class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prevNo = None
        i,count,k = 0,0,0
        while count < len(nums):
            count += 1
            if nums[i] != prevNo:
                prevNo = nums[i]
                i+=1
                k+=1
            else:
                nums.remove(nums[i])
                nums.append('_')
        return k
