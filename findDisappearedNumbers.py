class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set =set(nums)
        runs = len(nums)+1
        result = []
        for i in range(1,runs):
            print(i)
            if i not in nums_set:
                result.append(i)
            i+=1
        return result
