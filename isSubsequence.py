class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s in t: return True
        counter = 0
        string = []
        i=0
        while counter < len(s) and i < len(t):
            if t[i] in s:
                if s[counter] == t[i]: 
                    counter += 1
                    string.append(t[i])
            i+=1
        if ''.join(string) == s: return True
        else: return False
