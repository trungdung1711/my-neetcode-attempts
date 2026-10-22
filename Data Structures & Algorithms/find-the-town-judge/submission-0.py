class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        # i
        # in a town, n people
        # 1 -> n
        # one of these people
        # secretly the town judge
        # 1. the town judge trusts nobody
        # 2. everybody (except the town judge) trusts
        # the town judge
        # one person that satisfies [1] and [2]
        # trust[i] = [a, b] -> a trusts b
        # if a trust doesn't exist in the trust array, then
        # such a relationship does not exist

        # o
        # label of the town judge if he exists
        # otherwise -1

        # c
        # n >= 1 <= 1000
        # len(trust) >= 0 <= 10^4
        # len(trust[i]) == 2
        # all the pairs are unique

        # e
        # len(trust) == 0
        # len(trust) == 1

        i_trust = [0] * (n + 1)
        be_trusted = [0] * (n + 1)

        for t in trust:
            a, b = t

            i_trust[a] += 1
            be_trusted[b] += 1

        for i in range(1, n + 1):
            if i_trust[i] == 0 and be_trusted[i] == n - 1:
                return i

        return -1