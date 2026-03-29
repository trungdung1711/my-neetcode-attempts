class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std:: unordered_map<int, std:: size_t> freq;
        int threshold = nums.size() / 2;

        for (const int& num : nums) {
            // not exist -> 0 -> 1
            freq[num]++;
            if (freq[num] > threshold) {
                return num;
            }
        }
        // garbage
        return nums.size();

        // but this is not space complexity is O(m), m is the number unique elements in the array
    }
};