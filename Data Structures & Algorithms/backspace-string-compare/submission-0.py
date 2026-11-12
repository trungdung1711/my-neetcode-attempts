class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # i
        # given two strings s and t

        # o
        # return true if they are equal
        # when both are typed into empty editor
        # # means backspace character

        # c
        # len(s) len(t) >= 1 <= 200
        # s and t only contains lowercase letters and # characters

        # e

        stack1 = deque()
        stack2 = deque()

        for c in s:
            if c == "#":
                if stack1:
                    stack1.pop()

            else:
                stack1.append(c)

        for c in t:
            if c == "#":
                if stack2:
                    stack2.pop()
            
            else:
                stack2.append(c)

        return "".join(stack1) == "".join(stack2)