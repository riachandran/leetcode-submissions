class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        i = 0
        minBuy = None
        maxSell = 0
        if len(prices) < 2: return 0
        else:
            for i in range(len(prices)-1):
                if prices[i] < prices[i+1] and minBuy == None:
                    minBuy = prices[i]
                if minBuy!= None:
                    if prices[i] < prices[i+1]:
                        maxSell = max(maxSell,prices[i+1])
                        if i+1 == len(prices)-1:
                            totalProfit += maxSell - minBuy
                            minBuy = None
                    else:
                        totalProfit += maxSell - minBuy
                        minBuy = None
                        maxSell = 0
                elif prices[i] > prices[i+1] and minBuy == None:
                    continue
        return totalProfit
