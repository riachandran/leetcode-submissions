class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        if len(arr) < 2: return False

        while arr[i] < arr[i+1] and i < len(arr)-2:
            i+=1
        
        if arr[i] == arr[i+1] or i == 0:
            return False
        
        while arr[i] > arr[i+1]:
            i+=1
            if i == len(arr) - 1: return True
        
        return False
