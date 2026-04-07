# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # input
        # head of a linked list
        # remove n node from the end of the list
        # output
        # head

        # constraints:
        # sz >= 1
        # val >= 0
        # n >= 1 <= sz (run from 1 to sz)

        # edge case2:
        # [1] 1 -> []
        # [1 2 ] 2 -> [2]

        arr = []
        nil = ListNode(next=head)
        arr.append(nil)

        traverse = head
        
        while traverse is not None:
            arr.append(traverse)
            # always remember to update
            # the traverse value
            traverse = traverse.next

        # index of the remove node
        sz = len(arr) - 1

        index = sz - n + 1
        # change the link
        arr[index - 1].next = arr[index].next

        return nil.next