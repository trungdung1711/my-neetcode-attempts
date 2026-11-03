# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # i
        # head of a linked list and int k

        # o
        # head of the new linked list
        # swapping values of kth node -->
        # swapping values of kth node <--

        # c
        # len(list) == n
        # k >= 1 <= n <= 10^5
        # node.val >= 0 <= 100

        # e
        m = {

        }

        i = 0

        t = head
        while t:
            i += 1
            m[i] = t
            t = t.next
        # i == len
        n = i
        m[k].val, m[n - k + 1].val = m[n - k + 1].val, m[k].val

        return head