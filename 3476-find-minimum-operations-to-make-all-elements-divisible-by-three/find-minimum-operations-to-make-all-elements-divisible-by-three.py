class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            ans = nums[i]%3 
            c+= min(ans,3-ans)
        return c
            


        