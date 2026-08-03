class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        # i
        # a string text
        # use characters of text
        # to form as many instances
        # of the word balloon
        # use each character at most once
        # return maximum number of instances

        # o
        # maximum number of balloons
        # thar can be formed

        # c
        # len(text) >= 1 <= 10^4
        # only lower case

        # e
        # no balloon

        # [b a l l o o n]
        l = 2
        o = 4

        balloon = [0, 0, 0, 0, 0, 0, 0]

        for c in text:
            if c == "b":
                balloon[0] += 1
            
            elif c == "a":
                balloon[1] += 1

            elif c == "n":
                balloon[6] += 1

            elif c == "l":
                balloon[l] += 1
                l = 3 if l == 2 else 2

            elif c == "o":
                balloon[o] += 1
                o = 5 if o == 4 else 4

        return min(balloon)
