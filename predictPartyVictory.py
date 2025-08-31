class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = [i for i,s in enumerate(senate) if s=='R']
        dir = [i for i,s in enumerate(senate) if s=='D']
        n = len(senate)
        while rad and dir:
            if rad[0] < dir[0]:
                rad.append(n)
            else:
                dir.append(n)

            n += 1
            rad.pop(0)
            dir.pop(0)

        return 'Radiant' if rad else 'Dire'    
