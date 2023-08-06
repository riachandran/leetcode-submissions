class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_nums = {}
        result = len(nums)
        i = 0
        count = 0
        while count < len(nums):
            if nums[i] not in hash_nums: 
                hash_nums[nums[i]] = 1
                i+=1
            else:
                hash_nums[nums[i]]+=1
                if hash_nums[nums[i]] > 2: 
                    nums.append('_')
                    nums.remove(nums[i])
                    result -= 1
                    count+=1
                    continue
                i+=1
            count+=1
        return result
