class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int sell = 0;
        for(int n:prices){
            buy= std::min(buy, n);
            sell = std::max(sell, n-buy);
        }
        return sell;
    }
};