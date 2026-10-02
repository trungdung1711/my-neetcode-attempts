class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # i
        # given string s

        # o
        # number of palindromic substrings in it
        # s is a palindrome -> reads the same backward as forward
        # substring -> contiguous sequence of characters within the string

        # c
        # len(s) >= 1 <= 1000
        # s consists of lowercase English letters

        # e
        # substring of len(1) can be a palindrome

        mem = set()
        res = 0

        def is_palin(i, j):
            if i >= j:
                if i == j:
                    mem.add((i, j))
                return True

            if (i, j) in mem:
                return True

            else:
                if s[i] == s[j] and is_palin(i + 1, j - 1):
                    mem.add((i, j))
                    return True

        for i in range(len(s)):
            for j in range(len(s), i - 1, - 1):
                if is_palin(i, j):
                    res += 1

        return res
