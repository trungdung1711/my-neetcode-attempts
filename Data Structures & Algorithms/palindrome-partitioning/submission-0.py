class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # i
        # a string s
        # You will need to partition s
        # such that every substring of the partition is a palindrome

        # o
        # return all possible palindrome partitioning of s

        # c
        # len(s) >= 1 <= 16
        # s contains only lowercase English letters

        # e
        # len(s) == 1 -> one partition

        if len(s) == 1:
            return [[s]]

        def is_palindrome(ss):
            if len(ss) <= 0:
                return False

            elif len(ss) == 1:
                return True

            else:
                # len(ss) >= 2
                left = 0
                right = len(ss) - 1

                while left <= right:
                    if ss[left] == ss[right]:
                        left += 1
                        right -= 1

                    else:
                        return False

                return True

        res = []

        def backtracking(ss, p):
            nonlocal res

            # a string will have a choice for partition
            # from index 1 -> n - 1

            for i in range(1, len(ss)):


                a = ss[0:i] # exclusively (a, ___ -> ___, a)
                b = ss[i:] # ___ and a

                is_a = is_palindrome(a)
                is_b = is_palindrome(b)

                if is_a and is_b:
                    # that would make a full partition
                    # must add two new partitions a and b
                    res.append(p + [a, b])

                    # although we have the solution
                    # but can we further partition on b
                    # important
                    backtracking(b, p + [a])

                elif is_a and not is_b:
                    # only a, further partition on b is needed
                    backtracking(b, p + [a])
                    # fail

        backtracking(s, [])

        if is_palindrome(s):
            res.append([s])

        return res