# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # input
        # two root1 and root2
        # put one of them to conver the other
        # some nodes are overlapped, while the others aren't

        # output
        # return the tree tree
        # built from those two overlapped trees

        # constraints
        # num(nodes) >= 0 <= 2000
        # node.val >= -10000 <= 10000

        # edge cases
        # if one null -> return the other
        # if two null -> return null

        # if root1 and not root2:
        #     return root1
        
        # if root2 and not root1:
        #     return root2

        # if not root1 and not root2:
        #     return None
        
        def build_tree(r1, r2):
            if r1 and r2:
                l = build_tree(r1.left, r2.left)
                r = build_tree(r1.right, r2.right)

                return TreeNode(val=r1.val + r2.val, left=l, right=r)

            if r1 and not r2:
                l = build_tree(r1.left, None)
                r = build_tree(r1.right, None)

                return TreeNode(val=r1.val, left=l, right=r)

            if r2 and not r1:
                l = build_tree(None, r2.left)
                r = build_tree(None, r2.right)

                return TreeNode(val=r2.val, left=l, right=r)

            if not r1 and not r2:
                return None

        return build_tree(root1, root2)
