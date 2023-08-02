class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        max_from_right = arr[size-1]
        
        arr[size-1] = -1

        for i in range(size-2,-1,-1):

            temp = arr[i]

            arr[i]=max_from_right

            if max_from_right< temp:
                max_from_right=temp
            
        return arr
