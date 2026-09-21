class Solution:
    def maxScore(self, s: str) -> int:
        
        # i
        # s 0s and 1s
        # maximum score after spliting the string into
        # w non-empty substrings -- left and right
        # score == num(0s)_left + num(1s)_right

        # o
        # maximum substring
        # num(0s) in the left
        # num(1s) in the right

        # c
        # len(s) >= 2 <= 500
        # s consists only '0' and '1'

        # e
        # len(s) == 2 -> one split
        # split 1 -> n - 1

        res = -float("inf")
        num_0 = 0
        num_1 = 0

        for c in s:
            if c == '0':
                num_0 += 1
            else:
                num_1 += 1

        a = 0

        # 1 -> n - 1
        for i in range(1, len(s)):
            # split -> 0 -> 
            if s[i-1] == '0':
                a += 1
            
            else:
                num_1 -= 1

            if a + num_1 > res:
                res = a + num_1

        return res