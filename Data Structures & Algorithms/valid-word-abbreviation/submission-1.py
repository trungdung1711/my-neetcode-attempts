class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        # input
        # a string can be shortened
        # non-empty substrings with their lengths
        # no leading 0s
        # no substrings replaced
        # adjacent substrings are replaced
        # given a string named word
        # an abbreviation abbr

        # output
        # true if abbr is an abbreviation of word
        # otherview false
        # while there is the condition
        # of non-adjacent
        # if adjacent -> ab -> we don't
        # know the number
        # not adjacent -> we can extract the number correctly

        # constraints
        # len(word) >= 1 <= 100
        # word contains only lowercase English letter
        # len(abbr) >= 1 <= 100
        # abbr == lowercase English letters + digits
        # all digit fit in a 32-bit integer

        # edge cases
        # abbr is the same thing as word
        # abbr contains only number

        # if character -> advance both
        # number -> extract the number and advance that number

        a = 0 # word
        b = 0 # abbr

        while a < len(word) and b < len(abbr):

            if abbr[b].isdigit():
                # handle
                # extract that digit
                # advance b
                num = ""
                while abbr[b].isdigit():
                    num += abbr[b]
                    b += 1

                # is not digit
                num = int(num)

                # advance word
                for i in range(num):
                    a += 1


            else:
                # character
                if word[a] != abbr[b]:
                    return False

                else:
                    # == -> advance
                    a += 1
                    b += 1

        return True if (a == len(word) and b == len(abbr)) else False