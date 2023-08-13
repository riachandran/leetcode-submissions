class Solution:
    def reverseWords(self, s: str) -> str:
        string = [word for word in s.split(" ") if word!=""]
        return " ".join(string[::-1])
