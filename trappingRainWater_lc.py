from typing import List

#trapping rainwater 

# at any point, the waterlevel at the 1 width space is the min(rightMax, leftMax)
# where righMax is the highest bar to the right and leftMax is the highst bar to the left
# thus find rmax and lmax for all positions and then the water above waterlevel-heightOfBar, only if this is positive
# add waterlevels

# create rmax -- just traverse from right to left and record max at each point
# same for lmax


class Solution:
    def trap(self, height: List[int]) -> int:
        ln=len(height)
        lmax = [0]*ln
        rmax = [0]*ln

        maxLeft = 0
        for i in range(ln):
            lmax[i]=maxLeft
            if height[i]>=maxLeft:
                maxLeft=height[i]
        
        maxRight=0
        for i in range(ln-1,-1,-1):
            rmax[i]=maxRight
            if height[i]>maxRight:
                maxRight = height[i]
        
        water = 0
        for i in range(ln):
            waterLevel= min(lmax[i], rmax[i])
            if  waterLevel >= height[i]:
                water+= waterLevel - height[i]
        
        return water

s=Solution()

height=[4,3,1,6,0,4,2,2,2,2,3]
height=[12]
water = s.trap(height)

print(water)







