class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_table = []
        for i in arr:
            mul = i*2
            div = i/2
            if mul in hash_table or div in hash_table:
                return True
            else:
                hash_table.append(i)
        return False
