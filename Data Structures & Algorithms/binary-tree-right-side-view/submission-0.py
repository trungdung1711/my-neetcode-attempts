# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # input
        # the root of a binary tree
        # standing on the right side

        # output
        # return the values from
        # the top to the bottom

        # constraints
        # number of nodes >= 0 <= 100
        # node.val >= -100 <= 100

        # edge cases
        # [] -> []
        # [1] -> []

        if root is None:
            return []

        # contain at least root
        res = [root.val]

        levels = [[root.val]]

        queue = []

        queue.append(root)

        while len(queue) > 0:
            # for each expand
            # a new level is created
            levels.append([])

            num = len(queue)

            for i in range(num):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                    levels[-1].append(cur.left.val)

                if cur.right:
                    queue.append(cur.right)
                    levels[-1].append(cur.right.val)

            # add to res
            if len(levels[-1]) > 0:
                res.append(levels[-1][-1])

        return res