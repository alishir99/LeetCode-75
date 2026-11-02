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
        int slow = n;
        int fast = next(n);
        while (slow !=fast){
            slow = next(slow);
            fast = next(next(fast));
        }
        return fast ==1;
    }

};