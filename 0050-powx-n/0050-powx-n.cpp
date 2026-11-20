class Solution {
public:
    double myPow(double x, long long n) {
        long long N = n;
       if (n<0) return 1/myPow(x,-N);
       if (n==0) return 1;
       double h = myPow(x, n/2); 
       if (n%2==0) return h*h;
       else return h*h*x; 
    }
};