class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # input: list of prices
        # task: maximize profit by choose one day to buy and one day to sell
        # output: max of profit

        # constraint
        # len(prices) >= 1

        # edge case
        # [ 4] -> 0
        # [3 2] -> 0

        # sol1: brute force

        # sol2:
        profit : int = 0
        # window to represent the lowest price
        # in the past
        min : int = prices[0]

        for i in range(1, len(prices)):
            candidate_profit = prices[i] - min
            if candidate_profit > profit:
                profit = candidate_profit
            
            if prices[i] <= min:
                min = prices[i]

        return profit