class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # i
        # a long flowerbed in which
        # some of the plots are planted
        # and some are not
        # flowers cannot be plated in adjacent plots
        # 0 -> empty
        # 1 -> not empty
        # n

        # o
        # true if n new flowers can be planted in the flowerbed
        # false otherwise

        # c
        # len(flowerbed) >= 1 <= 2 * 10^4
        # flowerbed[i] = {0, 1}
        # no two ajacent flowers in the flowerbed
        # n >= 0 <= len(flowerbed)

        # e
        # len(flowerbed) == 1 -> 1 can be planted
        # len(flowerbed) == 2 -> 1 can be planted

        # we are greedy
        i = 0

        while i < len(flowerbed) and n > 0:

            if flowerbed[i] == 0:

                # further checking
                if i - 1 >= 0 and flowerbed[i - 1] == 1:
                    i += 1
                    continue
                
                elif i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
                    i += 3
                    continue

                # then plant it
                flowerbed[i] = 1
                n -= 1

            else:
                # plant
                # then we need to move to a
                # non planted one
                i += 2

        # violation
        return True if n == 0 else False