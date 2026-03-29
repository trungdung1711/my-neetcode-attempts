class Solution {
public:
    void reverseString(vector<char>& s) {
        // input array of char
        // output reverse version of the array of char

        // edge case:
        // empty string
        // string with length = 1

        // constraint
        // s.length >= 1
        // space complexity O(1)
        // in-place modification

        std:: size_t a = 0;
        std:: size_t b = s.size() - 1;

        while (a < b) {
            char temp = s[a];
            s[a] = s[b];
            s[b] = temp;

            a++;
            b--;
        }

        return;
    }
};