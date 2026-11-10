# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        # i
        # root of a binary tree
        # check whether it is a mirror of itself

        # o
        # True if it is a mirror of itself

        # c
        # number of nodes >= 1 <= 1000
        # node.val >= -100 <= 100

        # e
        # if there is one node -> True

        # a tree is symmetric if left == right
        if root is None:
            return True

        def isSymmetric(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None and r2 or r1 and r2 is None:
                return False

            return r1.val == r2.val and (isSymmetric(r1.left, r2.right) and isSymmetric(r1.right, r2.left))

        return isSymmetric(root.left, root.right)