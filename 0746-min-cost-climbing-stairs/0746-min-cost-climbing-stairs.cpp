class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int first = 0, sec = 0; 
        for (auto c:cost){
            int temp = c+std::min(first,sec);
            sec = first;
            first = temp;
        }
        return first<sec? first : sec;
    }
};