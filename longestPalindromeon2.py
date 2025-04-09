class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        def expand(st,left,right):
            while left >= 0 and right < len(st) and st[left]==st[right]:
                left -= 1
                right += 1
            return st[left+1:right]
        res = ''
        for i in range(len(s)):
            res = max(res,expand(s,i,i),expand(s,i,i+1),key=len)
        return res
