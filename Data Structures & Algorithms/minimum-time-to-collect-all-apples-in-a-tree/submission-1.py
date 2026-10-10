class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        
        # i
        # undirected tree n vertices
        # numbered from 0 to n-1 which has
        # some apples in their vertices
        # 1 second to walk over one edge of the tree
        # minimum time (s) you have to spend to
        # collect all apples in the tree, starting at vertex
        # 0 and coming back to this vertex
        # the edges of the tree are given in the
        # array edges, where edges[i] = [a1, b1]
        # hasApple, where hasApple[i] == true
        # mean that vertex i has an apple, otherwise
        # it doesn't have any apple

        # o
        # return the min time to collect all apple

        # c
        # n >= 1 <= 10^5
        # len(edges) == n -1
        # len(edges[i]) == 2
        # ai < bi >= 0 <= n - 1
        # len(hasApple) == n

        # e
        connection = {

        }

        traversed = set()



        for v1, v2 in edges:
            if v1 not in connection:
                connection[v1] = [v2]

            else:
                connection[v1].append(v2)

            if v2 not in connection:
                connection[v2] = [v1]

            else:
                # already
                connection[v2].append(v1)

        # v : [v1, v2, v3, v4]

        # sol1
        def min_time(index):
            nonlocal traversed
            if index not in traversed:
                traversed.add(index)


            if index not in connection:
                if hasApple[index]:
                    return 0, True

                else:
                    return 0, False

            else:
                # not leaf
                can = []

                for l in connection[index]:
                    
                    if l in traversed:
                        continue

                    result, a = min_time(l)

                    if result > 0 or a:
                        can.append(result + 2)

                    else:
                        # result == 0
                        continue

                m = sum(can)

                if m == 0 and hasApple[index]:
                    return 0, True

                elif m == 0 and not hasApple[index]:
                    return 0, False

                elif m > 0 and not hasApple[index]:
                    return m, True

                elif m > 0 and hasApple[index]:
                    return m, True

        return min_time(0)[0]