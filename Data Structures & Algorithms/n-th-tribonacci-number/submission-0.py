class Solution:
    def tribonacci(self, n: int) -> int:
        
        # input
        # given n

        # output
        # return the tribonacci number of T_n

        # constraints
        # n >=0 <= 37

        # edge cases

        self.mem = {
            0 : 0,
            1 : 1,
            2 : 1,
        }

        def tri(n : int):
            if n in self.mem:
                return self.mem[n]

            else:
                result = tri(n - 1) + tri(n - 2) + tri(n - 3)
                self.mem[n] = result
                return result

        return tri(n)