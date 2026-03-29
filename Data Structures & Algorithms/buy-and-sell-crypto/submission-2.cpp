class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        for (std:: size_t i = 0; i < prices.size(); ++i) {
            for (std:: size_t j = i + 1; j < prices.size(); ++j) {
                if (-prices[i] + prices[j] > profit) {
                    profit = -prices[i] + prices[j];
                }
            }
        }
        return profit;
    }
};