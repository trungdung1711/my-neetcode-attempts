class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        # input
        # a list of file system operations

        # output

        # constraints

        # edge cases
        s = deque()

        for o in logs:
            if o == "../" and len(s) > 0:
                s.pop()

            elif o == "../" and len(s) == 0:
                continue

            elif o == "./":
                continue

            else:
                # go to the directory
                s.append(o)

        res = 0

        while True:
            if len(s) == 0:
                return res

            # else
            s.pop()
            res += 1