class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        # i
        # details
        # information -> str 15
        # 10c -> phone
        # 1c -> gender
        # 2c -> age [12, 13] -> [11, 12]
        # 2c -> seat

        # o
        # #pass where p.age > 60

        # c

        # e

        res = 0
        for d in details:
            age = int(d[11:13])

            if age > 60:
                res += 1

        return res