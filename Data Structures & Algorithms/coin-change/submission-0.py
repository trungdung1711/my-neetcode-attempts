class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # input
        # array of coins
        # coins of different denominations
        # anount -> a total amount of money

        # output
        # fewest number of coins
        # that you need to make up that amount
        # can not be made up, return -1
        # infinite number of each kind of coin

        # constraints
        # len(coins) >= 1 <= 12
        # coins[i] >= 1 <= 2^31 - 1
        # amount >= 0 <= 10^4

        # edge cases
        # amount = 0 -> return 0
        # anoumt = 2 but coins = [1] -> return -1

        # amount : number of fewest coins
        mem = {
            0 : 0
        }

        def dfs(coins : List[int], amount : int):

            if amount in mem:
                return mem[amount]
            
            if amount == 0:
                # sucessfully pick coins
                return 0

            if amount < 0:
                # fail to pick coins
                return -1


            min_picks = []

            for coin in coins:
                min_pick = dfs(coins, amount - coin)

                if min_pick == -1:
                    # fail
                    None
                
                else:
                    min_picks += [min_pick]

            if len(min_picks) == 0:
                # all coin pick can't make amount == 0
                fewest = -1

            else:
                fewest = 1 + min(min_picks)

            mem[amount] = fewest

            return mem[amount]

        dfs(coins, amount)

        return mem[amount]