class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # i
        # a string s
        # an integer k
        # k duplicate removal
        # choosing k adjacent and equal letters from s
        # removing them
        # causing the left and right side -> concatenate together
        # repeatedly make k duplicate removals until we no longer
        # can

        # o
        # return the final string after such duplicate removals
        # have been made
        # the answer is guaranteed to be unique

        # c
        # len(s) >= 1 <= 10^5
        # k >= 2 <= 10^4
        # s only contains lowercase English letter

        # e
        # if k = 2, but there is nothing to remove
        # k = 3 dddd -> kill ddd d or d ddd -> return the same

        # 1.
        # Use the stack
        # Continuously add the pair (c, count)
        # as we don't know whether or not the c is unique
        # if count >= k -> remove
        # tuple is immutable

        stack = deque()

        for c in s:
            if len(stack) == 0:
                stack.append((c, 1))

            else:
                # len(stack) > 0
                last_c, last_count = stack[-1]
                if last_c == c:
                    # same character
                    # added together
                    last_count += 1
                    if last_count == k:
                        # then we can remove them
                        stack.pop()

                    else:
                        stack.pop()
                        stack.append((c, last_count))

                else:
                    # different character
                    stack.append((c, 1))

        # inside the stack
        res = ""
        for c, count in stack:
            res += "".join([c] * count)

        return res

                        