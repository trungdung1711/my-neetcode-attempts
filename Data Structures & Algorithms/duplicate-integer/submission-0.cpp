class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std:: map<int, int> checks;
        for (auto it : nums) {
            if (checks.find(it) != checks.end()) {
                // Already exists
                return true;
            }
            // Non-exist
            checks.insert({it, 1});
        }

        return false;
    }
};