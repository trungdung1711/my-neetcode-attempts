# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # input
        # a binary tree

        # output
        # level order traversal of its nodes' values
        # from left to right, level by level

        # constraints
        # number of nodes >= 0 <= 2000
        # node.val >= -1000 <= 1000

        # edge cases
        # [] -> []
        # [1] -> [[1]]

        queue = []
        res = []

        if root is None:
            return []


        queue += [root]

        while len(queue) > 0:
            # for this level
            res += [[]]

            n = len(queue)

            for i in range(n):
                node = queue.pop(0)
                
                res[-1] += [node.val]

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            # done in one level


        return res