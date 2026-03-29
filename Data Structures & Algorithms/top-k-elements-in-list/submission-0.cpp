class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std:: vector<int> result;

        std:: unordered_map<int, int> freq;

        std:: map<int, std:: vector<int>, std:: greater<int>> top;
        

        for (const int& num : nums) {
            // map number and the frequency
            // then how can I take the frequency out?
            freq[num]++;
        }

        for (const auto& pair : freq) {
            // rank by frequency
            top[pair.second].push_back(pair.first);
        }

        std:: size_t c = 0;

        for (const auto& pair : top) {
            
            for (const int& num : pair.second) {

                result.push_back(num);
                c++;
                if (c == k) {
                    return result;
                }
            }
        }

        return {};
    }
};