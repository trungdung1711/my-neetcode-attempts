class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # input
        # arr of distinct integers candidates, target

        # output
        # same number can be chosen from candidates an unlimited number of times
        # unique combinations of candidates -> sum to target

        # constraint
        # len(candidates) >= 1 <= 30
        # candidates[i] >= 2 <= 40
        # all elements are distinct
        # target >= 1 <= 40

        # edge case

        index = 0
        self.sol = []

        candidate = []

        self.backtrack(candidate, 0, target, candidates)

        return self.sol

    def backtrack(self, candidate, index, target, candidates):
        if sum(candidate) == target:
            self.sol.append(candidate)
        
        if sum(candidate) > target:
            # backtracking
            return
        
        # sum < target
        # index < len(candidates) -> still have candidates

        # path = candidate solution

        while index < len(candidates):
            # only return when sum > target
            self.backtrack(candidate + [candidates[index]], index, target, candidates)
            index += 1

        # return, full choices
