class Solution:
    def makeGood(self, s: str) -> str:
        
        # i
        # a string s of lower can upper case English letters
        # good string which doesn't have 
        # 2 adjacent character s[i] and s[i + 1]
        # i >= 0 i <= s.length - 2
        # s[i] is lower-case letter and s[i + 1] same letter but upper-case
        # make the string good -> choose 2 adjacent characters -> make string bad
        # and remove them, keep doing this unti the string becomes good

        # o
        # remove eE or Ee to make the string good
        # remove everything to make it good

        # c
        # len(s) >= 1 <= 100
        # s contains only lower and upper case English letters

        # e
        # len(s) == 0 -> return
        # len(s) == 1 -> return

        if len(s) <= 1:
            return s

        stack = deque()
        # stack.append(s[i])

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])

            else:
                if ( s[i] != stack[-1] ) and ( s[i].lower() == stack[-1] or s[i] == stack[-1].lower() ):
                    # this will make string bad
                    stack.pop()

                else:
                    stack.append(s[i])

        return "".join(list(stack))