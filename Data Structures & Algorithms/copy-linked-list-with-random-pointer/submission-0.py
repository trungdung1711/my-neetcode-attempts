"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # input
        # a linked list with random pointer

        # output
        # a new deep copied linked list
        # with the random pointer is copied correctly

        # constraints
        # len(list) >= 0 <= 1000
        # node.random is either null or pointing to some node

        # edge case
        # null -> null

        linked = {}

        traverse = head
        nil = Node(10001, None, None)
        pre = nil

        while traverse is not None:
            cp = Node(traverse.val)
            linked[traverse] = cp
            pre.next = cp
            pre = cp
            traverse = traverse.next

        new_head = nil.next

        traverse = head
        curr = nil.next

        while traverse is not None:
            if traverse.random is None:
                ran = None
            else:
                ran = linked[traverse.random]
            
            curr.random = ran

            traverse = traverse.next
            curr = curr.next

        return nil.next
            

