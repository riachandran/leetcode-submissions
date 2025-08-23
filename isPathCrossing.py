class Solution:
    def isPathCrossing(self, path: str) -> bool:
        start = defaultdict(int)
        spoint = [0,0]
        count = 0
        p = 0
        start[tuple(spoint)] = 1

        for p in path:
            if p == 'N': spoint[1] += 1 
            elif p == 'E': spoint[0] += 1
            elif p == 'S': spoint[1] -= 1
            else:
                spoint[0] -= 1

            if tuple(spoint) not in start:
                start[tuple(spoint)] += 1 
            else:
                return True

        return False
