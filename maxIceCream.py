class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bars = 0
        for cost in sorted(costs):
            if cost <= coins:
                bars += 1
                coins -= cost
        return bars
