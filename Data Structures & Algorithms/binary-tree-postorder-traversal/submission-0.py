# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def traverse(r):
            nonlocal res

            if r is None:
                return

            # Not None
            traverse(r.left)

            traverse(r.right)

            res.append(r.val)

        traverse(root)

        return res