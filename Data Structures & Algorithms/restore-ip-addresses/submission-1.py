class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # i
        # IP address consists
        # exactly 4 integers separated by a single dots
        # each value is between 0 and 255, and cannot have leading zeros -> checking for leading 0
        # but 0.1.2.3 is a valid IP address
        # given a string containing only digits

        # o
        # all possible valid IP addresses, that can be formed
        # by inserting dots into s
        # you are not allowed to reorder or remove any digits
        # return the result in any order

        # c
        # len(s) >= 1 <= 20
        # s consists of digits only

        # e
        # len(s) >= 4
        # len(s) < 4
        # 1 -> no insertion
        # 23 -> one insertions
        # 123 -> two insertions
        # 1234 -> thress insertions

        if len(s) < 4:
            return []

        res = []
        # 1 2 3

        def backtracking(count, num, ip):
            nonlocal res

            # choices
            if count < 3:
                for i in range(1, len(num)):
                    # do operation
                    number = num[0:i]

                    if self.is_valid(number):
                        # further
                        backtracking(count + 1, num[i:], ip + number + ".")

                    else:
                        # not a valid one
                        continue

            elif count == 3:
                # insert the third dot
                for i in range(1, len(num)):
                    # insert
                    number1 = num[0:i]
                    number2 = num[i:]

                    if self.is_valid(number1) and self.is_valid(number2):
                        res.append(ip + number1 + "." + number2)

                    else:
                        # one of the two is not a valid
                        continue

        backtracking(1, s, "")

        return res



    def is_valid(self, s):
        # what should be a valid one
        if len(s) == 1:
            return True
        
        # leading 0
        if len(s) >= 2 and s[0] == "0":
            return False

        # values
        v = int(s)
        if not (v >= 0 and v <= 255):
            return False

        return True