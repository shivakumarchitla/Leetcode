class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c = 0
        for i in range(len(nums)-1):
            
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] < target:
                    c+=1
        return c


        