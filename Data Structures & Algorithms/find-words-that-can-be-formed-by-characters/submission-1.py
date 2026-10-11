from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        
        # i
        # an array of strings words
        # a string chars
        # a string is good
        # can be formed from chars
        # (each character can be used once for each words in word)

        # o
        # sum of lengths of all good strings in words
        
        # w
        # if we use a character
        # but it can't make a string
        # -> return that character for other
        # candidates

        # c
        # len(words) >= 1 <= 1000
        # len(words[i]) >= 1, len(chars) <= 100
        # words[i] and chars lower case

        # e

        res = 0

        freq = Counter(chars)

        for word in words:

            word_freq = Counter(word)
            can_be_formed = all(
                [True if word_freq[c] <= freq[c] else False for c in word]
            )

            if can_be_formed:
                # freq = freq - word_freq
                res += len(word)

            else:
                continue

        return res