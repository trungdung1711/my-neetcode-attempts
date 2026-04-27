"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def traverse(self, root : Node):
        if root is None:
            return

        # root is not None
        for child in root.children:
            self.traverse(child)

        self.res.append(root.val)
        return


    def postorder(self, root: 'Node') -> List[int]:
        
        # input
        # root of n-ary tree
        
        # output
        # postorder traversal of that tree

        # constraints
        # #node >=0 <= 10^4
        # height <= 1000

        # edge cases
        # None -> []
        # 

        # sol2 -> iterative

        res = []
        stack = []
        expanded = set()

        stack.append(root)

        while len(stack) != 0:

            element = stack[-1]

            if element is None:
                stack.pop()
                continue
            
            # is not None
            if element in expanded:
                # it is expanded
                # now get the result
                res += [element.val]
                stack.pop()
            
            else:
                # it is not expanded
                # then expanded and
                # store it into expanded
                stack += element.children[::-1]
                expanded.add(element)
        
        return res



        # sol1 -> recursive
        # self.res = []
        # self.traverse(root)
        # return self.res