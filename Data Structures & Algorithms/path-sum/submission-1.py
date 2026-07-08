# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # input
        # root of binary tree
        # integer targetSum

        # output
        # true if the tree has a root-to-left
        # that adding up all values along the path
        # equal to targetSum

        # constraints
        # number of nodes >= 0 <= 5000
        # node.val >= -1000 <= 1000
        # sum >= -1000 <= 1000

        # edge cases
        # one root == targetSum
        
        # sol1
        # def dfs(r, sum):
        #     if r is None:
        #             return False

        #     if r.left is None and r.right is None:
        #         # a leaf
        #         if sum + r.val == targetSum:
        #             return True
            
        #     left = False
        #     right = False

        #     # not a leaf
        #     if r.left:
        #         left = dfs(r.left, sum + r.val)

        #     if r.right:
        #         right = dfs(r.right, sum + r.val)

        #     return left or right

        # return dfs(root, 0)

        # sol2
        if root is None:
            return False

        res = False


        def dfs(root, sum):
            nonlocal res
            if not root.left and not root.right:
                # a left
                if sum + root.val == targetSum:
                    res = res or True
                
                else:
                    None

            # it is not a left
            if root.left:
                dfs(root.left, sum + root.val)

            if root.right:
                dfs(root.right, sum + root.val)

            return

        dfs(root, 0)

        return res