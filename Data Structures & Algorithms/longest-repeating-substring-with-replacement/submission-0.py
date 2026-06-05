class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # input
        # a string s and an integer k
        # choose any character
        # change it to any uppercase English character
        # perform at most k times

        # output
        # length of the longest substring containing
        # the same letter

        # constraints
        # len(s) >= 1 <= 10^5
        # s consists of only uppercase English letters
        # k >= 0 <= len(s)

        # edge cases
        # len(s) == k -> return len(s)

        res = 0

        if k == len(s):
            return len(s)

        else:
            left = 0
            right = 0

            most_c = s[0]
            most_count = 1
            len_window = right - left + 1
            window_count = Counter()
            window_count[s[right]] += 1

            while right < len(s) - 1:
                if (k - (len_window - most_count) == 0) and (s[right + 1] == most_c):
                    # out of replacement
                    # expanding
                    right += 1

                    window_count[s[right]] += 1
                    most_c, most_count = window_count.most_common()[0]
                    # most_count = window_count[most_c]
                    len_window = right - left + 1

                    if len_window > res:
                        res = len_window



                elif k - (len_window - most_count) > 0:
                    # expanding
                    right += 1

                    window_count[s[right]] += 1
                    most_c, most_count = window_count.most_common()[0]
                    # most_count = window_count[most_c]
                    len_window = right - left + 1

                    if len_window > res:
                        res = len_window

                else:
                    # shrinking
                    left += 1
                    if left - 1 >= 0 and s[left - 1] in window_count:
                        window_count[s[left - 1]] -= 1


                    
                    most_c, most_count = window_count.most_common()[0] if len(window_count.most_common()) > 0 else None, 0
                    # most_count = window_count[most_c]
                    len_window = right - left + 1

            return res