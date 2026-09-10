# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # i
        # given a the head of a linked list
        # rotate the list to the right by k places

        # o
        # return the new list

        # c
        # number of nodes >= 0 <= 500
        # node.val >= 100 <= 100
        # k >= 0 <= 2 * 10^9

        # e
        # k == 0
        # k == number of nodes
        # rotate 0 times
        # k > number of nodes -> return k % number of nodes

        l = []

        n = 0

        traverse = head

        while traverse != None:
            l.append(traverse)
            n += 1
            traverse = traverse.next

        if n == 0:
            return None

        t = k % n

        if t == 0:
            return head

        else:
            # t < n

            # link last to first
            l[n - 1].next = l[0]
            # list prev to None
            l[n - t - 1].next = None

            return l[n - t]
