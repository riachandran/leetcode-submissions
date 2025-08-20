class Solution:
    def reverseWords(self, s: str) -> str:
        str_array = [word[::-1] for word in s.split()]
        return " ".join(str_array)
