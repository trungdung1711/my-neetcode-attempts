# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        
        # i
        # root of a binary tree

        # o
        # true if it is complete binary tree

        # c
        # num(nodes) >= 1 <= 100
        # node.val >= 1 <= 1000

        # e
        # there is one node -> true

        queue = deque()

        queue.append(root)

        i = 0
        while queue:

            num = len(queue)

            for i in range(0, num):
                n = queue.pop()

                if n:
                    queue.append(n.left)
                    queue.append(n.right)

            # new row
            i += 1
            flag = True
            num_node = 0
            for n in queue:
                if n and flag == False:
                    return False

                if n is None and flag == True:
                    flag = False
                    return False

                num_node += 1

            if num_node == 0:
                return True

        return True