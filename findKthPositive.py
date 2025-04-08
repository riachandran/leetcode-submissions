class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_numbers = []
        i= 1
        while len(missing_numbers) != k:
            if i not in arr: missing_numbers.append(i)
            i+=1
        return missing_numbers[k-1]
