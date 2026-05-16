class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # input
        # cost
        # cost[i] is cost of the i step on the staircase
        # pay the cost -> climb one or two steps
        # can start from step index 0, or start index 1

        # output
        # min cost to reach the top of the floor

        # constraints
        # len(cost) >= 2 <= 1000
        # cost[i] >= 0 <= 999

        # edge case
        # cost == 2 -> start at cost 2 -> cost == 0 ?

        self.cost = float('inf')


        n = len(cost)

        # index : min cost to reach the top
        self.mem = {
            n - 1 : cost[n - 1],
            n - 2 : min(cost[n - 1] + cost[n - 2], cost[n - 2])
        }

        self.dfs(cost, 0)
        self.dfs(cost, 1)

        return min(self.mem[0], self.mem[1])

        
    def dfs(self, cost : List[int], index : int) -> int:

        if index in self.mem:
            return self.mem[index]

        else:
            # there is no index in self.mem
            # we have to find the min cost
            # to reach the top from this
            # index

            left = cost[index] + self.dfs(cost, index + 1)
            right = cost[index] + self.dfs(cost, index + 2)

            min_cost = min(left, right)
            self.mem[index] = min_cost
            return min_cost