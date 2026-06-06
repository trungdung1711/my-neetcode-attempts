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

            # intitalize
            left = 0
            right = 0

            count = Counter()
            count.update(s[left])

            res = 1

            right = 1

            # is this window valid?
            while right < len(s):
                # right forms the current substring
                # len window
                count.update(s[right])
                common_c, common_count = count.most_common()[0]
                len_window = right - left + 1

                if len_window - common_count <= k:
                    # valid
                    if len_window > res:
                        res = len_window
        
                else:
                    # not valid -> form again
                    while len_window - common_count > k:
                        left += 1
                        count[s[left - 1]] -= 1
                        common_c, common_count = count.most_common()[0]
                        len_window = right - left + 1

                right += 1


            return res