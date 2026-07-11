# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # input
        # root of a BST
        # low and high

        # output
        # sum of values
        # of all nodes which have values >= low <= high
        # inclusively

        # constraints
        # num(nodes) >= 1<= 2*10^4
        # node.val >= 1 <- 10^5
        # low <= high >= 1 <= 10^5
        # all node.val are unique

        # edge cases

        # sol1: just a normal tree
        res = 0
        def dfs(r):
            nonlocal res

            if r is None:
                return

            # not None
            if r.val >= low and r.val <= high:
                res += r.val

            dfs(r.left)
            dfs(r.right)

        dfs(root)

        return res