class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # i
        # a parentheses string is valid if and only if
        # empty str
        # AB -> valid
        # (A) where A is a valid string
        # one move -> insert a parenthesis at any
        # position of the string
        # minimum number of moves -> s valid

        # o
        # len(s) >= 1 <= 1000
        # s[i] is either "(" or ")"

        # c
        # len(s) >= 1 <= 1000
        # s[i] is either "(" or ")"

        # e
        # empty -> 0
        # "1" -> 1

        if len(s) <= 1:
            return len(s)

        stack = deque()
        # stack.append(s[i])

        for i in range(0, len(s)):

            if stack:

                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()

                else:
                    stack.append(s[i])


            else:
                stack.append(s[i])

        return len(stack)