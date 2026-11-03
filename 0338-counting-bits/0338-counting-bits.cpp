class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> r(n+1);
        for (int i= 0; i<(n+1); i++){
            r[i] = r[i/2]+i%2;
        }
        return r;
    }
};