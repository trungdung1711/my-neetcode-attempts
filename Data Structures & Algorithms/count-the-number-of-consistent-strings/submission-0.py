class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        # i
        # allowed
        # distinct characters
        # words
        # a string is consistent
        # if all characters in a string appear
        # in allowed

        # o
        # number of consistent string in words

        # c
        # len(words) >= 1 <= 10^4
        # len(allowed) >= 1 <= 26
        # len(words[i]) >= 1 <= 10
        # c in allowed distinct
        # words[i] and allowed contain lowercase letter

        # e

        a = set(allowed)
        res = 0

        for w in words:
            b = set(w)

            if b.issubset(a):
                res += 1

        return res