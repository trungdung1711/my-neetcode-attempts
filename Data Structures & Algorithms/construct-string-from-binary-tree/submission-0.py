# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        # i
        # binary tree -> string
        # node's value -> its children
        # enclose each child's representation
        # in parentheses, with the left child
        # before the right child

        # o
        # string representation
        # for the binary tree

        # e

        # c
        # num_node(tree) >= 1 <=10000
        # node.val >= -1000 <= 1000

        def helper(root):

            if root.left is None and root.right is None:
                return str(root.val)

            elif root.left is None and root.right:
                return f"{root.val}" + f"()" +f"({helper(root.right)})"

            elif root.left and root.right is None:
                return f"{root.val}" + f"({helper(root.left)})"

            else:
                return f"{root.val}" + f"({helper(root.left)})" + f"({helper(root.right)})"

        return helper(root)