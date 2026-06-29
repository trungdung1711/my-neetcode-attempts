class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # input
        # n piles of bananas
        # the guard will come back in h hours
        # koko can choose her eating speed
        # if k = 5, but the pile has only 4
        # koko will eat all, and stop in that hour

        # output
        # minimun integer k
        # such that in h hours
        # koko can eat all the banana

        # constraints
        # len(piles) >= 1 <= 10^4
        # len(piles) <= h <= 10^9
        # piles[i] >= 1 <= 10^9

        # edge cases

        def hours(k) -> int:
            return sum([math.ceil(banana / k) for banana in piles])

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hour = hours(mid)

            if hour <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left