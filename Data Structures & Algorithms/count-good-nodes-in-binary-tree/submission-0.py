# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # input
        # a binary tree
        # root
        # X is called
        # a good node if
        # in the path from root to X
        # there are no nodes with
        # the values greater than X

        # output
        # number of
        # good nodes

        # constraints
        # number of nodes >= 1 <= 10^5
        # values >= -10^4 <= 10^4

        # edge cases
        # there is only root
        # return that node

        res = 0

        def dfs(root, m):
            nonlocal res
            if root is None:
                return

            if root.val >= m:
                res += 1

            # children
            new_max = root.val if root.val >= m else m

            dfs(root.left, new_max)
            dfs(root.right, new_max)

        dfs(root, float("-inf"))

        return res