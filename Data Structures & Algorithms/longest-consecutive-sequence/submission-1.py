class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        res=0

        for i in num :
            if i-1 in num:
                continue
            else:
                ans = 1
                n=i
                while n+1 in num :
                    ans +=1
                    n =n+1

            res = max(res,ans) 

        return res   
        