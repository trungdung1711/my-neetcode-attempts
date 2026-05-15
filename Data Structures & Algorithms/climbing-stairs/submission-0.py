class Solution:
    def climbStairs(self, n: int) -> int:
        
        # input
        # n steps to reach the top
        # each time 1 or 2 steps
        # distinct way you can climb to reach
        # the top


        # ouput
        # how many distinct ways you can climb
        # to reach the top

        # constraints
        # n >= 1 n <= 45
        # reach the top

        # edge case
        # n == 1 -> return 1
        # n == 2 -> return 2

        self.result = 0

        self.dfs(n)


        return self.result

    def dfs(self, n : int):
        if n == 0:
            self.result += 1
            return

        elif n < 0:
            return

        else:
            # n >= 1
            # we have 2 choices

            # take one step
            self.dfs(n - 1)

            # take two steps
            self.dfs(n - 2)

