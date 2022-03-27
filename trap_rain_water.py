class Solution:
    def trap(self, height: List[int]) -> int:
        areas = 0
        max_left = max_right = 0
        l = 0
        r = len(height)-1
        while l < r:
            print(height[l],height[r])
            if height[l] < height[r]:
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    areas += max_left - height[l]
                l +=1
            else:
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    areas += max_right - height[r]
                r -=1
            print(max_left,max_right)
        return areas
            
        
