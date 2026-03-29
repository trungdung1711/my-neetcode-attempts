class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int result = 0;

        std:: unordered_map<int, bool> m;
        for (const int& num : nums) {
            m[num] = true;
        }

        // only starts at specific one
        std:: vector<int> needToCheck;

        for (const int& num : nums) {
            if (m.find(num - 1) == m.end()) {
                // we can't find any number that is less than that values
                // then that should be the start
                needToCheck.push_back(num);
            }
        }

        for (const int& num: needToCheck) {
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