class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = nums[0];
        std:: size_t freq = 1;

        for (std:: size_t i = 1; i < nums.size() ; ++i) {
            // canceling out
            if (candidate != nums[i]) {
                --freq;

                if (freq == 0) {
                    // it is cancelled out by others
                    // others are also cancelled by that value
                    candidate = nums[i + 1];
                    freq = 1;
                    i = i + 1;
                }
            } else {
                freq++;
            }
        }
        return candidate;
    }
};