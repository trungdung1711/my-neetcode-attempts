class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // The next index to be inserted
        std:: size_t fill = 0;
        
        for (std:: size_t i = 0; i < nums.size(); ++i) {
            int current = nums[i];

            if (current != val) {
                // It is OKe
                // That hole is filled
                nums[fill] = current;
                ++fill;
            } else {
                // current == val
                // Must drop that values
            }
        }

        return fill;
    }
};