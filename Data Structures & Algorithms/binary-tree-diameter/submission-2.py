# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
result = 0

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global result
        # input
        # root binary tree
        # output
        # len(diameter) == longest
        # path between two nodes
        # len = number of edges between them

        # constraints
        # num(nodes) >= 1
        # val >= -100

        # edge case
        # nodes == 1 -> 0

        # left -> longest path from root
        # right -> longest path from root
        # +
        # return

        self.res = 0

        def max_deep_from_node(root : Optinal[TreeNode]) -> int: 
            if root is None:
                return 0

            max_left = max_deep_from_node(root.left) + (1 if root.left else 0)
            max_right = max_deep_from_node(root.right) + (1 if root.right else 0)

            diameter = max_left + max_right

            self.res = max(diameter, self.res)

            return max(max_left, max_right)

        max_deep_from_node(root)

        return self.res