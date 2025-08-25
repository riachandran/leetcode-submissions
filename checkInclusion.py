class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1 = sorted(s1)

        for i in range(len(s2)-window+1):
            if s1 == sorted(s2[i:i+window]): return True

        return False
