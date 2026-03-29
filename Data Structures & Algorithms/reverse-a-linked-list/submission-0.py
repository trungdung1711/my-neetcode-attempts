# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # input: head of a singly linked list
        # output: reversed list

        # constraits:
        # len(list) >=0 <= 5000

        # edge case
        # len(list) == 0 -> head == None -> return
        # len(list) == 1-> head.next = None -> return

        if head is None:
            return None

        pre = None
        cur = head
        next = head.next

        while cur is not None:
            cur.next = pre

            pre = cur
            
            # if next is none -> cur is None -> next loop stop
        
            cur = next
            if next:
                next = next.next

        return pre
        