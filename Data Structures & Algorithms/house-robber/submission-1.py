class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # input
        # nums: amount of money of each house

        # output
        # maximum amount of money of each house
        # without alerting the police

        # constraints
        # if two houses are broken on the same night
        # alert -> call the police
        # len(nums) >= 1 <= 100
        
        # edge cases
        # len(nums) == 1 -> rob
        # len(nums) == 2 -> rob either
        # len(nums) == 3 -> rob 1-3 or rob 2

        # index : maximum amount of money that we can rob
        n = len(nums)
        self.mem = {
            n - 1 : nums[n - 1]
        }

        def max_money(nums : List[int], index : int):
            if index in self.mem:
                return self.mem[index]

            else:
                next_index = index + 2
                possibles = [0]

                while next_index < n:
                    possibles += [max_money(nums, next_index)]
                    next_index += 1

                max_amount = nums[index] + max(possibles)
                self.mem[index] = max_amount
                return max_amount

        max_amount = max([max_money(nums, i) for i in range(n)])

        return max_amount