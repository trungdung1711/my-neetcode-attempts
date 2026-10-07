class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        # i
        # given a string and a dictionary
        # wordDict
        # the same word in the dictionary may be re-used multiple times
        # in the segmentation

        # o
        # true if s can be segmented into a space-separated sequence
        # of one of more dictionary words

        # c
        # len(s) >= 1 <= 300
        # len(wordDict) >= 1 <= 1000
        # len(wordDict[i]) >= 2 <= 20
        # a and wordDict[i] consist of only lowercase English letters
        # all the strings of wordDict are unique

        # e

        mem = {

        }

        def searching(index):
            nonlocal mem

            if index in mem:
                return mem[index]

            if index >= len(s):
                return True

            # for every parts
            can = []
            for part in wordDict:
                len_part = len(part)

                chunk = s[index:index + len_part]

                if chunk == part:
                    # then we can chunk
                    # continue
                    can.append(searching(index + len_part))

            mem[index] = any(can)

            return mem[index]

        return searching(0)