class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set()
        for ch in sentence:
            alphabet.add(ch)
        if len(alphabet) == 26: return True
        else: return False
