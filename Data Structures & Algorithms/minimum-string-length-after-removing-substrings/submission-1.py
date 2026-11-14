class Solution:
    def minLength(self, s: str) -> int:
        
        # i
        # string s uppercase English letters
        # some operations
        # one operation
        # remove any occurence
        # "AB" or "CD" from s

        # o
        # minimum possible length of
        # the resulting string that you can obtain
        # remove "AB" or "CD" -> concatenate -> produce new string

        # c
        # len(s) >= 1 <= 100
        # s consists only of uppercase English letters

        # e
        # there is no "AB" or "CD"

        stack = deque()

        for c in s:
            if stack:
                if c == "B" and stack[-1] == "A":
                    stack.pop()

                elif c == "D" and stack[-1] == "C":
                    stack.pop()

                else:
                    stack.append(c)

            else:
                stack.append(c)

        return len(stack)