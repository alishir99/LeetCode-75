class Solution {
public:
    int next(int x){
        int r = 0;
        while (x>0){
            int d = x%10;
            r +=d*d;
            x = x/10;
        }
        return r;
    }
    
    bool isHappy(int n) {
        set<int> seen;
        while (n!=1 && !seen.count(n)){
            seen.insert(n);
            n= next(n);
        }
        
        return (n==1);

    }

};