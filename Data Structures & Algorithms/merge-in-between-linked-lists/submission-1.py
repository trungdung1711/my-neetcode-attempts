# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        # i
        # 2 linked lists
        # list1 and list2
        # size n and m
        # remove list1's nodes from a to b
        # and put list2 in their place

        # o
        # return the new list
        # a - b is removed
        # list2 is placed inside a - b

        # c
        # len(list1) >= 3 <= 10^4
        # a b >= 1 < len(list1) -1
        # len(list2) >= 1 <= 10^4

        # e
        # same - remove a node and place list2

        i = 0

        traverse = list1

        b1 = None
        b2 = None

        while traverse != None:

            if i == a - 1:
                b1 = traverse

            if i == b + 1:
                b2 = traverse

            i += 1
            traverse = traverse.next

        traverse = list2

        while traverse and traverse.next != None:
            traverse = traverse.next

        tail = traverse

        b1.next = list2
        tail.next = b2

        return list1