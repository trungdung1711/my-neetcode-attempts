class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        # i
        # an array of string
        # words
        # all strings in words that are substring of another word

        # o
        # strings in words, that are substring of another
        # word

        # c
        # len(words) >= 1 <= 100
        # len(words[i]) >= 1 <= 30
        # words[i] only lowercase English
        # all strings in words are unique

        # e
        # len(words) == 1
        res = set()

        if len(words) == 1:
            return list(res)


        for word in words:
            for w in words:
                if word != w and len(w) < len(word):
                    if w in word:
                        res.add(w)

        return list(res)
