class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jeweld = defaultdict(int)
        for j in jewels:
            jeweld[j] += 1
            
        count = 0
        for s in stones:
            if jeweld[s]:
                count += 1
                
        return count
