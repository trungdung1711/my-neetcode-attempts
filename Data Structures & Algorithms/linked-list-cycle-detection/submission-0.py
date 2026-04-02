# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # input: head of a linked list
        # output: if linked list contains circle or not

        # constraints:
        # len(list) >= 0 <= 10^4
        # val >= -10^5
        
        # edge cases:
        # [] -> return False
        # [ 1 ] -> None, but point to itself -> cycle

        dup : set = set()

        traverse = head
        while traverse is not None:
            if traverse in dup:
                return True
            else:
                dup.add(traverse)
                traverse = traverse.next

        return False