class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        # i
        # array of ints stones
        # stones[i] weight of ith stone
        # turn
        # choose the heaviest two stones -> smash
        # x and y x <= y
        # x == y -> destroyed
        # x != y -> y new weight y - x
        # at the end of the game, at most one stone left

        # o
        # return weight of the last remaining stone
        # there are no stones left -> return 0

        # c
        # len(stones) >= 1 <= 30
        # stones[i] >= 1 <= 1000 -> >= 0 -1

        # e

        import heapq
        
        s = [-v for v in stones]


        heapq.heapify(s)

        while len(s) >= 2:

            x = - heapq.heappop(s)
            y = - heapq.heappop(s)

            if x != y:
                heapq.heappush(s, - abs(x - y))

            # x == y

        if len(s) == 0:
            return 0

        return -s[0]