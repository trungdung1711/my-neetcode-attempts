class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # input: nums and k
        # output: nums[i] == nums[j] and abs(i, j) <= k -> true
        # else false

        # constraint
        # len(nums) >= 1
        # k <= n -> 

        # edge case
        # [1] -> false
        # k can't be 0

        # sol3: true sliding window
        # in the previous solution
        # when moving the window
        # I just recheck for every element in the windows
        # that is not effective for that
        # instead we can maintain a set of element in the current
        # window, when moving the window (to check for the next element)
        # remove the left-side and add the right-side

        n = len(nums)
        window: set = set()

        # if k == 0:
        #     return False
        for index, num in enumerate(nums):
            if num in window:
                return True
            
            else:
                # size of window is at most k
                # maintain the window at most k
                # less than k is ok
                window.add(num)
                if len(window) > k:
                    window.remove(nums[index - k])
        
        return False



        


        # sol2: wrong sliding window
        # if k == 0:
        #     return False
        
        # n = len(nums)

        # # max is n - 1
        # # k is the maximum, k is the biggest window
        # # it doesn't mean the pair must stay away of size k
        # # if k > n - 1:
        # #     return False

        # for i in range(0, n):
        #     # window of size k
        #     # search for duplicated values in that
        #     for j in range(1, k + 1):
        #         # in the window of size k
        #         # but can be out of bound
        #         if i - j < 0:
        #             continue
                
        #         if nums[i] == nums[i - j]:
        #             return True

        # return False


        # sol1: brute-force approach

        # time complexity:
        # k = 1 -> N
        # k = 2 -> N - 1
        # k = N -> 0
        # -> O(N^2)

        # if k == 0:
        #     return False

        # n = len(nums)
        
        # for i in range (1, k + 1):
        #     # loop of possible k values
        #     for j in range (0, n - i):
        #         if nums[j] == nums[j + i]:
        #             return True
        
        # return False