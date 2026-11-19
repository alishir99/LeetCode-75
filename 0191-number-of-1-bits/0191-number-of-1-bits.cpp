class Solution {
public:
    int hammingWeight(int n) {
        int ans = 0; 
        while (n>0){
            int b = n%2; 
            if (b==1) ans = ans+b; 
            n = n/2; 
        }
        return ans; 
    }
};