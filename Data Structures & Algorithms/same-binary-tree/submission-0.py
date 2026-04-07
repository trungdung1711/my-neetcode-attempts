# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # input
        # output
        # constraint
        # edge cases

        # 3 conditions and recursion
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False

        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        n = True if p.val == q.val else False

        res = l and r and n
        return res