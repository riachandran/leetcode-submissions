class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckd = {}
        lucky = -1

        for num in arr:
            if num not in luckd: luckd[num] = 1
            else: luckd[num] += 1

        for l in luckd:
            if l == luckd[l]:
                lucky = max(lucky,l)

        return lucky
