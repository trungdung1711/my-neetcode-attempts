class Solution:
    def clearDigits(self, s: str) -> str:
        
        # i
        # a string s
        # remove all digits
        # delete the first digit
        # and the closest non-digit character to its left
        # operation can't be performed on a digit
        # that doesn't have any non-digit character to its left [X] -> violation

        # o
        # string that has been removed all digits

        # c
        # len(s) >= 1 <= 100
        # s only lowercase English letters and digits
        # it is possible to delete all digits

        # e
        # only digits "123"
        # no non-digit character to the left "1f"
        # input is generated so that we can delete all digits
        # -> delete -> non-character to the left

        stack = deque()

        for c in s:
            if c.isdigit():
                stack.pop()

            else:
                stack.append(c)

        return "".join(list(stack))