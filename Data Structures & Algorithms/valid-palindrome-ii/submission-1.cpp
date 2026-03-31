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

        // s[a] != s[b]
        // only delete at most one character
        // skip a side or b side

        std:: size_t left = 0;
        std:: size_t right = s.size() - 1;
        bool isDeleted = false;

        while (left < right) {
            if (s[left] == s[right]) {
                left++;
                right--;
            } else {
                // s[left] != s[right] -> point of different
                if (isDeleted) {
                    return false;
                } else {
                    // can be deleted
                    
                    // special case
                    if (left == right - 1) {
                        // can delete either
                        // OK
                        left++;
                    } else {
                        // not special case
                        if (s[left + 1] == s[right]) {
                            isDeleted = true;
                            left++;
                        } else if (s[left] == s[right - 1]) {
                            isDeleted = true;
                            right--;
                        } else {
                            // fail to save
                            return false;
                        }
                    }
                }
            }
        }

        return true;
    }
};