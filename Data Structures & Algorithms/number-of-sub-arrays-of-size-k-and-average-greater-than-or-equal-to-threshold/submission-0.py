class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # i
        # an array arr and integers k and threshold

        # o
        # number of sub-arrays of size k with
        # average >= threshold

        # c
        # len(arr) >= 1 <= 10^5
        # arr[i] >= 1 <= 10^4
        # k >= 1 <= len(arr) -> max k = len(arr)
        # threshold >= 0 <= 10^4

        # e
        # k == 1 -> arr[i]
        # k = len(arr) -> the whole arr

        # create the first subarray
        # keeping sum
        s = 0
        res = 0

        for i in range(k):
            s += arr[i]

        if s / k >= threshold:
            res += 1

        # loop
        # check con
        # create new sub
        # check value
        for i in range(k, len(arr)):
            # k and len(arr) - 1

            # form array
            s = s + arr[i] - arr[i - k]
            if s / k >= threshold:
                res += 1

            # continue with k

        return res