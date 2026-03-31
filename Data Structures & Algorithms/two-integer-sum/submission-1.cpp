class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std:: map <int, int> helper;
        std:: vector<int> result;

        // map the difference (which is the next number with the index),
        // then if the next value exists helper[next_value] = index
        // return
        for (size_t i = 0; i < nums.size(); ++i) {
            // 1. Check whether helper does contain the dif
            // if yes -> return the current index and the stored index
            // as target - dif + dif = target
            auto it = helper.find(nums[i]);
            if (it != helper.end()) {
                // Find the dif -> match
                result.push_back(i);
                result.push_back(it->second);

                return result;
            }
            // the difference will be the next number to find
            helper.insert({target - nums[i], i});
        }
        // unreachable code
        return result;
    }
};