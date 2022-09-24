class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        output = []
        rev_mtr = list(reversed(matrix))
        for i in range(len(matrix[0])):
            tmp = []
            for l in rev_mtr:
                tmp.append(l[i])
            matrix[i] = tmp
