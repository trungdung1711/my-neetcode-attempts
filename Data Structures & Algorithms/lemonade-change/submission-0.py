class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # i
        # each lemonade costs $5
        # customers in a queue
        # each customer can only buy one
        # and pay with $5, $10, or $20
        # I don't have any change at first
        # given bills, bills[i]

        # o
        # return True, provide every customer
        # with the correct change
        # false otherwise

        # c
        # len(bills) >= 1 <= 10^5
        # bills[i] is i for i = {5, 10, 20}

        # e
        # first customer is 10 or 20 -> can't do
        my_money = [0, 0, 0]

        for bill in bills:
            if bill == 5:
                my_money[0] += 1

            elif bill == 10:
                # return 5
                if my_money[0] > 0:
                    my_money[0] -= 1
                    my_money[1] += 1

                else:
                    return False

            else:
                # bill == 20
                # two choices
                # one 5 and one 10
                # or 3 5s

                if my_money[0] and my_money[1]:
                    my_money[0] -= 1
                    my_money[1] -= 1

                elif my_money[0] >= 3:
                    my_money[0] -= 3
                

                else:
                    return False

        return True