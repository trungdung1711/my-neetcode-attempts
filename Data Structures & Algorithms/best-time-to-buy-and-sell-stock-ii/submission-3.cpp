class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        std:: size_t buy = 0;   // low
        std:: size_t sell = 0;     // high

        for (std:: size_t i = 0; i < prices.size() - 1; ++i) {
            if (prices[i + 1] >= prices[i]) {
                // upward trend
                sell = i + 1;
                if (i + 1 == prices.size() - 1) {
                    // sell it, because it is the last day to consider
                    profit = profit - prices[buy] + prices[sell];
                }
            } else {
                // downward trend
                // sell it
                profit = profit - prices[buy] + prices[sell];
                buy = i + 1;
                sell = i + 1;
            }
        }
        return profit;
        // for (std:: vector<int>:: iterator i = prices.begin(); i != prices.end(); ++i) {
        //     for (std:: vector<int>:: iterator j = ++i; j != prices.end(); ++j) {

        //     }
        // }
    }
};