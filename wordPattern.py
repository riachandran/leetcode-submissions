class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pairs = {}
        sl = s.split()
        if len(pattern) < len(sl) or len(pattern) > len(sl): return False

        for x,y in zip(pattern,sl):
            print(x,y)
            if x not in pairs:
                if y not in pairs.values():
                    pairs[x] = y
                else: return False
            else:
                if pairs[x] != y: return False

        return True
