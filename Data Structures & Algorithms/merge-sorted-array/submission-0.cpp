class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // input: 2 nums1 and nums2
        // 1 2 3 4
        // m, n = number of elements
        // return nums1 -> merge these 2 sorted

        // constraint
        // nums1.length == m + n
        // nums2.length == n
        // size(m) and size(n) can be 0
        // case n == 0 -> stop
        // case 

        // edge case
        // [] [] -> 
        // [1] [] ->
        // [3, 4] []

        if (n == 0) {
            return;
        }

        // m == 0 -> down1 stop
        int down1 {m - 1};
        int down2 {n - 1};
        int last {m + n - 1};

        while (down1 >= 0 && down2 >= 0) {
            if (nums1[down1] >= nums2[down2]) {
                // choose from 1
                nums1[last--] = nums1[down1--];
            } else {
                nums1[last--] = nums2[down2--];
            }
        }

        if (down1 >= 0) {
            // down2 is fully chosen
            // do nothing
        }

        if (down2 >= 0) {
            // nums1 is fully chosen
            // copy remaining nums2 into nums1
            while (down2 >= 0) {
                nums1[last--] = nums2[down2--];
            }
        }
        
        return;
    }
};