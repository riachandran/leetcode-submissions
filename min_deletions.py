from collections import Counter
class Solution:
    
    def minDeletions(self, s: str) -> int:
        sdict = Counter(s.lower())
        sdict_sorted_list = sorted([k for k in sdict.values()])
        counter = 0
        while len(set(sdict_sorted_list)) != len(sdict_sorted_list):
            sdict_sorted_list = list(filter(lambda x: x != 0,sdict_sorted_list))
            for i in range(0,len(sdict_sorted_list)-1):
                if sdict_sorted_list[i] == sdict_sorted_list[i+1]:
                    sdict_sorted_list[i] -= 1
                    counter += 1
        return counter
