class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loser = set()
        one_loser = set()
        more_loser = set()
        
        for winner,loser in matches:
            if winner not in one_loser and winner not in more_loser:
                zero_loser.add(winner)
            
            if loser in zero_loser:
                zero_loser.remove(loser)
                one_loser.add(loser)
            elif loser in one_loser:
                one_loser.remove(loser)
                more_loser.add(loser)
            elif loser in more_loser:
                continue
            else:
                one_loser.add(loser)
                
        return [sorted(list(zero_loser)),sorted(list(one_loser))]
