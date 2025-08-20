class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            idx = word.index(ch)
            final = word[0:idx+1][::-1]+word[idx+1:]
            return "".join(final)
        else:
            return word
