from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # input
        # 2 strs s1, s2

        # output
        # true if s2 contains a permutation of s1
        # or false otherwise
        # s1's permutations is the substring of s2

        # constraints
        # len(s1, s2) >= 1 <= 10^4
        # s1, s2 lowercase English letters

        # edge cases
        # 'a' -> contain that

        if len(s2) < len(s1):
            return False

        # len(s2) >= len(s1)

        s1_dict = dict(Counter(s1))

        s2_dict = {

        }

        left = 0
        right = -1

        for index, c in enumerate(s2):
            right += 1

            len_sub = right - left + 1

            if len_sub < len(s1):
                # move right
                if c in s2_dict:
                    s2_dict[c] += 1

                else:
                    s2_dict[c] = 1

            elif len_sub == len(s1):
                # slide right

                if c in s2_dict:
                    s2_dict[c] += 1

                else:
                    s2_dict[c] = 1

                if s2_dict == s1_dict:
                    return True

                else:
                    # slide window
                    s2_dict[s2[left]] -= 1

                    if s2_dict[s2[left]] == 0:
                        s2_dict.pop(s2[left])

                    left += 1

                    # if c in s2_dict:
                    #     s2_dict[c] += 1

                    # else:
                    #     s2_dict[c] = 1

                    # right += 1

        return False