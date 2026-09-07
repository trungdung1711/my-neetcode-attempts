class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        # i
        # an array of string words
        # a string pref

        # o
        # number of strings in words
        # contain pref as a prefix

        # c
        # len(words) >= 1 <= 100
        # len(words[i]), len(pref) >= 1 <= 100
        # words[i] and pref contains only lowercase English letters

        # e
        # pref == words[i]

        def is_pref(pref, s):
            
            if len(pref) > len(s):
                return False

            else:
                # len(pref) <= len(s)
                for i in range(len(pref)):
                    if not (pref[i] == s[i]):
                        return False
                return True

        res = 0
        for w in words:
            if is_pref(pref, w):
                res += 1

        return res