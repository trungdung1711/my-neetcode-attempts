# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # input
        # binary tree
        # output
        # true if height-balanced otherwise None

        # constraints
        # num(node) >= 0
        # val >= -10^4

        # edge case
        # root == None -> True
        # root = 1 -> True

        res = True

        def height(root : Optional[TreeNode]) -> int:
            nonlocal res
            
            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            h = max(left_height, right_height) + 1
            diff = abs(left_height - right_height)

            if diff > 1:
                res = False
            
            return h

        height(root)
        
        return res