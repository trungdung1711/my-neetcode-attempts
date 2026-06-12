class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        # input
        # blocks of "W" and "B"
        # integer k, number of consecutive black blocks
        # one operation = recolor a white block
        # a white block -> black block

        # output
        # min of operations
        # -> one occurence of
        # k consecutive black blocks

        # constraints
        # n = len(blocks)
        # n >= 1 <= 100
        # blocks[i] belongs {"W", "B"}
        # k >= 1 <= n

        # edge cases
        # BBB -> return 0
        # if there are all whites -> return k

        whites = 0

        for i in range(k):
            if blocks[i] == "W":
                whites += 1
        
        res = whites

        for i in range (k, len(blocks)):
            # move window
            if blocks[i] == "W":
                whites += 1
            
            if blocks[i - k] == "W":
                whites -= 1

            if (whites) < res:
                res = whites

        return res