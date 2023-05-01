class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        l = len(mat1[0])
        n = len(mat2[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(0,m):
            for j in range(0,n):
                for k in range(0,l):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result
