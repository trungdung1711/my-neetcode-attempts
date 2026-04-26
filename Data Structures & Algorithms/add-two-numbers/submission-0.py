# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # input
        # non-empty linked lists
        # non negative ints
        # reverse order
        
        # output
        # add the two numbers
        # return the sum of the two numbers

        # constraints
        # no leading zeros
        # len(linked list) >= 1 <= 100
        # node.val >=0 <= 9 (single digit)
        # no leading zeros

        nil = ListNode(val=10, next=None)
        prev = nil
        remember = False
        t1 = l1
        t2 = l2

        while t1 is not None or t2 is not None:

            if t1 is not None and t2 is not None:
                a = t1.val
                b = t2.val

            elif t1 is None:
                a = 0
                b = t2.val
            elif t2 is None:
                a = t1.val
                b = 0

            sum = a + b + (1 if remember else 0)
            if sum < 10:
                res = sum
                remember = False
            else:
                res = sum - 10
                remember = True

            new_node = ListNode(val = res, next=None)
            prev.next = new_node
            prev = new_node

            if t1 is not None:
                t1 = t1.next
            
            if t2 is not None:
                t2 = t2.next

        # we need to check the final remember
        if remember:
            new_node = ListNode(val = 1, next=None)
            prev.next = new_node
            prev = new_node

        return nil.next
