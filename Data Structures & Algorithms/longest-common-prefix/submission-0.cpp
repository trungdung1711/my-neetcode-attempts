class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std:: string result{""};

        // strs.length >= 1
        std:: string sample {strs[0]};
        std:: size_t len {sample.size()};

        for (std:: size_t i = 0 ; i < len ; ++i) {
            for (std:: size_t j = 1 ; j < strs.size() ; ++j) {
                if (strs[j].size() < i + 1) {
                    return result;
                }

                if (strs[j][i] != sample[i]) {
                    return result;
                } else {
                    // equal
                }
            }
            // all equal to sample[i]
            result += sample[i];
        }

        return result;
    }
};