class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        
        # i
        # int array prices
        # prices[i] price of the i item
        # special discount
        # buy i -> prices[j]
        # j min index j > i and prices[j] <= prices[i]
        # otherwise no discount
        # i -> right j prices[j] < princes[i] -> discount

        # o
        # anser answer[i] final prices pay for the item of the shop

        # c
        # len(prices) >= 1 <= 500
        # prices[i] >= 1 <= 1000

        # e

        answer = [0 for _ in range(len(prices))]

        for i in range(0, len(prices) - 1):
            discount = 0
            for j in range(i + 1, len(prices)):

                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break

            answer[i] = prices[i] - discount

        answer[-1] = prices[-1]

        return answer