class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        l = 0
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        currCost = 0

        for r in range(len(s)):
            currCost += diff[r]
            if currCost <= maxCost:
                ans = r - l + 1
            else:
                currCost -= diff[l]
                l += 1
        return ans
