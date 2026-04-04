# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # input:
        # root of binary tree
        # output:
        # invert the tree, and return its root

        # constraints:
        # node_num  >= 0
        # val >= -100, <= 100

        # edge case
        # node_num == 0 -> None

        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root