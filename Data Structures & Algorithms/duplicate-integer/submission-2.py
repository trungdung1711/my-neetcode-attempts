class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup : set = set()

        for num in nums:
            if num in dup:
                return True
            
            dup.add(num)
        
        return False
        
        # input: array of numbers
        # output: true if any value appears at least twice
        # false if distinct

        # constraint
        # len(nums) >= 1

        # edge case
        # [3] -> true

        # sol2
        


        # sol1