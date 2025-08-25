class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairs = {}
        for x,y in zip(s,t):
            if x not in pairs:
                if y not in pairs.values():
                    pairs[x] = y
                else:
                    return False
            else:
                if pairs[x] != y: return False
        
        return True
