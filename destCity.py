class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startcity = set()

        for start,end in paths:
            startcity.add(start)

        for start,end in paths:
            if end not in startcity: return end
            
