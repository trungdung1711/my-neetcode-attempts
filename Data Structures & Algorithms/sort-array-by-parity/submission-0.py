class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        # input
        # int array nums
        # move all the even int
        # at the beginning of the array
        # followed by all the odd int

        # output
        # [even, odd]

        # constraints
        # len(nums) >= 1 <= 5000
        # nums[i] >= 0 <= 5000

        # edge cases
        # [1] -> return [1]
        res = deque()

        for num in nums:
            res.append(num) if num % 2 != 0 else res.appendleft(num)

        return list(res)