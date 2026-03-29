class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // input: numbers sorted 1, 2, 3
        // two nums that add to target

        // constraint
        // numbers.length >= 2
        // numbers[i] >= -1000, numbers[i] <= 1000
        // solution is unique

        // brute-force approach
        // pairs-checking O(N^2)

        // numbers is sorted
        // + + +: sum is bigger than both -> 2 pointers
        // - 0 +
        // - - 0

        std:: size_t left = 0;
        std:: size_t right = numbers.size() - 1;
        std:: vector<int> result;

        while (left < right) {
            int sum = numbers[left] + numbers[right];

            if (target > sum) {
                left++;
            } else if (target < sum) {
                right--;
            } else {
                result.push_back(++left);
                result.push_back(++right);
                return result;
            }
        }

        // dump
        return result;
    }
};