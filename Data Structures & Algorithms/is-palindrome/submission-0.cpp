class Solution {
public:
    bool isPalindrome(string s) {
        // removal and lowercase
        for (std:: string:: iterator i = s.begin(); i != s.end(); ) {
            if (!((*i >= '0' && *i <= '9') || (*i >= 'a' && *i <= 'z') || (*i >= 'A' && *i <= 'Z'))) {
                i = s.erase(i);
            } else {
                // a-z, 0-9, A-Z
                if (*i >= 'A' && *i <= 'Z') {
                    *i = *i + 32;
                }
                i = std:: next(i);
            }
        }
        // check for palindrome

        if (s.size() == 0) {
            return true;
        }

        // size >= 1

        std:: size_t a = 0;
        std:: size_t b = s.size() - 1;

        while (a < b) {
            if (s[a] != s[b]) {
                return false;
            }
            a++;
            b--;
        }
 
        return true;
    }
};
