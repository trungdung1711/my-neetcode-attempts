# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # input: head of the linked list
        # output: palin -> true, not -> false

        # constraints:
        # len(list) >= 1
        # value >= 0 <= 9

        # edge cases:
        # 1 -> true

        #
        traverse = head
        s : int = 0
        while traverse is not None:
            s += 1
            traverse = traverse.next
        
        loop : int = s // 2
        # check from
        # loop + 1
        # loop + 2

        traverse = head

        prev = None
        curr = head

        for i in range (0, loop):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # prev is the head
        if s % 2 == 0:
            check = curr
        else:
            check = curr.next

        # prev is the new head
        while check is not None:
            if prev.val != check.val:
                return False

            prev = prev.next
            check = check.next

        return True

        


        # O(N), O(N)
        # lst : list = []
        # while head is not None:
        #     lst += [head.val]
        #     head = head.next
        
        # l : int = 0
        # r : int = len(lst) - 1

        # while l < r:
        #     if lst[l] != lst[r]:
        #         return False
            
        #     l += 1
        #     r -= 1
        
        # return True