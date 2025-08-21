class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        current_count = 0
        
        for i in range(k):
            if s[i] in vowels: current_count += 1

            ans = current_count

        for i in range(k,len(s)):
            if s[i] in vowels: current_count += 1
            if s[i-k] in vowels: current_count -= 1
            ans = max(ans,current_count)

            if ans == k: return k

        return ans
