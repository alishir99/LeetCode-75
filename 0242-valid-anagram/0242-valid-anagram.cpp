class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size()!=t.size()){ return false;}
        std::unordered_map<char, int> a;
        std::unordered_map<char, int> b;
        for (int i = 0; i<s.size(); i++){
            a[s[i]]++; 
            b[t[i]] ++; 
        }
        for (auto& [k,v]:a){
            if (b[k] != v){ return false;}
        }
        return true; 
    }
};