class Solution {
public:
    int maxArea(vector<int>& height) {
        int x = 0;
        int y = height.size()-1;
        int area = 0;
        while (x<y){
            int level = std::min(height[x], height[y]);
            area = std::max(area, level*(y-x));
            if (height[x]<height[y]){ x++;}
            else{y--;}  
        }
        return area;
    }
};