class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # input
        # an interger array in non-decreasing order
        # array of the squares of each number
        # sorted in non-decreasing order

        # output
        # array of squares sorted
        # in non-decreasing order

        # constraints
        # len(nums) >= 1 <= 10^4
        # nums[i] >= -10^4 <= 10^4
        # nums is sorted in non-decreasing order

        # edge cases

        left = 0
        right = len(nums) - 1
        res = deque()

        while left <= right:
            # we have to choose between left and right

            ll = nums[left] ** 2
            rr = nums[right] ** 2

            if ll >= rr:
                res.appendleft(ll)
                left += 1

            else:
                # rr > ll
                res.appendleft(rr)
                right -= 1

        # left > right
        # we can't pick one from the twos

        return list(res)