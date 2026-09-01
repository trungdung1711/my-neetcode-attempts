class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # i
        # days as the number of days to ship packages
        # each day, load the ship with packages

        # o
        # least weight capacity of the ship
        # all packages on the conveyor being shipped within days days
        # each day, we load the packages in the order
        # we need to find the least weight, so that
        # we could finish the loading with [days]

        # c
        # len(weights) >= 1 <= 5 * 10^4
        # weights[i] >= 1 <= 500

        # e
        # len(weights) == 1 -> return that number

        # how can I make this problem
        # to a binary search problem
        # days = 3
        # divide the array into 4 parts -> return maximum value

        if days == 1:
            return sum(weights)

        res = float("inf")

        def dfs(w, n, capacity):
            nonlocal res
            
            if n == 1:
                # done dividing
                for i in range(1, len(w)):
                    p1 = w[0:i]
                    p2 = w[i:]

                    c = capacity + [sum(p1)] + [sum(p2)]

                    possible = max(c)

                    if possible < res:
                        res = possible

                return


            for i in range(1, len(w)):

                part = w[0:i]
                wei = sum(part)

                dfs(w[i:], n - 1, capacity + [wei])

        dfs(weights, days - 1, [])

        return res