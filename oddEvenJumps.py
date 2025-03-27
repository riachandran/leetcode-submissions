class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        #memoization
        #next odd jump indices
        stack =[]
        next_odd_jump = [0]*n
        for index,value in sorted(enumerate(arr),key=lambda x:x[1]):
            while stack and stack[-1] < index:
                next_odd_jump[stack.pop()] = index
            stack.append(index)
            
        #next even jump indices
        stack =[]
        next_even_jump = [0]*n
        for index,value in sorted(enumerate(arr),key=lambda x:x[1],reverse=True):
            while stack and stack[-1] < index:
                next_even_jump[stack.pop()] = index
            stack.append(index)
        
        
        #use the jump indices to see if each index can odd-start & even-start to position n-1
        odd_start_good = [0]*n
        even_start_good = [0]*n
        
        #base class for dp
        odd_start_good[n-1] = 1
        even_start_good[n-1] = 1
        for i in range(n-2,-1,-1):
            i_next_odd = next_odd_jump[i]
            if i_next_odd and even_start_good[i_next_odd]:
                odd_start_good[i] = 1
            i_next_even = next_even_jump[i]
            if i_next_even and odd_start_good[i_next_even]:
                even_start_good[i] = 1
        
        #return sum of 1s in odd-start-good
        return sum(odd_start_good)
        
