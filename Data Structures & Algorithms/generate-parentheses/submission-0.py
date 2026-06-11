class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # input
        # n pairs of parenthesis

        # output
        # all combinations of
        # a well=formed parentheses

        # constraints
        # n >= 1 <= 8

        # edge case

        res = []

        def backtracking(o, c, result):
            nonlocal res

            # choices
            if o > 0 and c == 0:
                # one choices
                backtracking(o - 1, c, result + "(")

            elif c > 0 and o == 0:
                backtracking(o, c - 1, result + ")" )

            elif c > 0 and o > 0:
                # 2 choices
                backtracking(o - 1, c, result + "(")
                backtracking(o, c - 1, result + ")")


            elif c == 0 and o == 0:
                # result
                if self.check_well_formed(result) is True:
                    res += [result]


        backtracking(n, n, "")

        return res


    
    def check_well_formed(self, s) -> bool:
        stack = []

        # one well-formed string
        for c in s:
            if c == "(":
                stack.append(c)

            elif c == ")":
                if len(stack) == 0:
                    return False

                if stack[-1] == "(":
                    stack.pop(-1)

                elif stack[-1] == ")":
                    return False

        if len(stack) > 0:
            return False

        elif len(stack) == 0:
            return True