# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # i
        # the root of a binary tree
        # containing digits from 0 to 9
        # each root to leaf path in the tree represents a number

        # o
        # total sum of all root-to-leaf numbers

        # c
        # leaf node is a node with no children
        # num(nodes) >= 1 <= 1000
        # node.val >= 0 <= 9

        # e
        # leading 0 -> can be handled
        # only the root -> can be handled

        res = 0

        def dfs(r, v):
            nonlocal res
            if not r.left and not r.right:
                # this is the left node
                res += v * 10 + r.val

            else:
                # normal node
                # go to left, go to right
                dfs(r.left, v * 10 + r.val) if r.left else None
                dfs(r.right, v * 10 + r.val) if r.right else None

        dfs(root, 0)

        return res