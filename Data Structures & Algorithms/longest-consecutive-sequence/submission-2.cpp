class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result = 0;

        std:: unordered_map<int, bool> m;
        for (const int& num : nums) {
            m[num] = true;
        }

        for (const int& num: nums) {
            int search = num + 1;
            int size = 1;
            while (m.find(search) != m.end()) {
                // found
                ++size;
                ++search;
            }
            // stop because the sequence break;
            if (result < size) {
                result = size;
            }
        }
        
        return result;
    }
};