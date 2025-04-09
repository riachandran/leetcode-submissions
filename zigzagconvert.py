class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows: return s
        finalStr = [[] for i in range(numRows)]
        idx,d= 0,1
        for char in s:
            finalStr[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        
        finalStr = ''.join([''.join(row) for row in finalStr])
        return finalStr
