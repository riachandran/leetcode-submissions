class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        last = None

        for num in arr:
            dic[num] += 1
            
        return len(dic) == len(set(dic.values()))
