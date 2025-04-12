from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings: return []
        d = defaultdict(list)
        for s in strings:
            d[tuple((ord(c)-ord(s[0]))%26 for c in s)].append(s)
        
        return list(d.values())
