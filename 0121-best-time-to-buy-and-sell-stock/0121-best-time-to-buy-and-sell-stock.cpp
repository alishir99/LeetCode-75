class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = prices[0];
        int profit = 0;
        for (auto& p : prices){
            if (lowest > p){
                lowest = p;
            }
            else{
                profit = std::max(profit, p-lowest);
            }
        }
        return profit;
    }
};