# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:

        # base case
        if r1 is None and r2 is None:
            return True

        elif r1 is None and r2 is not None:
            return False

        elif r1 is not None and r2 is None:
            return False

        # both is not None

        left_cond = self.sameTree(r1.left, r2.left)
        right_cond = self.sameTree(r1.right, r2.right)

        root_cond = True if r1.val == r2.val else False
        return left_cond and right_cond and root_cond


    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> None:
        if root is None:
            return
        # process
        value = self.sameTree(root, subRoot)
        if value:
            self.result = True

        # process left
        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.result = False
        self.dfs(root, subRoot)
        return self.result
    

