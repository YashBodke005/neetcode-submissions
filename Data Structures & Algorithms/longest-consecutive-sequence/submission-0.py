class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num= set(nums)
        res = 0
        

        for n in num:
            if n-1 not in num:
                curr = n
                streak = 1
                
                while curr+1 in num:
                    curr+=1
                    streak+=1
                res = max(streak,res)
            
        return res