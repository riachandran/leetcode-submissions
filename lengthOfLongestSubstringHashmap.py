class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        ans = left = 0
        
        for right in range(len(s)):
            if not mp[s[right]]:
                mp[s[right]] += 1
                ans = max(ans,right-left+1)
            else:
                while mp[s[right]]:
                    mp[s[left]] -= 1
                    left += 1
                mp[s[right]] += 1
                
        return ans
