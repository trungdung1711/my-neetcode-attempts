class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        # i
        # distinct string
        # arr
        # k
        # k_th distinct string present
        # in arr

        # o
        # return the k_th distinct string
        # present in arr
        # fewer than k distinct strings
        # return ""

        # c
        # len(arr) >= k >= 1 <= 1000
        # len(arr[i]) >= 1 <= 5
        # arr[i] lowercase English letters

        # e
        
        # first we need to remove the dupplicates
        # and return the k_th

        c = Counter(arr)

        i = 0

        for s in arr:
            if c[s] == 1:
                i += 1

            if i == k:
                return s
        
        if i < k:
            return ""