class Solution:
    def dfs(self, index, nums, subset):
        if index == len(nums):
            # commit
            self.result.append(subset)
            return
        
        # decision
        # left
        self.dfs(index + 1, nums, subset)
        self.dfs(index + 1, nums, subset + [nums[index]])


    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # input 
        # array of unique elements
        # all possible subsets (The power set)

        # output
        # list of all possible subsets

        # constraints
        # len(nums) >= 1 <= 10
        # all the numbers are unique

        # edge cases
        # [] -> []
        # [1] -> [[], [1]]

        self.result = []
        self.dfs(0, nums, [])

        return self.result
