# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # i
        # root of a BST
        # value to insert into

        # o
        # return the root
        # after insertion

        # c
        # the value does not exist in the original tree
        # num(nodes) >= 0 <= 10^4
        # node.val >= -10^8 <- 10^8
        # all values are unique
        # val does not exist in the orginal BST

        # e
        # if root is None -> return that
        # not None -> left right

        if root is None:
            return TreeNode(val=val)

        # root is not None
        traverse = root

        while traverse:
            if val > traverse.val:
                
                if traverse.right is None:
                    # insert
                    traverse.right = TreeNode(val=val)
                    break

                else:
                    traverse = traverse.right

            else:
                # val < traverse.val
                if traverse.left is None:
                    # insert
                    traverse.left = TreeNode(val=val)
                    break

                else:
                    traverse = traverse.left

        return root