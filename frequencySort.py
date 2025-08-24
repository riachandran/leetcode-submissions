class Solution:
    def frequencySort(self, s: str) -> str:
        mp = defaultdict(int)
        res = []
        for ch in s:
            mp[ch] += 1

        mp = sorted(mp.items(),key= lambda kv: kv[1],reverse=True)
        for k,v in enumerate(mp):
            print(v,k)
            res.append(v[0]*v[1])

        return "".join(res)
