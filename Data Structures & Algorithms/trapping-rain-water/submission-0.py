class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax = [0]*n
        rightmax=[0]*n
        res=[0]*n
        
        
        maxi =0
        for i in range(1,n):
            maxi = max(height[i-1],maxi)
            leftmax[i]=maxi

        maxi2=0
        
        for i in range(n-2,-1,-1):
            maxi2 = max(height[i+1],maxi2)
            rightmax[i]=maxi2


        for i in range(n):
            res[i]= max(min(leftmax[i],rightmax[i])-height[i],0)
        
        return sum(res)

