class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word = defaultdict(int)
        rn = defaultdict(int)
     
        for ch in magazine:
            word[ch] += 1
            
        for r in ransomNote:
            if word[r]:
                word[r] -= 1
            else:
                return False
            
        return True
