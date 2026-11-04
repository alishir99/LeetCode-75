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
        int slow = n; 
        int fast = next(slow);
        while (slow!=fast){
            slow = next(slow);
            fast = next(next(fast));
        }
        
        return slow ==1;

    }

};