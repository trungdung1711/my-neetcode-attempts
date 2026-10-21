class Solution:
    def romanToInt(self, s: str) -> int:

        # i
        # roman numberal

        # o
        # integer

        # c
        # len(s) >= 15 <= 1
        # s[i] = {"I", "V", "X", "L", "C", "D", "M"}

        # e
        
        m = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV": 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
        }

        def eat(value):
            # check 2 values

            if len(value) == 1:
                return m[value]

            if len(value) == 0:
                return 0

            else:

                if value[0:2] in m:
                    return m[value[0:2]] + eat(value[2:])

                else:
                    return m[value[0:1]] + eat(value[1:])

        return eat(s)