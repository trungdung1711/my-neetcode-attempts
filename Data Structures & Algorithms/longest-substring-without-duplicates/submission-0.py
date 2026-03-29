class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # input: string s
        # output: longest substring without duplicate characters

        # constrants:
        # len(s) >= 0
        # s: 'a' , '1', symbols and spaced

        # edge cases:
        # "a" -> a
        # "" -> ""

        if len(s) <= 1:
            return len(s)

        max : int = -1

        # At each character, maintain the index
        # whether from that index to the index - 1
        # we have the current longest subarray without
        # duplication
        # check the current index, can it be the next character to expand the substring
        # if yes -> add to the set -> expand
        # if no -> duplicate happens -> new substring must be created
        # change the window to check for the next window

        # initialization
        first : int = 0
        second : int = 0
        dup : set = set()

        for index, c in enumerate(s):
            if c in dup:
                # duplication happens
                # longest substring breaks
                # must move the slide -> prevent breaks
                if len(dup) >= max:
                    # set will be reset
                    max = len(dup)
                
                # change the first and the dup set
                # we want to exclude elements up until the dup one
                # because the dup one breaks the unique -> next character
                while first < second and s[first] != s[second]:
                    dup.remove(s[first])
                    first += 1
                
                first += 1
                # no need to add c
            else:
                # the window can be expanded
                dup.add(s[second])
            

            second += 1

        # check for the final set
        if len(dup) >= max:
            max = len(dup)

        return max