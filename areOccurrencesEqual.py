from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict()
        for char in s:
            if char not in count: count[char] = 1
            else: count[char] += 1
        
        if len(set(count.values()))==1: return True
        else: return False
