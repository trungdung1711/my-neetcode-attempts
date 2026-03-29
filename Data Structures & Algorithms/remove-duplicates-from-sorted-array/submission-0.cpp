class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // input: sorted array in non-decreasing order [1, 2, 2, 2, 2]
        // output: sorted array with non dupplicates

        // constraint
        // min(length) = 1

        // edge cases
        // [1] -> [1]
        
        // sol1
        std:: size_t run {1};
        std:: size_t check{0};
        // insert to check + 1
        int k {1};

        while (run < nums.size()) {
            if (nums[run] != nums[check]) {
                // not duplicate
                // insert run
                nums[++check] = nums[run++];
                k++;
            } else {
                // duplicate
                run++;
            }
        }

        return k;
    }
};