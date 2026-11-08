class Solution {
public:
    void backtrack(int open, int close, int n, string& st, vector<string>& out){
        if(st.size()==2*n){
            out.push_back(st);
            return; 
        }
        if(open <n){
            st.push_back('(');
            backtrack(open+1, close, n, st, out);
            st.pop_back();
        }
        if (close < open){
            st.push_back(')');
            backtrack(open, close+1, n, st, out);
            st.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> out; 
        string st; 
        backtrack(0, 0, n, st, out);
        return out;
    }
};