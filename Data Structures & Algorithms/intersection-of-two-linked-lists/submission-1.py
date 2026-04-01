# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # input:
        # headA
        # headB
        # ouput:
        # return the node intersects
        # no intersection -> null

        # constraints:
        # m, n >= 1
        # Node.val >= 1
        # no circles

        # edge cases:
        # Same head -> return that
        
        dup : set = set()
        traverse1 = headA
        traverse2 = headB

        while traverse1:
            dup.add(traverse1)
            traverse1 = traverse1.next

        while traverse2:
            if traverse2 in dup:
                return traverse2
            
            traverse2 = traverse2.next

        return None