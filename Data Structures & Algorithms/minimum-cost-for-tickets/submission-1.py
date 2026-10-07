class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        
        # i
        # train traveling one year in advance
        # days of year when you will travel -> days
        # days[i] >= 1 <= 365
        # train tickets are sold in 3 different ways
        # 1-day pass -> costs[0]
        # 7-day pass -> costs[1]
        # 30-day pass -> costs[2]
        # passes -> many days of consecutive travel
        # day-2 buy 7-day pass -> [2, 3, 4, 5, 6, 7, 8

        # o
        # minimum number of dollars you need to travel
        # every day in the given lists of days

        # c
        # len(days) >= 1 <= 365
        # days[i] >= 1 <= 365
        # days strictly increasing order
        # len(costs) == 3
        # costs[i] >= 1 <= 1000

        # e
        # len(days) == 1 -> buy one day pass -> base case
        # len(days) == 365 -> continuously buy 30-day pass

        # index
        mem = {

        }

        p = [1, 7, 30]

        pass_cost = list(zip(p, costs))

        def min_cost(index):
            nonlocal mem

            # if we have already calculated the min cost
            # to travel from this day
            if index in mem:
                return mem[index]

            if index >= len(days):
                return 0


            if index == len(days) - 1:
                # the last day, then choose the cheapest pass
                # return costs[0]
                return min(costs)

            # calculate the min cost to travel from that day
            # we have 3 options


            can = []
            current_day = days[index]

            for p, cost in pass_cost:
                cover_days = current_day + p - 1

                # find the next day we need to buy a new pass
                i = index

                while i < len(days) and days[i] <= cover_days:
                    i += 1

                # break condition
                if i >= len(days):
                    # the current pass cover all
                    can.append(cost)

                elif days[i] > cover_days:
                    # we need to buy new pass
                    can.append(cost + min_cost(i))


            mem[index] = min(can)
            return mem[index]

        return min_cost(0)
