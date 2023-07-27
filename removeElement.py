class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k,i,count = 0,0,0
        while count < len(nums):
            count += 1
            if nums[i] != val:
                i+=1
                k+=1
            else:
                nums.remove(nums[i])
                nums.append("_")     
        return k
