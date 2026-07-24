class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # input
        # you are a parent
        # you want to give your children some cookies
        # each child at most one
        # each child has a greed factor == min size to satisfy
        # each cookie has a size
        # s[j] >= g[i] -> assign cookie j to child i -> satisfy

        # output
        # we need to maximize the number of content children

        # constraints
        # len(g) >= 1 <= 3*10^4
        # len(s) >= 0 <= 3*10^4
        # g[i], s[i] >= 1 <= 2^31 - 1

        # edge cases
        # len(s) == 0 -> return 0

        # to maximize the number of content children
        # we need to assign the cookie with s[i] to be the same as the g[i]
        # but if we can't, s[i] > g[i], but s[i] - g[i], should be smallest

        g = sorted(g)
        s = sorted(s)

        a = 0
        b = 0
        res = 0

        while a < len(g) and b < len(s):
            if s[b] >= g[a]:
                # assign that cookie to that child
                res += 1
                a += 1
                b += 1
            elif s[b] < g[a]:
                # that child doesn't satisfy with
                # the current cookie
                b += 1
                # throw that cookie
                # because we can't use it

        # we don't have any child
        # or we are out of cookies
        return res