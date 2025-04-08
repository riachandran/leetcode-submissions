class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        left = 0
        subs = set()

        for right in range(n):
            if s[right] not in subs:
                subs.add(s[right])
                max_len = max(right-left+1,max_len)
            else: 
                while s[right] in subs:
                    subs.remove(s[left])
                    left +=1
                subs.add(s[right])
        return max_len
