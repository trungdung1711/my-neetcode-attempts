# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # input
        # root binary tree
        # output
        # len(diameter) == longest
        # path between two nodes
        # len = number of edges between them

        # constraints
        # num(nodes) >= 1
        # val >= -100

        # edge case
        # nodes == 1 -> 0

        # left -> longest path from root
        # right -> longest path from root
        # +
        # return

        if root is None:
            return 0

        path_left = self.diameterOfBinaryTree(root.left)
        path_right = self.diameterOfBinaryTree(root.right)
        
