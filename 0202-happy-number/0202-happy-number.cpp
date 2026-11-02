class Solution {
public:
    int next (int x){
        int tot = 0;
        while (x>0){
           int d = x % 10;
            tot +=d*d;
            x = x/10;
        }
        return tot;

    }
    bool isHappy(int n) {
        std::unordered_set<int> seen; 
        while (n!= 1 && !seen.count(n)){
            seen.insert(n);
            n = next(n);
        }
        return n==1;
    }

};