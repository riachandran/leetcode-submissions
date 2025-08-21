class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixs = [0]
        for g in gain:
            prefixs.append(g + prefixs[-1])

        return max(prefixs)
