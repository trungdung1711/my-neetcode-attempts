# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # input:
        # heads of two sorted linked lists
        # output:
        # the head of one merged list (l1 and l2)

        # constraints
        # len(l1), len(l2) >=0 <= 50
        # non-ascending 1 1 1 

        # edge case:
        # h1 = None -> return h2
        # h2 = None -> return h1
        # Both None

        nil = ListNode(val=9999, next=None)
        curr = nil

        while list1 and list2:
            # not None
            nxt = list1 if list1.val <= list2.val else list2
            curr.next = nxt
            curr = curr.next
            if list1.val <= list2.val:
                list1 = list1.next
            else:
                list2 = list2.next

        # one of the twos is None
        if list1 is None:
            curr.next = list2
        
        if list2 is None:
            curr.next = list1

        return nil.next
        