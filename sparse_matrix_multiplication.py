class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        n = len(mat2[0])
        out = []
        if (len(mat1[0]) == len(mat2)):
            k = len(mat1[0])
            for ik,iv in enumerate(mat1):
                print(iv)
                temp =[]
                for a in range(0,n):
                    sum = 0
                    for b in range(0,k):
                        sum += mat1[ik][b]*mat2[b][a]
                    temp.append(sum)
                out.append(temp)
            return out
