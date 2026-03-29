class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // brute-force approach
        // for every number
        // running a loop from the next number to the end
        // checking whether the sum of i and i indices is target
        // time complexity n(n+1)/2 ~ n^2

        std:: vector<int> result;

        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] == target) {
                    result.push_back(i);
                    result.push_back(j);
                    return result;
                }
            }
        }

        // unrearch code
        return result;
    }
};
