class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # input
        # an array arr
        # replace every element
        # with the greatest element
        # among the elements to its right
        # last element with -1

        # output

        # constraints

        # edge cases

        start = len(arr) - 1

        max = float("-inf")

        while start >= 0:
            if start == len(arr) - 1:
                max = arr[start]
                arr[start] = -1
                

            else:
                cur = arr[start]

                arr[start] = max

                if cur > max:
                    max = cur
                    

            start -= 1

        return arr