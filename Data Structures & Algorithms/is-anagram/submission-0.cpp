class Solution {
public:
    bool isAnagram(string s, string t) {
        // first guard
        if (s.length() != t.length()) {
            return false;
        }

        // same length
        std:: string total = s + t;
        std:: map<char, int> nums;
        for (char c : total) {
            nums[c]++;
        }

        // must be an even number for all characters
        for (const auto& pair : nums) {
            if (pair.second % 2 != 0) {
                return false;
            }
        }

        return true;
    }
};
