class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # input
        # nums = array of distinct integers

        # output
        # all possible permutations

        # constraints
        # len(nums) >= 1 <= 6
        # nums[i] >= -10 <= 10
        # all the integers are unique

        # edge cases
        # [1] -> [[1]]
        # [1, 2] -> [[1, 2], [2, 1]]
        self.result = []
        empty_set = set()

        self.dfs(nums, empty_set, [])

        return self.result


    def dfs(self, nums : List[int], int_in : set[int], res : List[int]):
        if len(res) == len(nums):
            # a new permutation
            self.result += [res]
            return

        # not enough integers
        for num in nums:
            if num in int_in:
                continue
            
            else:
                int_in.add(num)
                self.dfs(nums, int_in, res + [num])
                int_in.remove(num)
