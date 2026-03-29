# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # input:
        # head of a singly linked list
        # output:
        # return the second middle node

        # constraints:
        # len(list) >= 1

        # edge case
        # len(list = 1) -> return it
        # even -> second
        # odd -> middle

        traverse = head
        size = 0

        while traverse is not None:
            size += 1
            traverse = traverse.next

        # not 0-based
        middle_index = size // 2 + 1

        count = 0
        nil = ListNode(next = head)
        traverse = nil

        # input -> prev
        # output -> done that node
        while count < middle_index:
            count += 1
            traverse = traverse.next

        return traverse
