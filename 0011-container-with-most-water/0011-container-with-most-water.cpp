class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size()-1;
        int area = 0;
        while(l<r){
            int h = std::min(height[l], height[r]);
            area = std::max(area, h*(r-l));
            if(height[l]<height[r]){l++;}
            else {r--;}
        }
        return area;
    }
};