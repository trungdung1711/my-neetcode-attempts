class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # input: array of heights length n
        # output: two lines that create the container containing the most water
        # maximum water
        # (a, b) -> min(a, b) * distance

        #constraints:
        # n >= 2
        # height >= 0 <= 10^4

        # edge case
        # [0 , 1] -> 0
        # [1, 2] -> 1
        # [5, 10, 12] -> 100

        # sol1: brute force
        # checking for every lines

        # sol2:
        # min(a, b) -> max, dis -> max
        # 2 things: height and dis

        left : int = 0
        right : int = len(height) - 1
        max : int = -1

        while left < right:
            candidate : int = (right - left) * min (height[left], height[right])
            if candidate > max:
                max = candidate
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max