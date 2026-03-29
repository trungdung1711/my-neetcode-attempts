class Solution:
    def isValid(self, s: str) -> bool:
        
        # input: string s () {} []
        # output: s is valid

        # constraint
        # len(s) .>= 1
        # s contains only () {} []

        # edge case
        # len(s) == 1 -> false
        # (
        # ((()) -> opens > closes
        # ())) -> closes > opens

        stack : list = []

        for c in s:
            if c == "(" or c == "{" or c == "[": 
                stack += [c]
            elif c == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        
        # handle the case: closes > opens
        if len(stack) != 0:
            return False

        return True