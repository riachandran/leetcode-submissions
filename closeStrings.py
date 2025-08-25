class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for w in word1:
            dict1[w] += 1

        for w2 in word2:
            dict2[w2] += 1

        if len(word1) != len(word2): return False
        if set(dict1.keys()) != set(dict2.keys()): return False
        if sorted(dict1.values()) != sorted(dict2.values()): return False

        return True
