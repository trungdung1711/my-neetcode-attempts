class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        std:: vector<int> result;

        std:: unordered_map<int, std:: size_t> freq;

        int threshold = nums.size() / 3;

        for (const int& num : nums) {
            freq[num]++;
            if (freq[num] == threshold + 1) {
                result.push_back(num);
            }
        }

        return result;
    }
};

// to solve it in O(1) space complexity