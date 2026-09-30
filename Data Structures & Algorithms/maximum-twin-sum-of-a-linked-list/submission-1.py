# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        
        # i
        # linked list of size n
        # n is even
        # the ith node
        # it has a twin at (n - 1)
        # if 0 <= i <= (n / 2) - 1

        # o
        # twin sum is defined as the sum
        # of a node and its twin
        # given the head of the linked list
        # return the maximum twin sum of the linked list

        # c
        # num(nodes) >= 2 <= 10^5
        # node.val >= 1 <= 10^5

        # e
        # [1. 10] -> return 11

        # 1. using the stack
        # but we don't know the length
        # stack = deque

        # traverse = head
        # index = 0

        # while traverse:
            
        #     if index >= 0 and index <=

        # 2. using a simple array
        # create the sum while traverse the linked list
        a = []
        # next
        # index = 0

        # next
        traverse = head

        while traverse:

            a.append(traverse.val)

            traverse = traverse.next

        res = -float("inf")

        i = 0
        j = len(a) - 1

        while i < j:
            can = a[i] + a[j]
            if can > res:
                res = can

            i += 1
            j -= 1

        return res