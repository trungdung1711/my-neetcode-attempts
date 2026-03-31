class Solution {
public:
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

        // point of decision
        // delete -> 

        // s[a] != s[b]
        // only delete at most one character
        // skip a side or b side

        std:: size_t lives = 1;

        std:: size_t a = 0;
        std:: size_t b = s.size() - 1;

        while (a < b) {
            if (s[a] != s[b]) {
                // point of mismatch
                if (lives == 0) {
                    return false;
                } else {
                    if ((s[a + 1] == s[b])) {
                        // save
                        lives--;
                        a++;
                    } else if ((s[a] == s[b - 1])) {
                        lives--;
                        b--;
                    } else {
                        return false;
                    }
                }
            } else {
                a++;
                b--;
            }
        }

        return true;
    }
};