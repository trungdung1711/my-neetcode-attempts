class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack : list = []

        for s in operations:
            if s == "+":
                stack += [stack[-1] + stack[-2]]

            elif s == "D":
                stack += [stack[-1] * 2]

            elif s == "C":
                stack.pop()
            
            else:
                stack += [int(s)]

        return sum(stack) 