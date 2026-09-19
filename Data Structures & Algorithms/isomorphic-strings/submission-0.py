class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # i
        # s and t strings
        # determine if they are isomorphic
        # characters in s can be replaced to get t
        # no two character may map to the same character
        # "a" -> "m", then "b" can not be mapped to "m"

        # o
        # True if they are isomorphic
        # False otherwise

        # c
        # len(s) >= 1 <= 5 * 10^4
        # len(s) == len(t)
        # s and t consist of any valid ascii characters

        # e
        # we only solve one case
        # 1. a -> m, but then we found b -> m
        # 2. a -> m, but then a -> n

        mapping = {

        }

        for index, c in enumerate(s):
            if c in mapping:
                mapped = mapping[c]

                if t[index] != mapped:
                    # we must map another
                    # a -> b
                    # c -> a -> c to make
                    return False
                
                # equal of
            else:
                # create mappings
                if t[index] in mapping.values():
                    return False
                mapping[c] = t[index]

        return True