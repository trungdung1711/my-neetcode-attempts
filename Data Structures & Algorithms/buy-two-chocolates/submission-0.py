class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        # i
        # prices = prices of various chocolates
        # a single integer money == initial amount of money
        # buy exactly 2 chocolates, remaining = non-negative
        # maximize the remaining, minimize the sum of the prices

        # o
        # the amount of money that you will have
        # leftover after buying
        # no way -> money

        # c
        # len(prices) >= 2 <= 50
        # prices[i] >= 1 <= 100
        # money >= 1 <= 100

        # e
        # [4, 5] -> must buy 2 of them

        # must buy 2 min values

        min_p = 101
        second_p = float("inf")

        for p in prices:

            if p < min_p:
                # find a value less than min_p
                tmp = min_p
                min_p = p
                second_p = tmp


            elif p > min_p and p < second_p:
                second_p = p

            elif p == min_p:
                second_p = p

        if money < (min_p + second_p):
            return money

        else:
            return money - min_p - second_p