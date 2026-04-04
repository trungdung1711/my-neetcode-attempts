# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # input:
        # root
        # output
        # return maximum depth = number of nodes (longest path)

        # constraints
        # numNode >= 0
        # val <= -100 , >= 100

        # edge cases
        # numNode = 0 -> 0
        # numNode = 1 -> 1

        # func: return maxDepth
        # assume it works
        # build answer from that

        if root is None:
            return 0

        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)

        maxNode = max (maxLeft, maxRight) + 1

        return maxNode