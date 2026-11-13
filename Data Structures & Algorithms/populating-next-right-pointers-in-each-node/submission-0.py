"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        # i
        # perfect binary tree
        # all leaves are on the same level
        # every parents has 2 children

        # o
        # poplulate each next pointer to point to its next right node
        # no next right node => the next point should point to NULL
        # initially all next pointers are set to NULL

        # c
        # num of nodes in tree >= 0 <= 2^12 - 1
        # node.val >= -1000 <= 1000

        # e
        # root is None ->
        # there is only one node

        if root is None:
            return root

        

        map_level_right = {
            # 0: root
        }

        def in_order(r, level = 0):
            # map later

            # left
            if r is None:
                return

            # map
            if level in map_level_right:
                # -> infinite loop
                map_level_right[level].next = r

            # not None
            in_order(r.left, level + 1)

            
            # None -> update
            map_level_right[level] = r

            # right
            in_order(r.right, level + 1)

        in_order(root)

        return root