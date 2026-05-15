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

        self.mem = {
            1 : 1,
            2 : 2,
        }

        self.dfs(n)


        return self.mem[n]

    def dfs(self, n : int):
        if n in self.mem:
            self.result += self.mem[n]
            return self.mem[n]

        else:
            # there is no n
            left = self.dfs(n - 1)
            right = self.dfs(n - 2)

            self.mem[n] = left + right
            return self.mem[n]
