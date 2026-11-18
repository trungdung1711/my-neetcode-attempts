class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        # i
        # two strings s and t
        # lowercase English letters
        # minimum number of characters
        # appended to the end s -> t becomes a subsequence of s
        # subsequence = derived from another string
        # deleting some or no characters without changing the order of the remaining character

        # o
        # min number of added characters -> t subseq of s

        # c
        # len(s), len(t) >= 1 <= 10^5
        # s, t consists only lowercase English letters

        # e
        # "" "dffgdk" -> len(t)

        p1 = 0
        p2 = 0

        while p2 < len(t) and p1 < len(s):
            if t[p2] == s[p1]:
                # max
                p1 += 1
                p2 += 1

            else:
                # diff
                p1 += 1

        if p2 >= len(t):
            return 0

        return len(t) - p2