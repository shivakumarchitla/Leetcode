class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = 0 
        nums.sort()
        for i in range(len(nums)-1):
            k = nums[i+1] - nums[i]
            if k>n:
                n = k
        return n



        