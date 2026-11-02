class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = prices[0];
        int profit = 0;
        for (int i = 1; i<prices.size(); i++){
            if (lowest > prices[i]){
                lowest = prices[i];
            }
            profit = std::max(profit, prices[i]-lowest);
        }
        return profit;
    }
};