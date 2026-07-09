# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # input
        # root of a binary tree

        # output
        # return true if it is a BST
        # left subtree of a node contains only nodes which
        # value < key
        # right subtree of a node contains only nodes which
        # keys >= key
        # both left subtree and right subtree must also be BST

        # constraints
        # num (nodes) >= 1 <= 10^4
        # val >= 2^-31 <= 2^31 -1

        # edge cases
        # one node -> True

        # sol1 wrong
        # if root is None:
        #     return True

        # con = (root.val > root.left.val if root.left else True) and (root.val < root.right.val if root.right else True)

        # if not con:
        #     return False

        # # con is True
            

        # # root is not null
        # left_con = self.isValidBST(root.left)

        # right_con = self.isValidBST(root.right)

        # return left_con and right_con

        res = True

        # sol2
        def gm_lm(r):
            nonlocal res
            if r is None:
                return float("inf"), float("-inf")

            # if not r.left and not r.right:
            #     # then this is a leaf
            #     return r.val, r.val

            min_left, max_left = gm_lm(r.left)
            min_right, max_right = gm_lm(r.right)

            # r.val > max_left and r.val < min_right
            if r.val <= max_left or r.val >= min_right:
                res = False

            return min(min_left, min_right, r.val), max(max_left, max_right, r.val)

        if root is None:
            return False

        # root is not None
        gm_lm(root)

        return res
            