class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,res1 =[],[]
        for i in range(len(nums)):
            if nums[i]>0: break
            if i == 0 or nums[i - 1] != nums[i]: 
                self.twoSum(nums,i,res)
        [res1.append(r) for r in res if r not in res1]
        return res1
    
    def twoSum(self, nums: List[int], i: int, res: List[int]):
        lo, hi = i + 1, len(nums) - 1
        while(lo < hi):
            tot = nums[i]+nums[lo]+nums[hi]
            if tot < 0: lo += 1
            elif tot > 0: hi -= 1
            else: 
                res.append([nums[i],nums[lo],nums[hi]]) 
                hi -= 1
                lo += 1
                if lo < hi and nums[lo] == nums[lo - 1]: lo += 1
