class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1

        res = []

        for o in order:
            if o in s:
                res.append(o * mp[o])
        
        for l in s:
            if l not in order:
                res.append(l)

        return "".join(res)
