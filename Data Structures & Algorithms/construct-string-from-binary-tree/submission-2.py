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

        if root is None:
            return ""

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node is None:
                result.append(")")
            else:
                result.append("(")
                result.append(str(node.val))

                stack.append(None)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)
                elif node.right:
                    result.append("()")

        return "".join(result)[1:-1]