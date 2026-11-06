# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        
        # i
        # 2D integer array
        # descriptions
        # descriptions[i] == [parent_i, child_i, isLeft_i]
        # binary tree unique of value

        # o
        # construct the binary tree
        # return its root
        # the binary is valid

        # c
        # len(descriptions) >= 1 <= 10^4
        # len(description) == 3
        # parent_i, child_i >= 1 <= 10^5
        # isLeft_i >= 0 <= 1
        # the binary tree is valid

        # e

        root = None
        parents = set()
        children = set()
        m = {}

        for p, c, isLeft in descriptions:
            parent = None
            child = None

            if p in m:
                parent = m[p]
            
            else:
                m[p] = TreeNode(p, None, None)
                parent = m[p]

            if c in m:
                child = m[c]
            
            else:
                m[c] = TreeNode(c, None, None)
                child = m[c]

            if isLeft == 1:
                parent.left = child
            else:
                parent.right = child

            # we are not sure to discard the children
            # at a time -> 
            parents.add(p)
            children.add(c)

        root_val = list(parents - children)[0]
        return m[root_val]
