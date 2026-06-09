class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # input
        # s and t

        # output
        # true if s is subsequence of t
        # else false

        # constraints
        # len(s) >= 0 <= 100
        # len(t) >= 0 <= 10^4
        # lowercase English letters

        # edge cases
        # if s = "", t = "" -> true
        # if s = "", t != "" -> true
        # if s = "s", t = ""

        # sol 1
        # if s == "":
        #     return True

        # if s == t:
        #     return True

        # if len(s) > len(t):
        #     return False

        # index = 0
        # j = 0

        # while index < len(s):
        #     # s is not exhausted

        #     # search for that in t
        #     while j < len(t):
        #         if s[index] == t[j]:
        #             j += 1
        #             break

        #         j += 1

        #     if j >= len(t) and index < len(s):
        #         return False

        #     index += 1


        # # after
        # # index == len(s)
        # if index >= len(s):
        #     return True

        # if index < len(s):
        #     return False

        # return True

        index = 0
        j = 0
        while index < len(s):
            found = False

            while j < len(t):
                if s[index] == t[j]:
                    found = True
                    j += 1
                    break
                j += 1

            if not found:
                return False

            index += 1

        return True