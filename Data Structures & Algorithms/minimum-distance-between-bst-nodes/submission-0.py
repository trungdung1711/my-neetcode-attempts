# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        
        # i
        # root of a BST
        # return minimum difference between
        # the values of any two different nodes in the tree

        # o
        # minumum of difference between any 2 different nodes in the tree
        # smaller -> middle -> larger
        # 

        # c
        # the number of nodes in the range [2, 100]
        # node.val >= 0 <= 10^5

        # e

        arr = []

        # min
        # maximize left
        # minimize right

        def inorder(r):
            nonlocal arr

            if r:
                inorder(r.left)
                arr.append(r.val)
                inorder(r.right)

        inorder(root)


        # 1 2 3 4 6
        # 0 1 12 48 49
        res = float("inf")

        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < res:
                res = arr[i] - arr[i - 1]

        return res