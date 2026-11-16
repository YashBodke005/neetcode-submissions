class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seti = set()
        for i in range(len(nums)):
            if nums[i] in seti:
                return True
            
            seti.add(nums[i])
        

        return False