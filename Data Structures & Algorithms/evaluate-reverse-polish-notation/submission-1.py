class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        # i
        # an array of strings tokens
        # represents an arithmetic expression in RPN

        # o
        # evaluate that expression and return an int of value of that expression

        # c
        # ops are + - * /
        # operand can be int or another exp
        # no division by 0
        # RPN
        # ans and intemediate result can be represented 32 bit int
        # len(tokens) >= 1 <= 10^4
        # tokens[i] can be op and int >= -200 <= 200

        # e
        # all operators are binary operators -> one op must come with 2 operands
        #

        # idea
        # well, because it works natively with the DS stack
        # then use it to calculate the expression

        stack = deque()

        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()

                stack.append(a + b)

            elif token == "-":
                a = stack.pop()
                b = stack.pop()

                stack.append(b - a)

            elif token == "*":
                a = stack.pop()
                b = stack.pop()

                stack.append(a * b)

            elif token == "/":
                a = stack.pop()
                b = stack.pop()

                stack.append(int(b / a))

            else:
                stack.append(int(token))

        return stack.pop()