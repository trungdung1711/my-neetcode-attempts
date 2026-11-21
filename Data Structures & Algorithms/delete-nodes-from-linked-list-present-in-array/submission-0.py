# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # i
        # nums
        # head

        # o
        # head of a linked list
        # removing all nodes from the linked list
        # value that exists in nums

        # c
        # len(nums) >= 1 <= 10^5
        # nums[i] >= 1 <= 10^5
        # all elements in nums are unique
        # number of nodes >= 1 <= 10^5
        # node.val >= 1 <= 10^5
        # after deleting -> at least one node left

        # e

        sentinal = ListNode()
        prev = sentinal

        nums_set = set(nums)

        traverse = head

        while traverse is not None:

            # linked
            if traverse.val not in nums_set:
                prev.next = traverse
                prev = prev.next

            else:
                # unlink
                prev.next = None

            traverse = traverse.next

        return sentinal.next