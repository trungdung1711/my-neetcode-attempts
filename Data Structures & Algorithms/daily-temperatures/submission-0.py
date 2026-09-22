class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        # i
        # array of ints
        # temperatures -> daily tem
        # 

        # o
        # answer such that
        # answer[i] is the number of days
        # to wait after the ith day to get
        # a warmer temperature
        # if there is no future day which is warmer
        # keep answer[i] == 0

        # idea
        # 1. i check i + 1 -- n - 1
        # if there exists a tem > tem[j] -> j - i
        # 2. use the stack
        # put the tem and the index
        # 1. tem increase -> delete the prev -> add the current
        # 2. tem decrease (<=) -> push to stack

        # c
        # len(temperatures) >= 1 <= 10^5
        # temperatures[i] >= 0 <= 100

        # e
        # len(temperatures) == 1 -> return [0]

        stack = deque()
        res = [0 for i in range(len(temperatures))]

        for index, tem in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((index, tem))

            elif len(stack) >= 1:

                # increase

                while len(stack) >= 1:
                    # found
                    prev_index, prev = stack[-1]
                    if tem > prev:
                        res[prev_index] = index - prev_index
                        # pop the prev
                        stack.pop()

                    else:
                        # tem <= prev
                        break


                stack.append((index, tem))

        return res