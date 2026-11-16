# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode | None, root: TreeNode | None) -> bool:
        
        # i
        # binary tree root
        # a linked list with head as the first node

        # o
        # true -> all elements starting from the head correspond
        # to some downward path connected in the binary tree
        # false otherwise

        # c
        # number of nodes >= 1 <= 2500
        # number of nodes (list) >= 1 <= 100
        # node.val >= 1 <= 100

        # e
        # 1 2 3
        # 1 1 1 2 3

        m = {

        }
        
        def collect(r):
            if r is None:
                return

            if r.val in m:
                m[r.val].append(r)

            else:
                m[r.val] = [r]

            collect(r.left)
            collect(r.right)

        collect(root)

        if head.val not in m:
            return False

        candidates = m[head.val]

        def advance(r, h):
            if h is None:
                return True

            if r is None:
                return False
            
            if r.val == h.val:
                return advance(r.left, h.next) or advance(r.right, h.next)

            return False

        for c in candidates:

            if advance(c, head):
                return True

            else:
                continue

        return False