class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        iterator = iter(range(len(arr)-1))
        for idx in iterator:
            if arr[idx]==0:
                if idx < len(arr)- 2:
                    arr[idx+1:]=arr[idx:len(arr)-1]
                    next(iterator)
                else:
                    arr[idx+1:]=arr[idx:len(arr)-1]
