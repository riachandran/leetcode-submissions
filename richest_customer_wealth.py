class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_r = 0
        for i in accounts:
            if sum(i) > max_r: max_r = sum(i)
        return max_r
