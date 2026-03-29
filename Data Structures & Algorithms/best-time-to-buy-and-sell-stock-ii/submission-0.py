class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        for i in range(0,n-1):
            if prices[i]<prices[i+1]:
                profit = profit + (prices[i+1]-prices[i])
        return profit