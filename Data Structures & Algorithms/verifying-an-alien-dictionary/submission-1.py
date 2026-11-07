class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        
        # i
        # alien language
        # English lowercase letters
        # different order
        # order of alphabet is some permutation of lowercase letters
        # sequence of words, order of the alphabet

        # o
        # true words are sorted lexicographically in this alien language
        # otherwise false

        # c
        # len(words) >= 1 <= 100
        # len(words[i]) >= 1 <= 20
        # order.length == 26
        # all characters in words[i] and order are in lowercase letters

        # e
        # apples > app

        map = {
            c: score for score, c in enumerate(order, 1)
        }

        def compare(a : str, b : str):
            for i in range(min(len(a), len(b))):
                if map[a[i]] < map[b[i]]:
                    return True

                elif map[a[i]] > map[b[i]]:
                    return False

                else:
                    # equal
                    None
            
            # == until now
            return True if len(a) <= len(b) else False

        for i in range(len(words) - 1):
            if not compare(words[i], words[i + 1]):
                return False

        return True