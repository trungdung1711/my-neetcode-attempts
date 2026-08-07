class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        # i
        # an array of integers arr
        # lucky int == int that has a frequency == its value

        # o
        # return largest lucky int, no lucky int -> return -1

        # c
        # len(arr) >= 1　<= 500
        # arr[i] >= 1 <= 500

        # e
        # [1] -> return 1
        # [4] -> return -1

        f = [0 for i in range(0, 501)]
        # 0 -> 500
        # 0 is dropped

        for num in arr:
            f[num] += 1

        for i in range(500, 0, -1):
            if i == f[i]:
                return i

        return -1

