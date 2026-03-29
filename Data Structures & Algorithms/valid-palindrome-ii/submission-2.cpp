class Solution {
public:
    bool validPalindromeSub(std:: string& s, std:: size_t left, std:: size_t right) {
        while (left < right) {
            if (s[left] == s[right]) {
                left++;
                right--;
            } else {
                return false;
            }
        }

        return true;
    }


    bool validPalindrome(string s) {
        // input: string
        // output: whether s can be a palindrome after deleting at most one (0 or 1)
        // character from it

        // constraint
        // s.length >=1 -> 2 pointers OK
        // only lowercase English letters

        // edge case
        // s.length == 1 -> return True
        // s.lenth  == 2 -> Normal
        // normal palindrome, there is no need to delete
        // ab cm ba
        // a b a
        // a b c a -> special case ?
        // a b b a -> choose which path to skip ?

        // s[a] != s[b]
        // only delete at most one character
        // skip a side or b side

        std:: size_t left = 0;
        std:: size_t right = s.size() - 1;

        while (left < right) {
            if (s[left] == s[right]) {
                left++;
                right--;
            } else {
                // choose to skip left or right
                // because both can be valid
                // but which one lead to the correct palindrome
                return validPalindromeSub(s, left + 1, right) || validPalindromeSub(s, left, right - 1);
            }
        }

        return true;
    }
};