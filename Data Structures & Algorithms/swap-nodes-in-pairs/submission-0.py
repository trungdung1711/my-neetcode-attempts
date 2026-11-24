# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        
        # i
        # linked list
        # swap every two adjacent nodes
        # return its head
        # no modifying the values in the list nodes

        # o
        # return the head of the swapped list

        # c
        # number of nodes >= 0 <= 100
        # node.val >= 0 <= 100

        # e

        sentinal = ListNode()

        traverse = head

        if traverse is None:
            return None
        
        if traverse.next is None:
            return traverse

        # at least 2
        prev = sentinal
        while traverse and traverse.next:

            n = traverse.next.next

            # prev traverse traverse.next
            prev.next = traverse.next
            traverse.next.next = traverse
            prev = traverse

            traverse = n

        if traverse:
            prev.next = traverse

        else:
            prev.next = None

        return sentinal.next