# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # i
        # the root of a binary tree

        # o
        # return zigzag level order traversal
        #  of its notes' values
        # from left to right, then right to left

        # c
        # num(nodes) >= 0 <= 2000
        # node.val >= -100 <= 100

        # e
        # root is None -> []
        # one note, only the root -> [[root.val]]

        res = []

        def traverse(flag, n):
            nonlocal res

            if len(n) == 0:
                return

            new_n = []
            new_r = []

            if flag:
                # left to right
                for i in range(len(n) - 1, -1, -1):
                    node = n[i]
                    new_r.append(node.val)
                    new_n.append(node.left) if node.left else None
                    new_n.append(node.right) if node.right else None

            else:
                # right to left
                for i in range(len(n) - 1, -1, -1):
                    node = n[i]

                    new_r.append(node.val)
                    new_n.append(node.right) if node.right else None
                    new_n.append(node.left) if node.left else None

            res.append(new_r)

            traverse(not flag, new_n)

        traverse(True, [root] if root else [])

        return res