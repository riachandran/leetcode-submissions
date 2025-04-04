class Solution:
    def maximumSwap(self, num: int) -> int:
        numb_list = [int(i) for i in str(num)]
        max_possible_outcome = []
        for i in range(0,len(numb_list)):
            for j in range(i,len(numb_list)):
                current_swap = numb_list.copy()
                current_swap[i],current_swap[j] = current_swap[j],current_swap[i]
                max_possible_outcome.append(int(''.join([str(i) for i in current_swap])))
                print(max_possible_outcome)
        return max(max_possible_outcome)
        
