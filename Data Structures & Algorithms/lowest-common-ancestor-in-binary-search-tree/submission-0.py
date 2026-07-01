# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # input
        # given a binary search tree

        # output
        # find the lowest common ancestor (LCA)
        # of the two given nodes in the BST

        # constraints
        # number of nodes >= 2 <= 10^5
        # val (node) >= -10^9 <= 10^9
        # All val(node) is unique
        # p != q
        # p and q exist in the BST

        # edge cases
        # [2, 1] -> 2

        # it must be a reason why the tree is a binary search tree
        # we can use the property of the binary search tree

        traverse = root

        low = min(p.val, q.val)
        high = max(p. val, q.val)

        while not (traverse.val >= low and traverse.val <= high):
            # continue to search for value
            if traverse.val < low:
                traverse = traverse.right

            elif traverse.val > high:
                traverse = traverse.left

        else:
            # stop because
            return traverse