# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # input
        # head of linked list
        # output
        # reorder the list
        # 0 - 1 - 2 - 3 - 4 - 5
        # 0 - 5 - 1 - 4 - 2 - 3

        # constraints
        # len(list) >= 1
        # val >= 1

        # edge cases:
        # 4 -> 3
        # 1, 3 -> 1, 3
        # 1 2 3 -> 1 3 2

        # 1. slow/fast -> find the middles
        # loop invariant
        # before [] -> after [x]

        nil = ListNode(next = head)
        slow = nil
        fast = nil

        # Go ahead, if there is a way
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        half = slow.next

        # reverse that list
        prev = None
        curr = half

        # curr is just nodes of the list
        # loop for all the nodes
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt


        # prev is the new head
        # merge them together
        curr = head
        while prev is not None:
            nxt1 = curr.next
            nxt2 = prev.next
            curr.next = prev
            prev.next = nxt1
            prev = nxt2
            curr = nxt1
        
        curr.next = None