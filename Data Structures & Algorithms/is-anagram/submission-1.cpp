class Solution {
public:
    bool isAnagram(string s, string t) {
        // first guard
        if (s.length() != t.length()) {
            return false;
        }

        std:: map<char, int> m1;
        std:: map<char, int> m2;

        // same length
        for (int i = 0; i < s.length(); ++i) {
            m1[s[i]]++;
            m2[t[i]]++;
        }

        return m1 == m2;
    }
};
