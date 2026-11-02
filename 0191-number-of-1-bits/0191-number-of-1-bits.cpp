class Solution {
public:
    int hammingWeight(int n) {
        int count = 0;
        while (n>0){
            int b = n%2;
            n = n/2;
            count +=b;
        }
        return count;
    }
};