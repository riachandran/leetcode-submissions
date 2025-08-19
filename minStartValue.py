class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 1
        while True:
            minstart = start
            is_valid = True
            for num in nums:
                minstart += num
                if minstart < 1: 
                    is_valid = False
                    break
                    
            if is_valid: return start
            else: start += 1
            
