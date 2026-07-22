class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' O(n2) tc very bad 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]== target:
                    return [i,j]
        '''

        ind = {}
        for i,n in enumerate(nums):
            ind[n]=i

        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in ind and ind[diff]!=i:
                return [i,ind[diff]]

        return []
