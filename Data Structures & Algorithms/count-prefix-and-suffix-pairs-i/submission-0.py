class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        # i
        # string away words
        # isPrefixAndSuffix(s1, s2)
        # true -> str1 is both prefix and suffix of str2
        # false -> othervise

        # of number of index pairs (i, j)
        # i < j and isPrefixAndSuffix(words[i], words[j]) is true

        # c
        # len(words) >= 1 <= 50
        # len(words[i]) >= 1 <= 10
        # words[i] consists of only of lowercase English letters

        # e
        # len(words) == 1 -> return 0

        if len(words) == 1:
            return 0

        def isPrefixAndSuffix(s1, s2):
            if len(s1) > len(s2):
                return False

            # <=
            len_s1 = len(s1)

            return True if s1 == s2[:len_s1] and s1 == s2[-len_s1:] else False

        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1

        return res