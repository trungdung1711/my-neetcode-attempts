
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        h1 = t1 = None
        h2 = t2 = None

        traverse = head

        while traverse:
            nxt = traverse.next

            # detach the current node
            traverse.next = None

            if traverse.val < x:
                if h1 is None:
                    h1 = t1 = traverse
                else:
                    t1.next = traverse
                    t1 = traverse
            else:
                if h2 is None:
                    h2 = t2 = traverse
                else:
                    t2.next = traverse
                    t2 = traverse

            traverse = nxt

        # first list is empty
        if h1 is None:
            return h2

        # connect
        t1.next = h2

        return h1
