class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # input
        # given a string s

        # output
        # longest palindromic substring in s

        # constraints
        # len(s) >= 1 <= 1000
        # s consists of only digits and letters

        # edge cases
        # "a" -> return that


        max_length = 0
        max_i = 0
        max_j = 0

        for index in range(len(s)):
            current_length = 1

            i = index - 1
            j = index + 1

            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    current_length += 2
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
                    break

            if current_length > max_length:
                max_length = current_length
                max_i = i
                max_j = j

        
        return s[max_i:max_j + 1]
            