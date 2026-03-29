class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std:: size_t n{nums.size()};
        std:: vector<int> ans(2 * n);
        std:: size_t i {0};


        for (const int&num : nums) {
            ans[i] = num;
            ans[i + n] = num;
            ++i;
        }

        return ans;
    }
};