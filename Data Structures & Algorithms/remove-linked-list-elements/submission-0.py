# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # input:
        # head of a linked list and an integer val
        # output:
        # linked that all node vals are removed

        # constraints:
        # len(list) >= 0

        # edge cases:
        # len(list) == 0 -> return None
        # len(list) == 1
        # val == head -> change head

        if head is None:
            return None

        traverse = head
        prev = None

        while traverse is not None:
            if traverse.val == val:
                # This node must be removed
                if traverse is head:
                    head = traverse.next
                
                else:
                    # traverse is not head
                    prev.next = traverse.next
            
            else:
                prev = traverse

            
            traverse = traverse.next

        return head