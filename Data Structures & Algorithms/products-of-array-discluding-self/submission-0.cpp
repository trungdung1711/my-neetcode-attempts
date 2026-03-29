class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std:: vector<int> result;

        std:: vector<int> prefix(nums.size());
        std:: vector<int> suffix(nums.size());

        int p = 1;
        int s = 1;

        for (std:: size_t i = 0; i < nums.size(); ++i) {
            prefix[i] = p;
            suffix[nums.size() - 1 - i] = s;

            p *= nums[i];
            s *= nums[nums.size() - 1 - i];
        }

        for (std:: size_t i = 0; i < nums.size(); ++i) {
            result.push_back(prefix[i] * suffix[i]);
        }

        return result;
    }
};