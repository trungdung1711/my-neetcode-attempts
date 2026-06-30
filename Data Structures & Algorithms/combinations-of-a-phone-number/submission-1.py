class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # input
        # a string made by {2-9} digits
        # a mapping of digits to letters

        # output
        # all possible letter
        # that the number could represent

        # constraints
        # len(digits) >= 1 <= 4
        # digits[i] is digit in range [2, 9]

        # edge cases

        if len(digits) == 0:
            return []

        digit_letter_map = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        res = []

        def gen(cur, letters):
            nonlocal res
            if cur == len(digits):
                res += [letters]
                return

            # not end
            digit = digits[cur]

            choices = digit_letter_map[int(digit)]

            for choice in choices:
                # 
                gen(cur + 1, letters + choice)

        gen(0, "")

        return res