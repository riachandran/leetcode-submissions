class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = defaultdict()
        for num in nums:
            if num not in count.keys():
                count[num] = 1
            else:
                count[num] += 1
                
        res = [k for k,v in count.items() if v == 1]
        if res: return max(res)
        else: return -1
