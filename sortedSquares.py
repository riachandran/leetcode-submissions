class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        unsortedSquares = [i**2 for i in nums]
        return sorted(unsortedSquares)
