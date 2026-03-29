class Solution {
public:
    bool isLettersNumbers(char c) {
        return ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z'));
    }


    bool isPalindrome(string s) {
        // input: str
        // true/false if/if not palindrome

        // constraint
        // s.length >= 1 -> be able to run the 2 pointers
        // palindrom only contains letters and numbers

        // edge case
        // empty string -> palindrome
        // s.length = 1 -> palindrome
        // after lowercase/removal -> empty string

        // number : 48 - 57
        // lower  : 97 - 122
        // upper  : 65 - 90
        // diff = 32

        // sol #3
        // It seems that we don't need to remove the weird characters
        std:: size_t a = 0;
        std:: size_t b = s.size() - 1;

        // How can I move the two poiters correctly?
        while (a < b) {
            if (!isLettersNumbers(s[a])) {
                a++;
                continue;
            }
            
            // a is OK
            if (!isLettersNumbers(s[b])) {
                b--;
                continue;
            }

            // b is OK
            // comparison
            if (std:: tolower(s[a]) != std:: tolower(s[b])) {
                return false;
            } else {
                // s[a] == s[b]
                a++;
                b--;
            }
        }

        return true;

        /*

        // sol1: removal -> checking
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

        */
    }
};