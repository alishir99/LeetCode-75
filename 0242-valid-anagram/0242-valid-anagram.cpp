class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){return false;}

        std::unordered_map<char, int> first;
        std::unordered_map<char, int> sec;
        for (int i = 0; i< s.size(); i++){
            first[s[i]] ++;
            sec[t[i]] ++;
        }
        for (auto& n: s){
            if (first[n] != sec[n]){
                return false;
            }
        }
        return true; 
    }
};