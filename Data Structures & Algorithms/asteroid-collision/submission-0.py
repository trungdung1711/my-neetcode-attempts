class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        
        # i
        # asteroids -> represent asteroids in a row
        # the indices -> relative position in space
        # |a| -> its size
        # sign represents its direction
        # each asteroid moves at the same speed

        # o
        # state after collision
        # two meet -> the smaller one will explode
        # both are the same size -> both will explode
        # two asteroids -> moving in the same direction
        # will never meet

        # ex
        # 3 5 -6 2 -1 4
        # 0 1  2 3  4 5
        # everything is in a line
        # + -> right
        # - -> left
        # 5 -6 -> -6
        # 2 -1 ->  2
        # 3 -6 2 4
        # 3 -6 -> -6
        # -6 2 4

        # c
        # len(asteroids) >= 2 <= 10^4
        # asteroids[i] >= -1000 <= 1000
        # asteroids[i] != 0

        # e
        # [4, 5] -> OK
        # [-4, -6] -> OK

        # idea
        # use a stack to continuously
        # add the asteroids
        # if there exist two asteroid
        # which could possibly collide
        # let them colide and create
        # the new asteroid

        stack = deque()
        stack.append(asteroids[0])

        for i in range(1, len(asteroids)):

            stack.append(asteroids[i])

            if len(stack) == 1:
                continue

            nearest = stack[-2]
            current = stack[-1]

            while nearest > 0 and current < 0:
                # ---> <---

                A = abs(nearest)
                B = abs(current)

                stack.pop()
                stack.pop()
                if A == B:
                    break

                elif A > B:
                    stack.append(nearest)
                    if len(stack) == 1:
                        # can't find nearest
                        break
                    
                    # >= 1
                    current = stack[-1]
                    nearest = stack[-2]

                else:
                    # A < B
                    stack.append(current)
                    if len(stack) == 1:
                        break

                    # >= 1
                    current = stack[-1]
                    nearest = stack[-2]

        return list(stack)