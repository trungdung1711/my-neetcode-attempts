class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # input
        # a string s consisting of words and spaces

        # output
        # length of the last word in the string

        # constraints

        # edge cases

        count = 0

        index = len(s) - 1

        while index >= 0:
            if count == 0 and s[index] == " ":
                None

            elif count > 0 and s[index] == " ":
                break

            else:
                count += 1

            index -= 1

        return count