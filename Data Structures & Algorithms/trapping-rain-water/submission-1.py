class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        maxi = 0
        leftMax = [0]*n
        rightMax = [0]*n
        for i in range(1,n):
            maxi = max(maxi, height[i-1])
            leftMax[i]=maxi

        maxi2= 0
        for i in range(n-2,-1,-1):
            maxi2 = max(maxi2, height[i+1])
            rightMax[i]=maxi2

        for i in range (n):
            res+= max(min(leftMax[i],rightMax[i])-height[i],0)

        return res

        


        
