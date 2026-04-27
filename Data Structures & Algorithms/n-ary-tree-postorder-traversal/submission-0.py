"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def traverse(self, root : Node):
        if root is None:
            return

        # root is not None
        for child in root.children:
            self.traverse(child)

        self.res.append(root.val)
        return


    def postorder(self, root: 'Node') -> List[int]:
        
        # input
        # root of n-ary tree
        
        # output
        # postorder traversal of that tree

        # constraints
        # #node >=0 <= 10^4
        # height <= 1000

        # edge cases
        # None -> []
        # 

        self.res = []
        self.traverse(root)
        return self.res